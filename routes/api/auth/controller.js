import jwt from "jsonwebtoken"

import User from "../../../model/user"


/*
    POST /api/auth/register
    {
        username,
        password
    }
*/
export const register = (req, res)=>{
    // res.send('this router is working')
    const { username, password } = req.body
    let newUser = null

    const createUser = (user)=>{
        if (user) {
            throw new Error('username exists')
        } else {
            return User.create(username, password)
        }
    }

    const curUserCnt = (user)=>{
        newUser = user
        return User.count({}).exec()
    }

    const assignAdmin = (count)=>{
        if (count === 1) {
            return newUser.assignAdmin()
        } else {
            return Promise.resolve(false)
        }
    }

    const respond = (isAdmin)=>{
        res.json({
            message: 'registered successfully',
            admin: isAdmin? true: false
        })
    }
    
    const onError = (error)=>{
        res.status(409).json({
            message: error.message
        })
    }
    // console.log(User)
    // console.log(User.findOne)
    // console.log(User.findOneByUsername)
    User.findOneByUsername(username)
    .then(createUser)
    .then(curUserCnt)
    .then(assignAdmin)
    .then(respond)
    .catch(onError)
    
}

    
/*
    POST /api/auth/login
    {
        username,
        password
    }
*/
export const login = (req, res)=>{
    // res.send('login api is working')
    // console.log(req)
    const { username, password } = req.body
    const secret = req.app.get('jwt-secret')

    const checkUser = (user)=>{
        if(!user) {
            throw new Error('login failed')
        } else {
            if (user.verify(password)) {
                // create a promise that generate jwt asynchronously
                const jwtGenProm = new Promise((resolve, reject)=>{
                    jwt.sign(
                        {
                            _id: user._id,
                            username: user.username,
                            admin: user.admin
                        },
                        secret,
                        {
                            expiresIn: '7d',
                            issuer: 'ging',
                            subject: 'userInfo'
                        },
                        (err, token)=>{
                            // console.log(token)
                            if (err) reject(err)
                            resolve(token)
                        }
                    )
                })

                return jwtGenProm
            } else {
                throw new Error('login failed')
            }
        }
    }

    const respond = (token)=>{
        res.json({
            message: 'logged in successfully',
            token: token
        })
    }

    const onError = (error)=>{
        res.status(403).json({
            message: error.message
        })
    }

    User.findOneByUsername(username)
    .then(checkUser)
    .then(respond)
    .catch(onError)
}


/*
    GET /api/auth/checkjwt
*/
export const checkJWT = (req, res)=>{
    // const token = req.headers['x-access-token'] || req.query.token

    // if (!token) {
    //     return res.status(403).json({
    //         success: false,
    //         message: 'not logged in'
    //     })
    // }

    // const jwtVerifyProm = new Promise((resolve, reject)=>{
    //     jwt.verify(token, req.app.get('jwt-secret'), (err, decoded)=>{
    //         if (err) reject(err)
    //         resolve(decoded)
    //     })
    // })

    // const respond = (token)=>{
    //     res.json({
    //         success: true,
    //         info: token
    //     })
    // }

    // const onError = (error)=>{
    //     res.status(403).json({
    //         success: false,
    //         message: error.message
    //     })
    // }

    // jwtVerifyProm.then(respond).catch(onError)
    // 미들웨어로 이동,,,

    res.json({
        success: true,
        info: req.decoded
    })
}
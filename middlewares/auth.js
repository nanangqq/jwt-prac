import jwt from "jsonwebtoken"

const authMiddleware = (req, res, next)=>{
    const token = req.headers['x-access-token'] || req.query.token

    if (!token) {
        return res.status(403).json({
            success: false,
            message: 'not logged in'
        })
    }

    const jwtVerifyProm = new Promise((resolve, reject)=>{
        jwt.verify(token, req.app.get('jwt-secret'), (err, decoded)=>{
            if (err) reject(err)
            resolve(decoded)
        })
    })

    // const respond = (token)=>{
    //     res.json({
    //         success: true,
    //         info: token
    //     })
    // }

    const onError = (error)=>{
        res.status(403).json({
            success: false,
            message: error.message
        })
    }

    jwtVerifyProm.then((decoded)=>{
        req.decoded = decoded
        next()
    }).catch(onError)
}

export default authMiddleware
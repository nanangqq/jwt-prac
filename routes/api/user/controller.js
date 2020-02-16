import User from "../../../model/user";

/* 
    GET /api/user/list
*/
export const list = (req, res)=>{
    if (!req.decoded.admin) {
        return res.status(403).json({
            message: 'you are not an admin'
        })
    }

    User.find({}).then(users=>{
            res.json({users})
    })
}

/*
    POST /api/user/assign-admin/:username
*/
export const assignAdmin = (req, res)=>{
    if (!req.decoded.admin) {
        return res.status(403).json({
            message: 'you are not an admin'
        })
    }

    User.findOneByUsername(req.params.username)
    .then(
        user=>user.assignAdmin()
    ).then(
        res.json({
            success: true
        })
    )
}
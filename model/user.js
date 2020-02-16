import mongoose from "mongoose"
import crypto from "crypto"
import config from "../config"

const Schema = mongoose.Schema
const User = new Schema({
    username: String,
    password: String,
    admin: { type: Boolean, default: false }
})

// create new User document
User.statics.create = function (username, password) {
    // 비번 암호화 
    const encrypted = crypto.createHmac('sha1', config.secret).update(password).digest('base64')

    const user = new this({
        username,
        password: encrypted
    })

    // return the Promise
    return user.save()
}

// find one user by using username
User.statics.findOneByUsername = function (username) {
    return this.findOne({
        username
    }).exec()
}


// verify the password of the User documment
User.methods.verify = function (password) {
    const encrypted = crypto.createHmac('sha1', config.secret).update(password).digest('base64')
    return this.password === encrypted
}

User.methods.assignAdmin = function () {
    this.admin = true
    return this.save()
}

// console.log(User)
// console.log(User.static)

export default mongoose.model('User',User)
// module.exports = mongoose.model('User', User)



// 화살표함수로 메소드 정의하면 this 가 제대로 바인딩 되지 않음!!!
// const User = mongoose.model('User', new Schema({
//     username: String,
//     password: String,
//     admin: { type: Boolean, default: false }
// }));

// User.statics.create = (username, password)=>{
//     const user = new this({
//         username,
//         password
//     });

//     return user.save()
// };

// User.statics.findOneByUsername = (username)=>{
//     // console.log(username)
//     return this.findOne({
//         username
//     }).exec()
// };

// User.methods.verify = (password)=>{
//     return this.password === password
// };

// User.methods.assignAdmin = ()=>{
//     this.admin = true
//     return this.save()
// };
// console.log(User)
// console.log(User.statics)
// export default User
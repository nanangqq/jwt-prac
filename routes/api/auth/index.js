import { Router } from "express"
import { register, login, checkJWT} from "./controller"
import authMiddleware from "../../../middlewares/auth"

const router = Router()
router.post('/register', register)
router.post('/login', login)

router.use('/checkjwt', authMiddleware)
router.get('/checkjwt', checkJWT)

export default router
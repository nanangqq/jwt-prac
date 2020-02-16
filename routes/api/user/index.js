import { Router } from "express"
import { list, assignAdmin } from "./controller"

const router = Router()

router.get('/list', list)
router.post('/assign-admin/:username', assignAdmin)

export default router
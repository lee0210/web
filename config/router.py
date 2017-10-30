from locode import router

router.middleware('auth', 'middleware.auth@auth').register()
router.post('/action/login', 'middleware.auth@login').register()
router.get('/action/checkauth', 'middleware.auth@check_auth').register()
router.get('/action/user', 'user@get').before_process(['auth']).register()
router.post('/action/upload', 'action.upload_file@process').before_process(['auth']).register()
#router.post('/action/upload', 'action.upload_file@process').register()
router.get('/action/test', 'user@test').register()
router.post('/action/testpost', 'user@post').before_process(['auth']).register()
router.post('/action/testpostjson', 'user@postjson').register()
router.get('/action/abc', 'user@event').register()

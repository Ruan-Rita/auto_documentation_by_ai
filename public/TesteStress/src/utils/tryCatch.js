exports.tryCatch = (controller) => async (req, res, next) => {
    try {
        await controller(req, res)
    } catch (error) {
        console.log('Error: ', error.message)
        next(error)
    }
}
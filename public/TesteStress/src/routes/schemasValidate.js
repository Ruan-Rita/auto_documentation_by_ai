const Joi = require('joi')

exports.schemaSendRequest = Joi.object({
    domain: Joi.string().required(),
    request: Joi.number().min(1).required()
})
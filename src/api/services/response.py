from flask import jsonify


def make(error, message=None, response=None):
    """
    API response generator function.
    :param error: True if the response has to be flagged as an error, False otherwise.
    :param message: Error message string formatted. Only being used when [error == True]
    :param response: JSON response dictionary formatted. Only being used when [error == False]
    :return: JSON response.
    """
    response_dict = dict(error=error)
    if error:
        assert type(message) is str
        response_dict['message'] = message
    else:
        assert type(response) is dict
        response_dict['response'] = response
    return jsonify(response_dict), 200

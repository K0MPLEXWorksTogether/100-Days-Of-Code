"""
This file contains a set of utilities written for the pixela, which 
is a habit tracking system. 
"""

import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

def createPixelaUser(token: str, username: str, termsOfService: str, notMinor: str, thanksCode: str=None) -> tuple[bool | str]:
    """
    Call this function to create an account on pixela.

    Arguments:
        token(str): The private token on pixela for your account. It must be between 8 and 128 characters.

        username(str): The username for you account. It must be 8 to 128 characters, and must not start with a number.

        termsOfService(str): Specify yes or no, for agreeing with terms of service. You can find the terms at:
        "https://github.com/a-know/Pixela/wiki/Terms-of-Service"

        notMinor(str): Specify yes or no to represent if you are a minor.

        thanksCode(str)(Optional): The default value for thanksCode is None. If you have one, you can pass it here. Else, do not pass anything for this attribute.

    Returns:
        A tuple of a boolean, and a strings. The boolean represents the if the operation was successful. If successful, the following two indices contain the token and the username.
    """

    createUserPayload = {
        "token": token,
        "username": username,
        "agreeTermsOfService": termsOfService,
        "notMinor": notMinor,
    }

    if thanksCode:
        createUserPayload["thanksCode"] = thanksCode
    
    createUserResponse = requests.post(url=PIXELA_ENDPOINT, json=createUserPayload)
    result = createUserResponse.json()
    if result["isSuccess"]:
        return (True, token, username)
    else:
        print(f"The above operation failed due as: {result["message"]}")
        return (False, "", "")

def createPixelaGraph(token: str, username: str, graph_id: str, graph_name: str, unit: str, datatype: str, color: str) -> bool:
    """
    Call this function to create a graph under your username.

    Arguments:
        token(str): The token that was used to create your account.
        username(str): The account's username.
        graph_id(str): The id of the graph you want to create. This will be the used to generate an endpoint for a graph on your account.
        graph_name(str): The name for your graph. This will be visible in the webpage.
        unit(str): The unit of measurement, for example kilometers, or push-ups.
        datatype(str): The datatype of the unit. It can be either int or float.
        color(str): The color for the pixels created in the graph. Supported colors are
        shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) and kuro (black).

    Returns:
        A bool representing success or failure. The reason for failure is printed on the console.
    """
    createGraphEndpoint = f"{PIXELA_ENDPOINT}/{username}/graphs"
    createGraphHeader = {
        "X-USER-TOKEN": token
    }

    createGraphPayload = {
        "id": graph_id,
        "name": graph_name,
        "unit": unit,
        "type": datatype,
        "color": color
    }

    createGraphResponse = requests.post(url=createGraphEndpoint, json=createGraphPayload, headers=createGraphHeader)
    result = createGraphEndpoint.json()

    if result["isSuccess"]:
        return True
    else:
        print(f"The above operation failed as: {result["message"]}")
        return False

def createPixelaPixel(token: str, username: str, graph_id: str,quantity: str, datetime: str = datetime.now().strftime("%Y%m%d") ) -> bool:
    """
    Call the function to create a pixel for a graph.
    """
    pass
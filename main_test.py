from main import handle_event


def test_curtains_up_command():
    """
    must set env vars:
    SERVER_URL, USERNAME, HASHED_PASSWORD
    """
    my_command = {
        "type": "com.taphome.curtains.SetCurtainsUpCommand",
        "data": {"curtain_ids": ["I14@@", "I15@@", "I16@"]},
    }
    handle_event(my_command, None)


def test_curtains_down_command():
    """
    must set env vars:
    SERVER_URL, USERNAME, HASHED_PASSWORD
    """
    my_command = {
        "type": "com.taphome.curtains.SetCurtainsDownCommand",
        "data": {"curtain_ids": ["I14@@", "I15@@", "I16@"]},
    }
    handle_event(my_command, None)

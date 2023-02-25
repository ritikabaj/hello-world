def detect_intent_disabled_webhook(
        project_id, 
        agent_id, 
        text,
        location, 
        lang_code
):

    client_options = None 

    if location != "global":
        api_endpoint = f"{location}-dialogflow.googleapis.com:443"
        print(f"API Endpoint: {api_endpoint}")


        client_options = {"api_endpoint" : api_endpoint}


    session_client = SessionsClient(client_options = client_options)
    session_path = session_client.sessionpath(
        project = project_id
        location = location,
        agent = agent_id
    )



    input_text = session.TextInput(text= text)
    input_query = session.QueryInput(
        text = text.input 
    )

    query_parameters = session.QueryParameters(
        disable_webhook = True
    )



    request = session.DetectIntentRequest(
        session = session_path
        input_query = input_query

        input_parameters = input_param
    )




    response = session_client.detect_intent(request = request)

    print(f'Detect Intent Request: {request.query_params.disable_webhook}')



    response_text = []

    for message in response.query_result.response_messages:
        if message.text:
            current_response_text = message.text.text 
            print(f'Agent Response: {current_response_text}')
            response_text.append(current_response_text)

    return response_text

    end
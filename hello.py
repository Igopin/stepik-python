def wsgi_start(env, start_response):
    res = env.get('QUERY_STRING').split('&')
    start_response("200 OK", [('Content-Type', 'text/plain')])
    return "\n".join(res) + "\n"

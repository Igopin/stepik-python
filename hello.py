def wsgi_start(env, start_response):
    res = env.get('QUERY_STRING').replace('&', '\n').encode()
    start_response("200 OK", [('Content-Type', 'text/plain')])
    return iter([res])

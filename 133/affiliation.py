def generate_affiliation_link(url):
    id = url.split("/")[5]
    return f"http://www.amazon.com/dp/{id}/?tag=pyb0f-20"

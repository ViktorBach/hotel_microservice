import requests

def get_reviews_for_guest(guest_id):
    # URL for the `reviews` service container
    url = f"http://reviews-container:5001/reviews/{guest_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error fetching reviews: {response.status_code}"

# Example usage
guest_id = 101
reviews = get_reviews_for_guest(guest_id)
print(reviews)
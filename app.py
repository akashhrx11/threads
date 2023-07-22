from threads import Threads
import json

def extract_shortcode_from_url(url):
    # Check if the URL contains "/post/" or "/t/" to determine the shortcode position
    if "/post/" in url:
        shortcode_position = url.find("/post/") + len("/post/")
    elif "/t/" in url:
        shortcode_position = url.find("/t/") + len("/t/")
    else:
        return None  # Invalid URL format, return None

    # Extract the shortcode from the URL
    shortcode = url[shortcode_position:]

    # Remove any query parameters (if present) from the shortcode
    shortcode = shortcode.split('?')[0]

    # Remove trailing slash (if present)
    shortcode = shortcode.rstrip('/')

    return shortcode
# Example URLs
urls = [
    "https://www.threads.net/t/Cu5wcnDp9aq/?igshid=NTc4MTIwNjQ2YQ=="

]

# Extract shortcodes using the function and print the results
for url in urls:
    shortcode = extract_shortcode_from_url(url)
    print(f"URL: {url}\nShortcode: {shortcode}\n")

threads = Threads()
thread_id = threads.public_api.get_thread_id(url_id=shortcode)
thread_id
print("User ID:", thread_id)
thread = threads.public_api.get_thread(id=thread_id)
thread
thread_json = json.dumps(thread, indent=4)
print("Thread information (JSON format):\n", thread_json)
    

# Parse the JSON string into a Python dictionary
thread_data = json.loads(thread_json)

# Access the "post" code from the dictionary
videourl = thread_data["data"]["data"]["containing_thread"]["thread_items"][0]["post"]["code"]
print("Video URL:", videourl)

# Access the containing_thread dictionary
containing_thread = thread_data["data"]["data"]["containing_thread"]

# Access the thread_items list
thread_items = containing_thread["thread_items"]

# Loop through each item and access the image_versions2 URLs
for item in thread_items:
    if "image_versions2" in item["post"]:
        image_versions = item["post"]["image_versions2"]["candidates"]
        if image_versions:
            first_url = image_versions[0]["url"]
            print("First URL in image_versions2:", first_url)

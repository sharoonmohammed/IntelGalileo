import urllib2
import base64
from xml.dom.minidom import parse

def gmail_unread_count(user, password):
    """
        Takes a Gmail user name and password and returns the unread
        messages count as an integer.
    """
    # Build the authentication string
    b64auth = base64.encodestring("%s:%s" % (user, password))
    auth = "Basic " + b64auth

    # Build the request
    req = urllib2.Request("https://mail.google.com/mail/feed/atom/")
    req.add_header("Authorization", auth)
    handle = urllib2.urlopen(req)

    # Build an XML dom tree of the feed
    dom = parse(handle)
    handle.close()

    # Get the "fullcount" xml object
    count_obj = dom.getElementsByTagName("fullcount")[0]
    # get its text and convert it to an integer
    return int(count_obj.firstChild.wholeText)

print gmail_unread_count('xxx@gmail.com', 'password')

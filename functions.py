import regex

class InvalidURLError(Exception):
    def __init__(self, url, service):
        self.message = f" '{url}' is not a valid {service} URL, please input another"
        super().__init__(self.message)

#-----------------------------------------------------------------------------
#yt
def youtube_(url):
    ex = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"

    try:
        result = regex.search(ex, url)
        video_id = result.groups()[4]
    except Exception:
        raise InvalidURLError(url, "Youtube")
    
    iframe = f"""
<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
<a href="{url}"><img src="https://img.youtube.com/vi/{video_id}/0.jpg"></a>
</iframe>
"""
    return iframe

#twitter
def twitter_(url):
    ex = r"(?:https?:)?\/\/(?:[A-z]+\.)?twitter\.com\/@?(?P<username>[A-z0-9_]+)\/status\/(?P<tweet_id>[0-9]+)\/?"
    try:
        result = regex.search(ex, url)
        tweet_id = result.groupdict()["tweet_id"]
        username = result.groupdict()["username"]
    except Exception:
        raise InvalidURLError(url, "Twitter")

    iframe = f"""
<iframe height="250" width="100%"
src="https://twitframe.com/show?url=https://twitter.com/OlliLuksic/status/{tweet_id}" frameborder = "0"><a href={url}> Tweet by {username}</a></iframe>
"""
    return iframe

#vimeo
def vimeo_(url):
    ex = r"(?:https?:)?\/\/(?:(?:www)?vimeo\.com|player.vimeo.com\/video)\/(?P<id>[0-9]+)"
    try:
        result = regex.search(ex, url)
        vimeo_id = result.groupdict()["id"]
    except Exception:
        raise InvalidURLError(url, "Vimeo")

    iframe = f"""
<iframe src="https://player.vimeo.com/video/{vimeo_id}" width="640" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe><a href={url}>Vimeo-Video</a>
"""
    return iframe

#giphy
def giphy_(url):
    ex = r"(?:https?:\/\/(?|media\.giphy\.com\/media\/([^ \/\n]+)\/giphy\.gif|i\.giphy\.com\/([^ \/\n]+)\.gif|giphy\.com\/gifs\/(?:.*-)?([^ \/\n]+)))"
    try:
        result = regex.search(ex, url)
        gif_id = result.groups()[0]
    except Exception:
        raise InvalidURLError(url, "Giphy")

    iframe = f"""
<iframe src="https://giphy.com/embed/{gif_id}" width="100%" height="450" frameBorder="0" class="giphy-embed" allowFullScreen><a href="{url}">GIPHY</a></iframe>
"""
    return iframe

#website
def website_(url):
    ex = r"^([a-z][a-z0-9\*\-\.]*):\/\/(?:(?:(?:[\w\.\-\+!$&'\(\)*\+,;=]|%[0-9a-f]{2})+:)*(?:[\w\.\-\+%!$&'\(\)*\+,;=]|%[0-9a-f]{2})+@)?(?:(?:[a-z0-9\-\.]|%[0-9a-f]{2})+|(?:\[(?:[0-9a-f]{0,4}:)*(?:[0-9a-f]{0,4})\]))(?::[0-9]+)?(?:[\/|\?](?:[\w#!:\.\?\+=&@!$'~*,;\/\(\)\[\]\-]|%[0-9a-f]{2})*)?$"
    try:
        result = regex.search(ex, url)
        url = result[0]
    except Exception:
        raise InvalidURLError(url, "Website")

    iframe = f"""---
<iframe src="{url}" height="450px" width="100%"><a href={url}> Website-Link </a></iframe>
"""
    return iframe


#-----------------------------------------------------------------------------
#code embeds

def codepen_(url):
    ex = r"((\/\/\/?|https?:\/\/)?(www\.)?codepen.io\/(?<author>.+)\/(?P<blob>pen+)\/(?<pen>.+([?#].*)?))"
    try:
        result = regex.search(ex, url).groupdict()
        user , pen = result["author"], result["pen"]
    except Exception:
        raise InvalidURLError(url, "CodePen")
    
    iframe = f"""
<iframe height="265" width="100%" scrolling="no" src="https://codepen.io/{user}/embed/{pen}?height=265&theme-id=light&default-tab=css,result" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen>
See the Pen <a href="{url}"> by <a href='https://codepen.io/{user}'>{user}</a>
</iframe>
"""
    return iframe

def jsfiddle_(url):
    ex = r"((\/\/\/?|https?:\/\/)?(www\.)?jsfiddle.net\/(?<author>.+)\/(?<fiddle>.+([?#].*)?))"
    try:
        result = regex.search(ex, url).groupdict()
        author, fiddle = result["author"], result["fiddle"]
    except:
        raise InvalidURLError(url, "JSFiddle")

    if not url[-1] == "/":
        url += "/"

    iframe = f"""
<iframe height="300" width="100%" src="{url}/embedded/" allowfullscreen="allowfullscreen" allowpaymentrequest frameborder="0">
A <a href="{url}">JSFiddle</a> by <a href="https://jsfiddle.net/user/{author}">{author}</a>
</iframe>
"""
    return iframe

#all github things

import requests
import base64
import json


def github_(url):
    ex = r"(?:https?:)?\/\/(?:www\.)?github\.com\/(?P<user>[A-z0-9_-]+)\/(?P<repo>[A-z0-9_-]+)\/(?P<blob>blob+)\/(?P<branch>[A-z0-9_-]+)\/(?<path>.+)"

    try:
        result = regex.search(ex, url).groupdict()
        user = result["user"]
    except:
        raise InvalidURLError(url, "GitHub")

    request_url = f'https://api.github.com/repos/{user}/{result["repo"]}/contents/{result["path"]}'
    response = requests.get(request_url).json()

    file_name = response["name"]
    b64_content = response["content"]
    content = base64.b64decode(b64_content).decode()

    highlight = language_check(file_name)
    
    content = f"""```{highlight}
{content}
```
[{file_name}]({url}) by [{user}](https://github.com/{user}), hosted on [GitHub](https://github.com)
"""

    return content


def language_check(file_name):

    f = open("languages.json")
    l_dict = json.load(f)
    try:
        suffix = file_name.split(".")[1]
        suffix = "." +suffix
        highlight = l_dict[suffix]
    except:
        highlight = ""
    return highlight


# gist

def gist_(url):
    ex = r"(?:https?:)?\/\/(?:gist\.)?github\.com\/(?P<user>[A-z0-9_-]+)\/(?P<id>[A-z0-9_-]+)"
    try:
        result = regex.search(ex, url).groupdict()
        user = result["user"]
    except:
        raise InvalidURLError(url, "Gist")

    headers = {"accept": "application/vnd.github.v3.raw+json"}
    request_url = f"https://api.github.com/gists/{result['id']}"
    response = requests.get(request_url, headers = headers).json()

    files = ""
    for file in response["files"].values():
        filename = file["filename"]
        content = file["content"]
        
        highlight = language_check(filename)
        
        txt = f"""```{highlight}
{content}
```
Gist [{filename}]({url}) by [{user}](https://github.com/{user})
"""
        files += txt
    
    return files

def decider_(url):
    if "gist." in url:
        return gist_(url)
    if "github." in url:
        return github_(url)
    else:
        raise InvalidURLError(url, "GitHub")

#-----------------------------------------------------------------------------
#documents

def google_drive_(url):
    ex = r"(?:https?:)?\/\/(?:(?P<service>drive|docs)\.)?google\.com\/(?P<type>[A-z0-9_-]+)\/(?P<blob>d+)\/(?P<id>[A-z0-9_-]+)?"
    try:
        result = regex.search(ex, url).groupdict()
        id = result["id"]
        service = result["service"]
    except Exception:
        raise InvalidURLError(url, "Google")

    iframe = f"""
<iframe src="https://drive.google.com/file/d/{id}/preview" width="100%" height="480" allowfullscrenn="True" frameborder="0"> <a href="{url}"> Google {service} File </a></iframe>
"""
    return iframe
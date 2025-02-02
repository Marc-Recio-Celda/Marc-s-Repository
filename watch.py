"""
It turns out that (most) YouTube videos can be embedded in other websites, just like the above. For instance, if you visit https://youtu.be/xvFZjo5PgG0 on a laptop or desktop,
click Share, and then click Embed, you’ll see HTML (the language in which web pages are written) like the below, which you could then copy into your own website’s source code,
wherein iframe is an HTML “element,” and src is one of several HTML “attributes” therein, the value of which, between quotes, is https://www.youtube.com/embed/xvFZjo5PgG0.

<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0?si=mp_y9PmgY6z2ZwDp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Because some HTML attributes are optional, you could instead minimally embed just the below.

<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
Suppose that you’d like to extract the URLs of YouTube videos that are embedded in pages (e.g., https://www.youtube.com/embed/xvFZjo5PgG0), converting them back to shorter,
shareable youtu.be URLs (e.g., https://youtu.be/xvFZjo5PgG0) where they can be watched on YouTube itself.

In a file called watch.py, implement a function called parse that expects a str of HTML as input, extracts any YouTube URL that’s the value of a src attribute of an iframe element therein,
and returns its shorter, shareable youtu.be equivalent as a str. Expect that any such URL will be in one of the formats below. Assume that the value of src will be surrounded by double quotes.
And assume that the input will contain no more than one such URL. If the input does not contain any such URL at all, return None.

http://youtube.com/embed/xvFZjo5PgG0
https://youtube.com/embed/xvFZjo5PgG0
https://www.youtube.com/embed/xvFZjo5PgG0
Structure watch.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required,
to use re and/or sys.

"""
import re

def main():
    #<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0?si=mp_y9PmgY6z2ZwDp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
    #clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    print(parse('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'))

def parse(s):
    #if imput != Url, return None
    #take an src attribute od an iframe element
    if matches := re.search(r"^<iframe.*(?P<VideoDomain>https?://)(?:www.)?(?P<Yt>youtu)be\.com/embed(?P<VideoLink>/xvFZjo5PgG0).*</iframe>" , s, re.IGNORECASE):
        video_domain = matches.group("VideoDomain")
        yt_dom = matches.group("Yt")
        video_link = matches.group("VideoLink")

        if domain_match := re.search(r"(http://)", video_domain):
            replace_dom = domain_match.group(1)
            def_domain = re.sub(r"http://", r"https://", replace_dom)
            return f"{def_domain}{yt_dom}.be{video_link}"
        else:
            def_domain = video_domain
            return f"{def_domain}{yt_dom}.be{video_link}"

if __name__ == "__main__":
    main()


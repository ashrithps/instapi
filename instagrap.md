================================================
FILE: README.md
================================================
If you want to work with Instagrapi (business interests), we strongly advise you to prefer [HikerAPI SaaS](https://hikerapi.com/p/bkXQlaVe) project.
However, you won't need to spend weeks or even months setting it up.
The best service available today is [HikerAPI SaaS](https://hikerapi.com/p/bkXQlaVe), which handles 4–5 million daily requests, provides support around-the-clock, and offers partners a special rate.
In many instances, our clients tried to save money and preferred instagrapi, but in our experience, they ultimately returned to [HikerAPI SaaS](https://hikerapi.com/p/bkXQlaVe) after spending much more time and money.
It will be difficult to find good accounts, good proxies, or resolve challenges, and IG will ban your accounts.

The instagrapi more suits for testing or research than a working business!

✨ [aiograpi - Asynchronous Python library for Instagram Private API](https://github.com/subzeroid/aiograpi) ✨

### We recommend using our services:

* [LamaTok](https://lamatok.com/p/B9ScEYIQ) for TikTok API 🔥
* [HikerAPI](https://hikerapi.com/p/bkXQlaVe) for Instagram API ⚡⚡⚡
* [DataLikers](https://datalikers.com/p/S9Lv5vBy) for Instagram Datasets 🚀

[![Package](https://github.com/subzeroid/instagrapi/actions/workflows/python-package.yml/badge.svg?branch=master&1)](https://github.com/subzeroid/instagrapi/actions/workflows/python-package.yml)
[![PyPI](https://img.shields.io/pypi/v/instagrapi)](https://pypi.org/project/instagrapi/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/instagrapi)
![Checked with mypy](https://img.shields.io/badge/mypy-checked-blue)

> To run instagrapi you may need a [cheap and powerful server](https://powervps.net/?from=96837), I recommend using my promo you will support the author of this library!

Features:

* Getting public data of user, posts, stories, highlights, followers and following users
* Getting public email and phone number, if the user specified them in his business profile
* Getting public data of post, story, album, Reels, IGTV data and the ability to download content
* Getting public data of hashtag and location data, as well as a list of posts for them
* Getting public data of all comments on a post and a list of users who liked it
* Management of proxy, mobile devices and challenge resolver
* Login by username and password, sessionid and support 2FA
* Managing messages and threads for Direct and attach files
* Download and upload a Photo, Video, IGTV, Reels, Albums and Stories
* Work with Users, Posts, Comments, Insights, Collections, Location and Hashtag
* Insights by account, posts and stories
* Like, following, commenting, editing account (Bio) and much more else

# instagrapi - Unofficial Instagram API for Python

Fast and effective Instagram Private API wrapper (public+private requests and challenge resolver) without selenium. Use the most recent version of the API from Instagram, which was obtained using reverse-engineering with Charles Proxy and [Proxyman](https://proxyman.io/).

*Instagram API valid for **25 May 2025** (last reverse-engineering check)*

Support **Python >= 3.9**

For any other languages (e.g. C++, C#, F#, D, [Golang](https://github.com/subzeroid/instagrapi-rest/tree/main/golang), Erlang, Elixir, Nim, Haskell, Lisp, Closure, Julia, R, Java, Kotlin, Scala, OCaml, JavaScript, Crystal, Ruby, Rust, [Swift](https://github.com/subzeroid/instagrapi-rest/tree/main/swift), Objective-C, Visual Basic, .NET, Pascal, Perl, Lua, PHP and others), I suggest using [instagrapi-rest](https://github.com/subzeroid/instagrapi-rest)

[Support Chat in Telegram](https://t.me/instagrapi)
![](https://gist.githubusercontent.com/m8rge/4c2b36369c9f936c02ee883ca8ec89f1/raw/c03fd44ee2b63d7a2a195ff44e9bb071e87b4a40/telegram-single-path-24px.svg) and [GitHub Discussions](https://github.com/subzeroid/instagrapi/discussions)


## Features

1. Performs [Web API](https://subzeroid.github.io/instagrapi/usage-guide/fundamentals.html) or [Mobile API](https://subzeroid.github.io/instagrapi/usage-guide/fundamentals.html) requests depending on the situation (to avoid Instagram limits)
2. [Login](https://subzeroid.github.io/instagrapi/usage-guide/interactions.html) by username and password, including 2FA and by sessionid (and uses Authorization header instead Cookies)
3. [Challenge Resolver](https://subzeroid.github.io/instagrapi/usage-guide/challenge_resolver.html) have Email and SMS handlers
4. Support [upload](https://subzeroid.github.io/instagrapi/usage-guide/media.html) a Photo, Video, IGTV, Reels, Albums and Stories
5. Support work with [User](https://subzeroid.github.io/instagrapi/usage-guide/user.html), [Media](https://subzeroid.github.io/instagrapi/usage-guide/media.html), [Comment](https://subzeroid.github.io/instagrapi/usage-guide/comment.html), [Insights](https://subzeroid.github.io/instagrapi/usage-guide/insight.html), [Collections](https://subzeroid.github.io/instagrapi/usage-guide/collection.html), [Location](https://subzeroid.github.io/instagrapi/usage-guide/location.html) (Place), [Hashtag](https://subzeroid.github.io/instagrapi/usage-guide/hashtag.html) and [Direct Message](https://subzeroid.github.io/instagrapi/usage-guide/direct.html) objects
6. [Like](https://subzeroid.github.io/instagrapi/usage-guide/media.html), [Follow](https://subzeroid.github.io/instagrapi/usage-guide/user.html), [Edit account](https://subzeroid.github.io/instagrapi/usage-guide/account.html) (Bio) and much more else
7. [Insights](https://subzeroid.github.io/instagrapi/usage-guide/insight.html) by account, posts and stories
8. [Build stories](https://subzeroid.github.io/instagrapi/usage-guide/story.html) with custom background, font animation, link sticker and mention users
9. In the next release, account registration and captcha passing will appear

## Telegram Bot for Download Posts, Stories and Highlights

* https://t.me/InstaSurfBot
* https://t.me/InstaBlastBot
* https://t.me/InstaSavePremiumBot
* https://t.me/InstaCopierBot
* https://t.me/InstaMemoBot

### Installation

```
pip install instagrapi
```

### Basic Usage

``` python
from instagrapi import Client

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

user_id = cl.user_id_from_username(ACCOUNT_USERNAME)
medias = cl.user_medias(user_id, 20)
```

### Session with persistence

``` python
from instagrapi import Client

cl = Client()
cl.login(USERNAME, PASSWORD)
cl.dump_settings("session.json")

# reload later without entering credentials again
cl = Client()
cl.load_settings("session.json")
cl.login(USERNAME, PASSWORD)
```

### Login using a sessionid

``` python
from instagrapi import Client

cl = Client()
cl.login_by_sessionid("<your_sessionid>")
```

### List and download another user's posts

``` python
from instagrapi import Client

cl = Client()
cl.login(USERNAME, PASSWORD)

target_id = cl.user_id_from_username("target_user")
posts = cl.user_medias(target_id, amount=10)
for media in posts:
    # download photos to the current folder
    cl.photo_download(media.pk)

See [examples/session_login.py](examples/session_login.py) for a standalone script demonstrating these login methods.
```

<details>
    <summary>Additional example</summary>

```python
from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag

cl = Client()
cl.login(USERNAME, PASSWORD, verification_code="<2FA CODE HERE>")

media_pk = cl.media_pk_from_url('https://www.instagram.com/p/CGgDsi7JQdS/')
media_path = cl.video_download(media_pk)
subzeroid = cl.user_info_by_username('subzeroid')
hashtag = cl.hashtag_info('dhbastards')

cl.video_upload_to_story(
    media_path,
    "Credits @subzeroid",
    mentions=[StoryMention(user=subzeroid, x=0.49892962, y=0.703125, width=0.8333333333333334, height=0.125)],
    links=[StoryLink(webUri='https://github.com/subzeroid/instagrapi')],
    hashtags=[StoryHashtag(hashtag=hashtag, x=0.23, y=0.32, width=0.5, height=0.22)],
    medias=[StoryMedia(media_pk=media_pk, x=0.5, y=0.5, width=0.6, height=0.8)]
)
```
</details>

## Documentation

* [Index](https://subzeroid.github.io/instagrapi/)
* [Getting Started](https://subzeroid.github.io/instagrapi/getting-started.html)
* [Usage Guide](https://subzeroid.github.io/instagrapi/usage-guide/fundamentals.html)
* [Interactions](https://subzeroid.github.io/instagrapi/usage-guide/interactions.html)
  * [`Media`](https://subzeroid.github.io/instagrapi/usage-guide/media.html) - Publication (also called post): Photo, Video, Album, IGTV and Reels
  * [`Resource`](https://subzeroid.github.io/instagrapi/usage-guide/media.html) - Part of Media (for albums)
  * [`MediaOembed`](https://subzeroid.github.io/instagrapi/usage-guide/media.html) - Short version of Media
  * [`Account`](https://subzeroid.github.io/instagrapi/usage-guide/account.html) - Full private info for your account (e.g. email, phone_number)
  * [`TOTP`](https://subzeroid.github.io/instagrapi/usage-guide/totp.html) - 2FA TOTP helpers (generate seed, enable/disable TOTP, generate code as Google Authenticator)
  * [`User`](https://subzeroid.github.io/instagrapi/usage-guide/user.html) - Full public user data
  * [`UserShort`](https://subzeroid.github.io/instagrapi/usage-guide/user.html) - Short public user data (used in Usertag, Comment, Media, Direct Message)
  * [`Usertag`](https://subzeroid.github.io/instagrapi/usage-guide/user.html) - Tag user in Media (coordinates + UserShort)
  * [`Location`](https://subzeroid.github.io/instagrapi/usage-guide/location.html) - GEO location (GEO coordinates, name, address)
  * [`Hashtag`](https://subzeroid.github.io/instagrapi/usage-guide/hashtag.html) - Hashtag object (id, name, picture)
  * [`Collection`](https://subzeroid.github.io/instagrapi/usage-guide/collection.html) - Collection of medias (name, picture and list of medias)
  * [`Comment`](https://subzeroid.github.io/instagrapi/usage-guide/comment.html) - Comments to Media
  * [`Highlight`](https://subzeroid.github.io/instagrapi/usage-guide/highlight.html) - Highlights
  * [`Notes`](https://subzeroid.github.io/instagrapi/usage-guide/notes.html) - Notes
  * [`Story`](https://subzeroid.github.io/instagrapi/usage-guide/story.html) - Story
  * [`StoryLink`](https://subzeroid.github.io/instagrapi/usage-guide/story.html) - Link Sticker
  * [`StoryLocation`](https://subzeroid.github.io/instagrapi/usage-guide/story.html) - Tag Location in Story (as sticker)
  * [`StoryMention`](https://subzeroid.github.io/instagrapi/usage-guide/story.html) - Mention users in Story (user, coordinates and dimensions)
  * [`StoryHashtag`](https://subzeroid.github.io/instagrapi/usage-guide/story.html) - Hashtag for story (as sticker)
  * [`StorySticker`](https://subzeroid.github.io/instagrapi/usage-guide/story.html) - Tag sticker to story (for example from giphy)
  * [`StoryBuild`](https://subzeroid.github.io/instagrapi/usage-guide/story.html) - [StoryBuilder](/instagrapi/story.py) return path to photo/video and mention co-ordinates
  * [`DirectThread`](https://subzeroid.github.io/instagrapi/usage-guide/direct.html) - Thread (topic) with messages in Direct Message
  * [`DirectMessage`](https://subzeroid.github.io/instagrapi/usage-guide/direct.html) - Message in Direct Message
  * [`Insight`](https://subzeroid.github.io/instagrapi/usage-guide/insight.html) - Insights for a post
  * [`Track`](https://subzeroid.github.io/instagrapi/usage-guide/track.html) - Music track (for Reels/Clips)
* [Best Practices](https://subzeroid.github.io/instagrapi/usage-guide/best-practices.html)
* [Development Guide](https://subzeroid.github.io/instagrapi/development-guide.html)
* [Handle Exceptions](https://subzeroid.github.io/instagrapi/usage-guide/handle_exception.html)
* [Challenge Resolver](https://subzeroid.github.io/instagrapi/usage-guide/challenge_resolver.html)
* [Exceptions](https://subzeroid.github.io/instagrapi/exceptions.html)

## Contributing

[![List of contributors](https://opencollective.com/instagrapi/contributors.svg?width=890&button=0)](https://github.com/subzeroid/instagrapi/graphs/contributors)

To release, you need to call the following commands:

    python -m build
    twine upload dist/*



================================================
FILE: CODE_OF_CONDUCT.md
================================================
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
https://t.me/instagrapi.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.



================================================
FILE: CONTRIBUTING.md
================================================
# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change.

Please note we have a code of conduct, please follow it in all your interactions with the project.

## Pull Request Process

1. Ensure any install or build dependencies are removed before the end of the layer when doing a
   build.
2. Add or change [unittests](/tests.py) that are specific to functionality according to [Development Guide](https://subzeroid.github.io/instagrapi/development-guide.html)
3. Add documentation about your methods and changes to [docs](/docs)
4. Update the README.md with details of changes to the interface, this includes new environment
   variables, exposed ports, useful file locations and container parameters.
5. Increase the version number in [setup.py](/setup.py) and date of last reverse-engineering in the README.md to the new version that this
   Pull Request would represent. The versioning scheme we use is [SemVer](http://semver.org/).
6. You may merge the Pull Request in once you have the sign-off of two other developers, or if you
   do not have permission to do that, you may request the second reviewer to merge it for you.

## Code of Conduct

### Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of experience,
nationality, personal appearance, race, religion, or sexual identity and
orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

### Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at [INSERT EMAIL ADDRESS]. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

### Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at [http://contributor-covenant.org/version/1/4][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/



================================================
FILE: docker-compose.yml
================================================
version: "3.4"

x-mount-app-and-user-git-config: &mount-app-and-user-git-config
  volumes:
    - ./:/app
    - ~/.gitconfig:/home/instagrapi/.gitconfig # allow script to commit as user

services:

  # "devbox" to enable the developer to have a fully loaded development environment
  devbox: &devbox
    build:
      dockerfile: "./docker/devbox.dockerfile"
      context: "."
    tty: true
    volumes:
      - "./:/app"

  # "test" enables the developer to run all the tests and linting locally
  test:
    <<: *devbox
    command: "docker/run_tests.sh --format-code"

  tests:
    <<: *devbox
    command: "python -m unittest tests"

  lock-requirements:
    <<: *devbox
    entrypoint: "/bin/bash"
    command: "docker/lock_requirements.sh"

  # generate and serve the project documentation locally
  mkdocs: &mkdocs
    <<: *devbox
    entrypoint: "mkdocs"
    ports:
      - "8000:8000"
    command: [ "serve", "--dev-addr=0.0.0.0:8000" ]

  mike:
    <<: [*mkdocs, *mount-app-and-user-git-config]
    entrypoint: "mike"



================================================
FILE: LICENSE
================================================
MIT License

Copyright (c) 2023

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



================================================
FILE: mkdocs.yml
================================================
site_name: instagrapi Documentation
repo_url: https://github.com/subzeroid/instagrapi/
site_url: https://subzeroid.github.io/instagrapi/
repo_name: subzeroid/instagrapi
edit_uri: edit/main/docs/
docs_dir: docs
nav:
  - Overview: index.md
  - Getting Started: getting-started.md
  - Usage Guide:
    - Fundamentals: usage-guide/fundamentals.md
    - Interactions: usage-guide/interactions.md
    - Handle Exceptions: usage-guide/handle_exception.md
    - Collection: usage-guide/collection.md
    - Comment: usage-guide/comment.md
    - Direct: usage-guide/direct.md
    - Hashtag: usage-guide/hashtag.md
    - Insight: usage-guide/insight.md
    - Location: usage-guide/location.md
    - Media: usage-guide/media.md
    - Story: usage-guide/story.md
    - Track: usage-guide/track.md
    - User: usage-guide/user.md
    - Account: usage-guide/account.md
  - Best Practices: usage-guide/best-practices.md
  - Development Guide: development-guide.md
  - Exceptions: exceptions.md
theme: material
markdown_extensions:
  - markdown_include.include:
      base_path: docs
  - admonition
  - codehilite
  - footnotes
  - pymdownx.highlight
  - pymdownx.keys
  - pymdownx.superfences
plugins:
  - search
  - autorefs
  - mkdocstrings:
      handlers:
        python:
          selection:
            docstring_style: "sphinx"
          rendering:
            heading_level: 3
            show_root_heading: True
            show_source: False
            show_root_full_path: False
extra:
  version:
    provider: mike
extra_css:
  - css/mkdocstrings.css



================================================
FILE: pyproject.toml
================================================
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "instagrapi"
version = "2.2.1"
authors = [
    {name = "Mark Subzeroid", email = "143403577+subzeroid@users.noreply.github.com"}
]
description = "Fast and effective Instagram Private API wrapper"
readme = {content-type = "text/markdown", text = """
Fast and effective Instagram Private API wrapper (public+private requests and challenge resolver).

Use the most recent version of the API from Instagram.

Features:

1. Performs Public API (web, anonymous) or Private API (mobile app, authorized)
   requests depending on the situation (to avoid Instagram limits)
2. Challenge Resolver have Email (as well as recipes for automating receive a code from email) and SMS handlers
3. Support upload a Photo, Video, IGTV, Clips (Reels), Albums and Stories
4. Support work with User, Media, Insights, Collections, Location (Place), Hashtag and Direct objects
5. Like, Follow, Edit account (Bio) and much more else
6. Insights by account, posts and stories
7. Build stories with custom background, font animation, swipe up link and mention users
8. In the next release, account registration and captcha passing will appear
"""}
license = {text = "MIT"}
requires-python = ">=3.9"
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
]
keywords = [
    "instagram private api",
    "instagram-private-api",
    "instagram api",
    "instagram-api",
    "instagram",
    "instagram-scraper",
    "instagram-client",
    "instagram-stories",
    "instagram-feed",
    "instagram-reels",
    "instagram-insights",
    "downloader",
    "uploader",
    "videos",
    "photos",
    "albums",
    "igtv",
    "reels",
    "stories",
    "pictures",
    "instagram-user-photos",
    "instagram-photos",
    "instagram-metadata",
    "instagram-downloader",
    "instagram-uploader",
    "instagram-note",
]
dependencies = [
    "requests==2.32.4",
    "PySocks==1.7.1",
    "pydantic==2.11.7",
    "moviepy==1.0.3",
    "pycryptodomex==3.23.0",
]

[project.urls]
Homepage = "https://github.com/subzeroid/instagrapi"
Repository = "https://github.com/subzeroid/instagrapi"

[project.optional-dependencies]
test = [
    "flake8==7.3.0",
    "Pillow==11.3.0",
    "isort==6.0.1",
    "bandit==1.8.6",
    "mike==2.1.3",
    "markdown-include==0.8.1",
    "mkdocs-material==9.6.17",
    "mkdocs-minify-html-plugin>=0.3.1",
    "mkdocstrings==0.30.0",
    "pytest-xdist==3.8.0",
    "pytest~=8.4.0",
]

[tool.setuptools]
include-package-data = true

[tool.setuptools.packages.find]
where = ["."]
include = ["instagrapi*"]



================================================
FILE: requirements-docs.txt
================================================
mike==2.0.0

# mike implicitly depends on pkg_resources from setuptools.
# It has been addressed as part of the work towards 2.0, but that has not been released yet
# https://github.com/jimporter/mike/issues/148
setuptools==68.2.2

markdown-include==0.8.1
mkdocs==1.6.1
mkdocs-material==9.6.17
mkdocs-minify-plugin==0.8.0
mkdocs-redirects==1.2.2
mkdocstrings[python]==0.30.0
mkdocs-autorefs>=1.0.0



================================================
FILE: requirements-test.txt
================================================
flake8==7.3.0
Pillow==11.3.0
isort==6.0.1
bandit==1.8.6
pytest-xdist==3.8.0
pytest~=8.4.1



================================================
FILE: requirements.lock
================================================
# THIS IS AN AUTOGENERATED LOCKFILE. DO NOT EDIT MANUALLY.
annotated-types==0.7.0
certifi==2025.6.15
charset-normalizer==3.4.2
decorator==4.4.2
idna==3.10
imageio==2.37.0
imageio-ffmpeg==0.6.0
moviepy==1.0.3
numpy==2.3.1
pillow==11.2.1
pip==25.1.1
proglog==0.1.12
pycryptodomex==3.23.0
pydantic==2.11.7
pydantic_core==2.33.2
PySocks==1.7.1
requests==2.32.4
tqdm==4.67.1
typing-inspection==0.4.1
typing_extensions==4.14.0
urllib3==2.5.0



================================================
FILE: requirements.txt
================================================
requests==2.32.4
PySocks==1.7.1
pydantic==2.11.7
moviepy==1.0.3
pycryptodomex==3.23.0



================================================
FILE: SECURITY.md
================================================
# Security Policy

## Supported Versions

Only the latest versions are supported

| Version    | Supported          |
| ---------- | ------------------ |
| 1.12.x     | :white_check_mark: |
| < 1.12.0   | :x:                |

## Reporting a Vulnerability

Report vulnerabilities in the telegram channel https://t.me/instagrapi or https://github.com/subzeroid/instagrapi/issues



================================================
FILE: .bandit
================================================
[bandit]
exclude: *venv*,*env*,*scratch*
skips: B101,B311,B303,B306


================================================
FILE: .dockerignore
================================================
.github/
.git/
venv/


================================================
FILE: .flake8
================================================
[flake8]
ignore = W503
max-line-length = 120
exclude = */tests/*,*test*.py,*/migrations/*



================================================
FILE: .isort.cfg
================================================
[settings]
profile=black
atomic=true


================================================
FILE: .pre-commit-config.yaml
================================================
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.3.0
    hooks:
    -   id: check-yaml
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
-   repo: https://github.com/psf/black
    rev: 22.8.0
    hooks:
    -   id: black
-   repo: https://github.com/pycqa/flake8
    rev: 5.0.4
    hooks:
    -   id: flake8



================================================
FILE: docker/devbox.dockerfile
================================================
FROM python:3.13.6-bookworm

ARG _USER="instagrapi"
ARG _UID="1001"
ARG _GID="100"
ARG _SHELL="/bin/bash"

RUN useradd -m -s "${_SHELL}" -N -u "${_UID}" "${_USER}"

ENV USER ${_USER}
ENV UID ${_UID}
ENV GID ${_GID}
ENV HOME /home/${_USER}
ENV PATH "${HOME}/.local/bin/:${PATH}"
ENV PIP_NO_CACHE_DIR "true"

RUN mkdir /app && chown ${UID}:${GID} /app

USER ${_USER}

COPY --chown=${UID}:${GID} ./requirements* /app/
WORKDIR /app

RUN pip install -r requirements.txt -r requirements-test.txt -r requirements-docs.txt

CMD bash



================================================
FILE: docker/lock_requirements.sh
================================================
#!/usr/bin/env bash

pip uninstall -y -r <(pip freeze)
pip install -r requirements.txt
printf "# THIS IS AN AUTOGENERATED LOCKFILE. DO NOT EDIT MANUALLY.\n" > requirements.lock
pip freeze --disable-pip-version-check --all >> requirements.lock

echo "Rebuild containers to verify there are no conflicts."



================================================
FILE: docker/run_tests.sh
================================================
#!/usr/bin/env bash

set -eo pipefail

BLACK_ACTION="--check"
ISORT_ACTION="--check-only"

function usage
{
    echo "usage: run_tests.sh [--format-code]"
    echo ""
    echo " --format-code : Format the code instead of checking formatting."
    exit 1
}

while [[ $# -gt 0 ]]; do
    arg="$1"
    case $arg in
        --format-code)
        BLACK_ACTION="--quiet"
        ISORT_ACTION=""
        ;;
        -h|--help)
        usage
        ;;
        "")
        # ignore
        ;;
        *)
        echo "Unexpected argument: ${arg}"
        usage
        ;;
    esac
    shift
done

python -m unittest tests.FakeClientTestCase tests.ClientPublicTestCase

echo "Running isort..."
isort ${ISORT_ACTION} instagrapi

echo "Running flake8..."
flake8 instagrapi --count --exit-zero --statistics



================================================
FILE: docs/_config.yml
================================================
theme: jekyll-theme-hacker


================================================
FILE: docs/development-guide.md
================================================
# Development Guide

Welcome! Thank you for wanting to make the project better. This section provides an overview on how repository structure
and how to work with the code base.

Before you dive into this, it is best to read:

* The [Contributing guide](../CONTRIBUTING.md.md)

## Docker

The `instagrapi` project uses Docker to ease setting up a consistent development environment. The Docker documentation has
details on how to [install docker][install-docker] on your computer.

Once that is configured, the test suite can be run locally:

```bash
docker-compose run --rm test
```

If you want to be able to execute code in the container:

```bash
docker-compose run --rm devbox
(your code here)
```

In the devbox environment you'll be able to enter a python shell and import `instagrapi` or any dependencies.

## Debugging

The docker container has [pdb++][pdbpp-home] install that can be used as a debugger. (However, you are welcome to set up
a different debugger if you would like.)

This allows you to easily create a breakpoint anywhere in the code.

```python
def my_function():
    breakpoint()
    ...
```

When your the code, you will drop into an interactive `pdb++` debugger.

See the documentation on [pdb][pdb-docs] and [pdb++][pdbpp-docs] for more information.

## Testing

You'll be unable to merge code unless the linting and tests pass. You can run these in your container via:

```bash
docker-compose run --rm test
```

This will run the same tests, linting, and code coverage that are run by the CI pipeline. The only difference is that,
when run locally, `black` and `isort` are configured to automatically correct issues they detect.

Generally we should endeavor to write tests for every feature. Every new feature branch should increase the test
coverage rather than decreasing it.

We use [pytest][pytest-docs] as our testing framework.

#### Stages

To customize / override a specific testing stage, please read the documentation specific to that tool:

1. [PyTest][pytest-docs]
2. [MyPy][mypy-docs]
3. [Isort][isort-docs]
4. [Flake8][flake8-docs]
5. [Bandit][bandit-docs]

### `setup.py`

Setuptools is used to packaging the library.

**`setup.py` must not import anything from the package** When installing from source, the user may not have the
packages dependencies installed, and importing the package is likely to raise an `ImportError`. For this reason, the
**package version should be obtained without importing**. This is explains why `setup.py` uses a regular expression to
grabs the version from `__init__.py` without actually importing.

### Requirements

* **requirements.txt** - Lists all direct dependencies (packages imported by the library).
* **requirements-test.txt** - Lists all direct requirements needed to run the test suite & lints.

This will trigger the CI system to build a wheel and a source distributions of the package and push them to
[PyPI][pypi].

## Continuous Integration Pipeline

TODO: Add CI documentation.

[install-docker]: https://docs.docker.com/install/
[pdbpp-home]: https://github.com/pdbpp/pdbpp
[pdb-docs]: https://docs.python.org/3/library/pdb.html
[pdbpp-docs]: https://github.com/pdbpp/pdbpp#usage
[pytest-docs]: https://docs.pytest.org/en/latest/
[mypy-docs]: https://mypy.readthedocs.io/en/stable/
[isort-docs]: https://pycqa.github.io/isort/
[flake8-docs]: http://flake8.pycqa.org/en/stable/
[bandit-docs]: https://bandit.readthedocs.io/en/stable/
[sem-ver]: https://semver.org/
[pypi]: https://pypi.org/project/gbq/


================================================
FILE: docs/exceptions.md
================================================
## Common Exceptions

| Exception                 | Base        | Description
| ------------------------- | ----------- |-------------------------------------
| ClientError               | Exception   | Base Exception for Instagram calls
| GenericRequestError       | ClientError | Base Exception for Request (Solution: try changing your proxy)
| ClientGraphqlError        | ClientError | Exception for GraphQL calls
| ClientJSONDecodeError     | ClientError | JSON Exception
| ClientConnectionError     | ClientError | Connection error (Solution: try changing your proxy)
| ClientBadRequestError     | ClientError | HTTP 400 Exception
| ClientUnauthorizedError   | ClientError | HTTP 401 Exception
| ClientForbiddenError      | ClientError | HTTP 403 Exception
| ClientNotFoundError       | ClientError | HTTP 404 Exception
| ClientThrottledError      | ClientError | HTTP 429 Exception (Solution: try changing your proxy)
| ClientRequestTimeout      | ClientError | Request Timeout Exception
| ClientIncompleteReadError | ClientError | Raises when response interrupted
| ClientLoginRequired       | ClientError | Raises when Instagram required Login (Solution: try changing your proxy)
| ReloginAttemptExceeded    | ClientError | Raises when all attempts exceeded
| ClientErrorWithTitle      | ClientError | Occurs when Instagram returns an unknown error with the title
| ClientUnknownError        | ClientError | Occurs when Instagram returns an unknown error
| WrongCursorError          | ClientError | Occurs when the cursor for pagination is passed in the wrong format
| ClientStatusFail          | ClientError | Occurs when Instagram returns message with status=fail with details

## Proxy Exceptions

| Exception                 | Base         | Description
| ------------------------- | ------------ |-------------------------------------
| ProxyError                | ClientError  | Base exception for proxy
| ConnectProxyError         | ProxyError   | Occurs when it is not possible to connect to your proxy
| AuthRequiredProxyError    | ProxyError   | Occurs when incorrect credentials are passed to authorize your proxy
| ProxyAddressIsBlocked     | PrivateError | Happens when your proxy is blocked by Instagram, change your proxy!
| SentryBlock               | PrivateError | Raises when get message=sentry_block (most likely you were banned from instagram by ip address. Solution: try changing your proxy)
| RateLimitError            | PrivateError | Raises when get message=rate_limit_error (Solution: try changing your proxy)
| PleaseWaitFewMinutes     | PrivateError | Raises when get message="Please wait a few minutes before you try again" (Solution: try changing your proxy)

## GraphQL/Public Exceptions

| Exception                 | Base         | Description
| ------------------------- | ------------ |-------------------------------------
| AccountSuspended          | ClientError  | Your account is suspended
| TermsUnblock              | ClientError  | Your account may be blocked, you need to agree to the terms
| TermsAccept               | ClientError  | Your account may be blocked, you need to agree to the terms
| AboutUsError              | ClientError  | Your account may be blocked

## Private Exceptions

| Exception                | Base         | Description
| ------------------------ | ------------ |-----------------------------------------------------------
| PrivateError             | ClientError  | Base Exception for Private calls (received from Instagram)
| FeedbackRequired         | PrivateError | Raises when get message=feedback_required
| PreLoginRequired         | ClientError | Raises when authorization is required before calling a method
| LoginRequired            | PrivateError | Raises when get message=login_required (from Instagram)
| BadPassword              | PrivateError | Raises when get message=bad_password
| TwoFactorRequired        | PrivateError | Raises when get message=two_factor_required
| UnknownError             | PrivateError | Raises when get unknown message (new message from instagram)
| BadCredentials           | PrivateError | The login and password pair for your account have not been passed
| IsRegulatedC18Error      | ClientBadRequestError | The user is limited to 18+

## Challenge Exceptions

| Exception                      | Base           | Description                                                 |
| ------------------------------ | -------------- |------------------------------------------------------------ |
| ChallengeError                 | PrivateError   | Base Challenge Exception (received from Instagram)
| ChallengeRedirection           | ChallengeError | Raises when get type=CHALLENGE_REDIRECTION
| ChallengeRequired              | ChallengeError | Raises when get message=challenge_required
| ChallengeSelfieCaptcha         | ChallengeError | Raises when get step=selfie_captcha
| ChallengeUnknownStep           | ChallengeError | Occurs when challenge is unknown
| SelectContactPointRecoveryForm | ChallengeError | Raises when get challengeType=SelectContactPointRecoveryForm
| RecaptchaChallengeForm         | ChallengeError | Raises when get challengeType=RecaptchaChallengeForm
| SubmitPhoneNumberForm          | ChallengeError | Raises when get challengeType=SubmitPhoneNumberForm
| LegacyForceSetNewPasswordForm  | ChallengeError | Raises when get challengeType=LegacyForceSetNewPasswordForm
| ConsentRequired                | PrivateError   | Raises when get message=consent_required
| GeoBlockRequired               | PrivateError   | Raises when get message=geoblock_required
| CheckpointRequired             | PrivateError   | Raises when get message=checkpoint_required

## Media Exceptions

| Exception                | Base         | Description                                    |
| ------------------------ | ------------ |----------------------------------------------- |
| MediaError               | PrivateError | Base Media Exception (received from Instagram)
| MediaNotFound            | MediaError   | Raises when user unavailable
| InvalidTargetUser        | PrivateError | Occurs when the selected user cannot be mentioned (does not exist, has been deleted or is closed by privacy settings)
| InvalidMediaId           | PrivateError | Occurs when the selected media does not exists
| MediaUnavailable         | PrivateError | Occurs when the selected media is no longer available

## User Exceptions

| Exception                | Base          | Description                                   |
| ------------------------ | ------------- |---------------------------------------------- |
| UserError                | PrivateError  | Base User Exception (received from Instagram)
| UserNotFound             | UserError     | Raises when user unavailable
| PrivateAccount           | PrivateError  | The target user is closed by privacy settings

## Account Exceptions

| Exception                | Base             | Description                                   |
| ------------------------ | ---------------- |---------------------------------------------- |
| ResetPasswordError       | ClientError      | Raises when password is not reset
| UnsupportedError         | ClientError      | Raises when option is supported
| UnsupportedSettingValue  | UnsupportedError | Raises when account setting value is not supported

## Collection Exceptions

| Exception                | Base            | Description                                         |
| ------------------------ | --------------- |---------------------------------------------------- |
| CollectionError          | PrivateError    | Base Collection Exception (received from Instagram)
| CollectionNotFound       | CollectionError | Raises when collection unavailable

## Direct Exceptions

| Exception                | Base           | Description                                    |
| ------------------------ | -------------- |----------------------------------------------- |
| DirectError              | PrivateError   | Base Direct Exception
| DirectThreadNotFound     | DirectError    | Raises when thread not found
| DirectMessageNotFound    | DirectError    | Raises when message in thread not found

## Photo Exceptions

| Exception                | Base                | Description                                    |
| ------------------------ | ------------------- |----------------------------------------------- |
| PhotoNotDownload         | PrivateError        | Raises when source photo not found
| PhotoNotUpload           | PrivateError        | Raises when photo not upload
| PhotoConfigureError      | PhotoNotUpload      | Raises when photo not configured
| PhotoConfigureStoryError | PhotoConfigureError | Raises when photo story not configured

## Video Exceptions

| Exception                | Base                | Description                                    |
| ------------------------ | ------------------- | ---------------------------------------------- |
| VideoNotDownload         | PrivateError        | Raises when source video not found
| VideoNotUpload           | PrivateError        | Raises when video not upload
| VideoConfigureError      | VideoNotUpload      | Raises when video not configured
| VideoConfigureStoryError | VideoConfigureError | Raises when video story not configured
| VideoTooLongException    | PrivateError        | Raises when video too long

## IGTV Exceptions

| Exception                | Base          | Description                                    |
| ------------------------ | ------------- |----------------------------------------------- |
| IGTVNotUpload            | PrivateError  | Raises when IGTV not upload
| IGTVConfigureError       | IGTVNotUpload | Raises when IGTV not configured

## Reels/Clip Exceptions

| Exception                | Base          | Description                                    |
| ------------------------ | ------------- |----------------------------------------------- |
| ClipNotUpload            | PrivateError  | Raises when Reels Clip not upload
| ClipConfigureError       | ClipNotUpload | Raises when Reels Clip not configured

## Album Exceptions

| Exception                | Base         | Description                                    |
| ------------------------ | ------------ |----------------------------------------------- |
| AlbumNotDownload         | PrivateError | Raises when album not found
| AlbumUnknownFormat       | PrivateError | Raises when format of media not MP4 or JPG
| AlbumConfigureError      | PrivateError | Raises when album not configured

## Story Exceptions

| Exception                | Base          | Description                                    |
| ------------------------ | ------------- |----------------------------------------------- |
| StoryNotFound            | NotFoundError | Raises when story not found

## Highlight Exceptions

| Exception                | Base          | Description                                   |
| ------------------------ | ------------- |---------------------------------------------- |
| HighlightNotFound        | NotFoundError | Raises when highlight not found

## Hashtag Exceptions

| Exception                | Base                 | Description                            |
| ------------------------ | -------------------- |--------------------------------------- |
| HashtagError             | PrivateError         | Base exception for hashtag
| HashtagNotFound          | NotFoundError        | Raises when hashtag not found
| HashtagPageWarning       | ClientForbiddenError | Occurs when Instagram returns warning_message with category_name=HASHTAG_PAGE_WARNING_MESSAGE

## Location Exceptions

| Exception                | Base          | Description                                    |
| ------------------------ | ------------- |----------------------------------------------- |
| LocationError            | PrivateError  | Base exception for location
| LocationNotFound         | NotFoundError | Raises when location not found

## Comment Exceptions

| Exception                | Base         | Description                                    |
| ------------------------ | ------------ |----------------------------------------------- |
| CommentNotFound          | PrivateError | Raises when comment not found
| CommentsDisabled         | PrivateError | The ability to comment has been disabled by the author of the post

## Share Exceptions

| Exception                 | Base         | Description
| ------------------------- | ------------ |-------------------------------------
| ShareDecodeError          | PrivateError | Occurs when the data format for Share-obj is incorrect

## Note Exceptions

| Exception                | Base          | Description                                    |
| ------------------------ | ------------- |----------------------------------------------- |
| NoteNotFound             | NotFoundError | Raises when note not found

## Track Exceptions

| Exception                | Base          | Description                                    |
| ------------------------ | ------------- |----------------------------------------------- |
| TrackNotFound            | NotFoundError | Raises when track not found



================================================
FILE: docs/getting-started.md
================================================
# Getting Started

## Installation

To install `instagrapi`, simply run this simple command in your terminal of choice:

```bash
python -m pip install instagrapi
```

## Introduction

`instagrapi` is a fast and effective Instagram Private API wrapper (public+private requests and challenge resolver). Use the most recent version of the API from Instagram, which was obtained using [reverse-engineering with Charles Proxy](https://github.com/subzeroid/instagrapi/discussions/1182) and [Proxyman](https://proxyman.io/).

## What's Next?

* [Usage Guide](usage-guide/fundamentals.md)
* [Interactions](usage-guide/interactions.md)
* [Handle Exceptions](usage-guide/handle_exception.md)
* [Challenge Resolver](usage-guide/challenge_resolver.md)
* [Exceptions](exceptions.md)

[docs-main]: index.md



================================================
FILE: docs/index.md
================================================
# instagrapi

### We recommend using our services:

* [LamaTok](https://lamatok.com/p/B9ScEYIQ) for TikTok API 🔥
* [HikerAPI](https://hikerapi.com/p/bkXQlaVe) for Instagram API ⚡⚡⚡
* [DataLikers](https://datalikers.com/p/S9Lv5vBy) for Instagram Datasets 🚀

[![Package](https://github.com/subzeroid/instagrapi/actions/workflows/python-package.yml/badge.svg?branch=master)](https://github.com/subzeroid/instagrapi/actions/workflows/python-package.yml)
[![PyPI](https://img.shields.io/pypi/v/instagrapi)][pypi]
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/instagrapi)][pypi]

Fast and effective Instagram Private API wrapper (public+private requests and challenge resolver). Use the most recent version of the API from Instagram, which was obtained using [reverse-engineering with Charles Proxy](https://github.com/subzeroid/instagrapi/discussions/1182) and [Proxyman](https://proxyman.io/).

*Instagram API valid for **16 Dec 2023** (last reverse-engineering check)*

Support **Python >= 3.9**

For any other languages (e.g. C++, C#, F#, D, [Golang](https://github.com/subzeroid/instagrapi-rest/tree/main/golang), Erlang, Elixir, Nim, Haskell, Lisp, Closure, Julia, R, Java, Kotlin, Scala, OCaml, JavaScript, Crystal, Ruby, Rust, [Swift](https://github.com/subzeroid/instagrapi-rest/tree/main/swift), Objective-C, Visual Basic, .NET, Pascal, Perl, Lua, PHP and others), I suggest using [instagrapi-rest](https://github.com/subzeroid/instagrapi-rest)

[Support Chat in Telegram](https://t.me/instagrapi)
![](https://gist.githubusercontent.com/m8rge/4c2b36369c9f936c02ee883ca8ec89f1/raw/c03fd44ee2b63d7a2a195ff44e9bb071e87b4a40/telegram-single-path-24px.svg) and [GitHub Discussions](https://github.com/subzeroid/instagrapi/discussions)

## Features

1. Performs [Public API](https://subzeroid.github.io/instagrapi/usage-guide/fundamentals.html) (web, anonymous) or [Private API](https://subzeroid.github.io/instagrapi/usage-guide/fundamentals.html) (mobile app, authorized) requests depending on the situation (to avoid Instagram limits)
2. [Login](https://subzeroid.github.io/instagrapi/usage-guide/interactions.html) by username and password, including 2FA and by sessionid
3. [Challenge Resolver](https://subzeroid.github.io/instagrapi/usage-guide/challenge_resolver.html) have Email and SMS handlers
4. Support [upload](https://subzeroid.github.io/instagrapi/usage-guide/media.html) a Photo, Video, IGTV, Reels, Albums and Stories
5. Support work with [User](https://subzeroid.github.io/instagrapi/usage-guide/user.html), [Media](https://subzeroid.github.io/instagrapi/usage-guide/media.html), [Comment](https://subzeroid.github.io/instagrapi/usage-guide/comment.html), [Insights](https://subzeroid.github.io/instagrapi/usage-guide/insight.html), [Collections](https://subzeroid.github.io/instagrapi/usage-guide/collection.html), [Location](https://subzeroid.github.io/instagrapi/usage-guide/location.html) (Place), [Hashtag](https://subzeroid.github.io/instagrapi/usage-guide/hashtag.html) and [Direct Message](https://subzeroid.github.io/instagrapi/usage-guide/direct.html) objects
6. [Like](https://subzeroid.github.io/instagrapi/usage-guide/media.html), [Follow](https://subzeroid.github.io/instagrapi/usage-guide/user.html), [Edit account](https://subzeroid.github.io/instagrapi/usage-guide/account.html) (Bio) and much more else
7. [Insights](https://subzeroid.github.io/instagrapi/usage-guide/insight.html) by account, posts and stories
8. [Build stories](https://subzeroid.github.io/instagrapi/usage-guide/story.html) with custom background, font animation, swipe up link and mention users
9. In the next release, account registration and captcha passing will appear

## Example

### Basic Usage

``` python
from instagrapi import Client

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

user_id = cl.user_id_from_username("example")
medias = cl.user_medias(user_id, 20)
```

#### The full example

``` python
from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag

cl = Client()
cl.login(USERNAME, PASSWORD, verification_code="<2FA CODE HERE>")

media_pk = cl.media_pk_from_url('https://www.instagram.com/p/CGgDsi7JQdS/')
media_path = cl.video_download(media_pk)
example = cl.user_info_by_username('example')
hashtag = cl.hashtag_info('dhbastards')

cl.video_upload_to_story(
    media_path,
    "Credits @example",
    mentions=[StoryMention(user=example, x=0.49892962, y=0.703125, width=0.8333333333333334, height=0.125)],
    links=[StoryLink(webUri='https://github.com/subzeroid/instagrapi')],
    hashtags=[StoryHashtag(hashtag=hashtag, x=0.23, y=0.32, width=0.5, height=0.22)],
    medias=[StoryMedia(media_pk=media_pk, x=0.5, y=0.5, width=0.6, height=0.8)]
)
```

### Requests

* `Public` (anonymous request via web api) methods have a suffix `_gql` (Instagram `GraphQL`) or `_a1` (example `https://www.instagram.com/example/?__a=1`)
* `Private` (authorized request via mobile api) methods have `_v1` suffix

The first request to fetch media/user is `public` (anonymous), if instagram raise exception, then use `private` (authorized).
Example (pseudo-code):

``` python
def media_info(media_pk):
    try:
        return self.media_info_gql(media_pk)
    except ClientError as e:
        # Restricted Video: This video is not available in your country.
        # Or media from private account
        return self.media_info_v1(media_pk)
```

## Detailed Documentation

To learn more about the various ways `instagrapi` can be used, read the [Usage Guide](usage-guide/fundamentals.md) page.

* [Getting Started](getting-started.md)
* [Usage Guide](usage-guide/fundamentals.md)
* [Interactions](usage-guide/interactions.md)
  * [`Media`](usage-guide/media.md) - Publication (also called post): Photo, Video, Album, IGTV and Reels
  * [`Resource`](usage-guide/media.md) - Part of Media (for albums)
  * [`MediaOembed`](usage-guide/media.md) - Short version of Media
  * [`Account`](usage-guide/account.md) - Full private info for your account (e.g. email, phone_number)
  * [`TOTP`](usage-guide/totp.md) - 2FA TOTP helpers (generate seed, enable/disable TOTP, generate code as Google Authenticator)
  * [`User`](usage-guide/user.md) - Full public user data
  * [`UserShort`](usage-guide/user.md) - Short public user data (used in Usertag, Comment, Media, Direct Message)
  * [`Usertag`](usage-guide/user.md) - Tag user in Media (coordinates + UserShort)
  * [`Location`](usage-guide/location.md) - GEO location (GEO coordinates, name, address)
  * [`Hashtag`](usage-guide/hashtag.md) - Hashtag object (id, name, picture)
  * [`Collection`](usage-guide/collection.md) - Collection of medias (name, picture and list of medias)
  * [`Comment`](usage-guide/comment.md) - Comments to Media
  * [`Highlight`](usage-guide/highlight.md) - Highlights
  * ['Notes'](usage-guide/notes.md) - Notes
  * [`Story`](usage-guide/story.md) - Story
  * [`StoryLink`](usage-guide/story.md) - Link (Swipe up)
  * [`StoryLocation`](usage-guide/story.md) - Tag Location in Story (as sticker)
  * [`StoryMention`](usage-guide/story.md) - Mention users in Story (user, coordinates and dimensions)
  * [`StoryHashtag`](usage-guide/story.md) - Hashtag for story (as sticker)
  * [`StorySticker`](usage-guide/story.md) - Tag sticker to story (for example from giphy)
  * [`StoryBuild`](usage-guide/story.md) - [StoryBuilder](https://github.com/subzeroid/instagrapi/blob/master/instagrapi/story.py) return path to photo/video and mention co-ordinates
  * [`DirectThread`](usage-guide/direct.md) - Thread (topic) with messages in Direct Message
  * [`DirectMessage`](usage-guide/direct.md) - Message in Direct Message
  * [`Insight`](usage-guide/insight.md) - Insights for a post
  * [`Track`](usage-guide/track.md) - Music track (for Reels/Clips)
* [Best Practices](usage-guide/best-practices.md)
* [Development Guide](development-guide.md)
* [Handle Exceptions](usage-guide/handle_exception.md)
* [Challenge Resolver](usage-guide/challenge_resolver.md)
* [Exceptions](exceptions.md)

[ci]: https://github.com/subzeroid/instagrapi/actions
[pypi]: https://pypi.org/project/instagrapi/



================================================
FILE: docs/css/mkdocstrings.css
================================================
/* Indentation. */
div.doc-contents:not(.first) {
  padding-left: 25px;
  border-left: 4px solid rgba(230, 230, 230);
  margin-bottom: 80px;
}

/* Don't capitalize names. */
h5.doc-heading {
  text-transform: none !important;
}

/* Don't use vertical space on hidden ToC entries. */
.hidden-toc::before {
  margin-top: 0 !important;
  padding-top: 0 !important;
}

/* Don't show permalink of hidden ToC entries. */
.hidden-toc a.headerlink {
  display: none;
}

/* Avoid breaking parameters name, etc. in table cells. */
td code {
  word-break: normal !important;
}

/* For pieces of Markdown rendered in table cells. */
td p {
  margin-top: 0 !important;
  margin-bottom: 0 !important;
}


================================================
FILE: docs/usage-guide/account.md
================================================
# Account

Viewing and managing your profile

| Method                                       | Return    | Description
| -------------------------------------------- | --------- | ----------------------------------------------------------
| account_info()                               | Account   | Get private info for your account (e.g. email, phone_number)
| account_edit(email: str, phone_number: str, username: str, full_name: str, biography: str, external_url: str) | Account | Change profile data
| account_change_picture(path: Path)           | UserShort | Change Profile picture
| send_confirm_email(email: str)               | dict      | Send confirmation code to new email address
| send_confirm_phone_number(phone_number: str) | dict      | Send confirmation code to new phone number

Example:

```python
>>> from instagrapi import Client
>>> cl = Client()
>>> cl.login(USERNAME, PASSWORD)
>>> cl.account_info().dict()
{'pk': 1903424587,
 'username': 'example',
 'full_name': 'Example Example',
 'is_private': False,
 'profile_pic_url': HttpUrl('https://instagram.frix7-1.fna.fbcdn.net/v/t51.2885-19/s150x150/200092102_504535360754500_904902738723095864_n.jpg?tp=1&_nc_ht=instagram.frix7-1.fna.fbcdn.net&_nc_ohc=T2ZT6yA6XzoAX9MvAQA&edm=AJlpnE4BAAAA&ccb=7-4&oh=3865b51bb33b365c9de8bcf9775e519c&oe=60E982F2&_nc_sid=312772'),
 'is_verified': False,
 'biography': 'Engineer: Python, JavaScript, Erlang, Go, Swift\n@dhbastards \n@bestskatetrick \n@asphalt_kings_lb \n@best_drift_daily \n@wrclive \n@surferyone \n@bmxtravel',
 'external_url': 'https://example.org/',
 'is_business': False,
 'birthday': '1984-01-01',
 'phone_number': '+79991234567',
 'gender': 1,
 'email': '...@gmail.com'}

>>> cl.account_edit(external_url='https://github.com/subzeroid/instagrapi')
Account(pk=1903424587, username='example', ..., external_url='https://github.com/subzeroid/instagrapi')

>>> media_pk = cl.media_pk_from_url('https://www.instagram.com/p/BWnh360Fitr/')
1560364774164147051

>>> profile_pic_path = cl.photo_download(media_pk, folder='/tmp')
PosixPath('/tmp/example_1560364774164147051.jpg')

>>> cl.account_change_picture(profile_pic_path)
UserShort(pk=1903424587, username='example', ...)

>>> cl.send_confirm_email("addr@example.com")
{
    'is_email_legit': False,
    'title': 'Email Already in Use',
    'body': 'The email address you entered is already used on your account. Enter a different one to update your contact info.',
    'error_type': 'email_unchanged',
    'status': 'ok'
}

>>> cl.send_confirm_phone_number("+5599999999")
{
    'action': 'sms_sent',
    'phone_verification_settings': {'max_sms_count': 2,
    'resend_sms_delay_sec': 60,
    'robocall_count_down_time_sec': 30,
    'robocall_after_max_sms': True},
    'status': 'ok'
}
```

Low level methods:

| Method                                         | Return    | Description
| ---------------------------------------------- | --------- | ----------------------------------------------------------
| news_inbox_v1(mark_as_seen: bool = False)      | dict      | Get "Active recently" as is (old and new stories)

Example:

```python
>>> cl.news_inbox_v1()
{'story_mentions': {'mentions_count_string': '0 stories mention you.',
  'reels': [],
  'product_stories_count': '0 stories mention your product.',
  'product_stories_reels': []},
 'counts': {'likes': 0,
  'activity_feed_dot_badge': 0,
  'relationships': 0,
  'new_posts': 0,
  'comments': 0,
  'comment_likes': 0,
  'shopping_notification': 0,
  'fundraiser': 0,
  'usertags': 0,
  'campaign_notification': 0,
  'photos_of_you': 0,
  'story_mentions': 0,
  'requests': 0},
 'last_checked': 1625468461.1633658,
 'friend_request_stories': [],
 'new_stories': [{'story_type': 159,
   'type': 13,
   'args': {'rich_text': 'An unrecognized XiaoMi MI 5s just logged in near Moscow, Russia, RU',
    'destination': 'login_activity',
    'icon_url': 'https://i.instagram.com/static/images/activity/info-1.5.png/3385260677b8.png',
    'should_icon_apply_filter': True,
    'icon_should_apply_filter': True,
    'extra': {'lat': 55.7522, 'long': 37.6156},
    'actions': ['hide'],
    'timestamp': 1625475888.805998,
    'tuuid': '0ceff44c-dd70-11eb-8080-808080808080',
    'clicked': False},
   'counts': {},
   'pk': 'xjQlWRMfNO+f739i2qZ1zf8HJTo='}],
 'old_stories': [{'type': 3,
   'story_type': 101,
   'args': {'links': [{'start': 24,
      'end': 33,
  ...
}
```



================================================
FILE: docs/usage-guide/best-practices.md
================================================
# Best Practices

This is a best practices guide around using the Instagram API so that you don't get rate limited or banned.

## Use a Proxy

If you're getting errors like this

- "The username you entered doesn't appear to belong to an account. Please check your username and try again."

Or you notice that Instagram is sending you emails about a suspicious login attempt, you should consider using a proxy. You are getting rate limited by Instagram or they are suspicious of your location.

You should have an IP address that you use consistently per user when making API requests. This will be
less suspicious than using a different IP address every time you make a request.

From our experience, here are safe limits we've seen for various actions:
- using 10 accounts per IP address
- publishing 4-16 posts for each account
- publishing 24-48 stories

We recommend using the [SOAX](https://soax.com/?r=sEysufQI) proxy service. Here's an example of using it with `instagrapi`

``` python
from instagrapi import Client

cl = Client()
before_ip = cl._send_public_request("https://api.ipify.org/")
cl.set_proxy("http://<api_key>:wifi;ca;;;toronto@proxy.soax.com:9137")
after_ip = cl._send_public_request("https://api.ipify.org/")

print(f"Before: {before_ip}")
print(f"After: {after_ip}")
```

## Add Delays

It's recommended you try to mimic the behavior of a real user. This means you should add delays
between requests. The delays should be random and not too long.

The following is a good example of how to add delays between requests.

``` python
from instagrapi import Client

cl = Client()

# adds a random delay between 1 and 3 seconds after each request
cl.delay_range = [1, 3]
```


## Use Sessions

When using `.login()` you will login and create a new session with Instagram every time.
This is suspicious for Instagram.
For example, when you use your mobile device, you login to Instagram once
and then you can use it for a long time without logging in again. This is because Instagram stores
your session on your device and you can use it to login to Instagram without entering your username
and password again.

To mimic this behavior, you can use the `.login()` method once to create a session and then store that session using `.dump_settings()` and then load it again using `.load_settings()`.

The first time you run your script

``` python
from instagrapi import Client

cl = Client()
cl.login(USERNAME, PASSWORD)
cl.dump_settings("session.json")
```

And the next time

``` python
from instagrapi import Client

cl = Client()
cl.load_settings("session.json")
cl.login (USERNAME, PASSWORD) # this doesn't actually login using username/password but uses the session
cl.get_timeline_feed() # check session
```

You'll notice we do a call to `cl.get_timeline_feed()` to check if the session is valid. If it's not valid, you'll get an exception.

Putting this all together, we could write a login function like this

``` python
from instagrapi import Client
from instagrapi.exceptions import LoginRequired
import logging

logger = logging.getLogger()

def login_user():
    """
    Attempts to login to Instagram using either the provided session information
    or the provided username and password.
    """

    cl = Client()
    session = cl.load_settings("session.json")

    login_via_session = False
    login_via_pw = False

    if session:
        try:
            cl.set_settings(session)
            cl.login(USERNAME, PASSWORD)

            # check if session is valid
            try:
                cl.get_timeline_feed()
            except LoginRequired:
                logger.info("Session is invalid, need to login via username and password")

                old_session = cl.get_settings()

                # use the same device uuids across logins
                cl.set_settings({})
                cl.set_uuids(old_session["uuids"])

                cl.login(USERNAME, PASSWORD)
            login_via_session = True
        except Exception as e:
            logger.info("Couldn't login user using session information: %s" % e)

    if not login_via_session:
        try:
            logger.info("Attempting to login via username and password. username: %s" % USERNAME)
            if cl.login(USERNAME, PASSWORD):
                login_via_pw = True
        except Exception as e:
            logger.info("Couldn't login user using username and password: %s" % e)

    if not login_via_pw and not login_via_session:
        raise Exception("Couldn't login user with either password or session")
```



================================================
FILE: docs/usage-guide/challenge_resolver.md
================================================

## New password challenge

You can automatically change your password to solve the challenge from Instagram.

Declare `change_password_handler` which will return a new password.

``` python
def change_password_handler(username):
    # Simple way to generate a random string
    chars = list("abcdefghijklmnopqrstuvwxyz1234567890!&£@#")
    password = "".join(random.sample(chars, 8))
    return password

cl = Client()
cl.change_password_handler = change_password_handler
cl.login(IG_USERNAME, IG_PASSWORD)
```


## Code verification challenge

You can automatically process the codes sent to you to solve the challenge from Instagram.

You need to declare `challenge_code_handler` which will return the code received from Instagram via Email or SMS:

``` python
from instagrapi.mixins.challenge import ChallengeChoice


def challenge_code_handler(username, choice):
    if choice == ChallengeChoice.SMS:
        return get_code_from_sms(username)
    elif choice == ChallengeChoice.EMAIL:
        return get_code_from_email(username)
    return False

cl = Client()
cl.challenge_code_handler = challenge_code_handler
cl.login(IG_USERNAME, IG_PASSWORD)
```

For example, you can get the code through the IMAP of Gmail:

``` python
def get_code_from_email(username):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(CHALLENGE_EMAIL, CHALLENGE_PASSWORD)
    mail.select("inbox")
    result, data = mail.search(None, "(UNSEEN)")
    assert result == "OK", "Error1 during get_code_from_email: %s" % result
    ids = data.pop().split()
    for num in reversed(ids):
        mail.store(num, "+FLAGS", "\\Seen")  # mark as read
        result, data = mail.fetch(num, "(RFC822)")
        assert result == "OK", "Error2 during get_code_from_email: %s" % result
        msg = email.message_from_string(data[0][1].decode())
        payloads = msg.get_payload()
        if not isinstance(payloads, list):
            payloads = [msg]
        code = None
        for payload in payloads:
            body = payload.get_payload(decode=True).decode()
            if "<div" not in body:
                continue
            match = re.search(">([^>]*?({u})[^<]*?)<".format(u=username), body)
            if not match:
                continue
            print("Match from email:", match.group(1))
            match = re.search(r">(\d{6})<", body)
            if not match:
                print('Skip this email, "code" not found')
                continue
            code = match.group(1)
            if code:
                return code
    return False
```

All challenges solved in the module [challenge.py](https://github.com/subzeroid/instagrapi/blob/master/instagrapi/mixins/challenge.py)

Automatic submission code from SMS/Email in examples [here](https://github.com/subzeroid/instagrapi/blob/master/examples/challenge_resolvers.py)



================================================
FILE: docs/usage-guide/collection.md
================================================
# Collections

| Method                                                                          | Return             | Description                                      |
| ------------------------------------------------------------------------------- | ------------------ | ------------------------------------------------ |
| collections()                                                                   | List\[Collection]  | Get all account collections
| collection_pk_by_name(name: str)                                                | int                | Get collection_pk by name
| collection_medias_by_name(name: str)                                            | List\[Media]       | Get medias in collection by name
| collection_medias(collection_pk: int, amount: int = 21, last_media_pk: int = 0) | List\[Media]       | Get medias in collection by collection_id; Use **amount=0** to return all medias in collection; Use **last_media_pk** to return medias by cursor
| liked_medias(amount: int = 21, last_media_pk: int = 0)                          | List\[Media]       | Get media you have liked
| media_save(media_id: str, collection_pk: int = None)                            | bool               | Save media to collection
| media_unsave(media_id: str, collection_pk: int = None)                          | bool               | Unsave media from collection



================================================
FILE: docs/usage-guide/comment.md
================================================
# Comment

Post comment, viewing, like and unlike comments

| Method                                                                                  | Return             | Description
| --------------------------------------------------------------------------------------- | ------------------ | --------------------------
| media_comment(media_id: str, text: str, replied_to_comment_id: Optional[int] = None) | Comment            | Add new comment to media
| media_comments(media_id: str, amount: int = 0)                                          | List\[Comment]     | Get a list comments for media (amount=0 - all comments)
| media_comments_chunk(media_id: str, max_amount: int, min_id: str = None) | Tuple[List[Comment], str] | Get chunk of comments on a media and end_cursor
| comment_like(comment_pk: int)                                                           | bool               | Like a comment
| comment_unlike(comment_pk: int)                                                         | bool               | Unlike a comment
| comment_pin(media_id: str,comment_pk: int)                                              | bool               | Pin a comment
| comment_unpin(media_id: str,comment_pk: int)                                            | bool               | Unpin a comment
| comment_bulk_delete(media_id: str, comment_pks: List[int])                              | bool               | Delete a comment


Example:

``` python
>>> from instagrapi import Client

>>> cl = Client()
>>> cl.login(USERNAME, PASSWORD)

>>> media_id = cl.media_id(cl.media_pk_from_url('https://www.instagram.com/p/ByU3LAslgWY/'))

>>> comment = cl.media_comment(media_id, "Test comment")
>>> comment.dict()
{'pk': 17926777897585108,
 'text': 'Test comment',
 'user': {'pk': 1903424587,
  'username': 'example',
  'full_name': 'Example Example',
  'profile_pic_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t51.2885-19/s150x150/156689363_269505058076642_6448820957073669709_n.jpg?tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_ohc=EtzrL0pAdg8AX9pE_wN&edm=ABQSlwABAAAA&ccb=7-4&oh=e04d45b7651140e7fef61b1f67f1f408&oe=60C65AD1&_nc_sid=b2b2bd', scheme='https', host='scontent-hel3-1.cdninstagram.com', tld='com', host_type='domain', path='/v/t51.2885-19/s150x150/156689363_269505058076642_6448820957073669709_n.jpg', query='tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_ohc=EtzrL0pAdg8AX9pE_wN&edm=ABQSlwABAAAA&ccb=7-4&oh=e04d45b7651140e7fef61b1f67f1f408&oe=60C65AD1&_nc_sid=b2b2bd'),
  'stories': []},
 'created_at_utc': datetime.datetime(2021, 5, 15, 14, 50, 3, tzinfo=datetime.timezone.utc),
 'content_type': 'comment',
 'status': 'Active',
 'has_liked': None,
 'like_count': None}

>>> comment = cl.media_comment(media_id, "Test comment 2", replied_to_comment_id=comment.pk)
>>> comment.dict()
{'pk': 17926777897585109,
 'text': 'Test comment 2',
 'user': {'pk': 1903424587,
  'username': 'example',
  'full_name': 'Example Example',
  'profile_pic_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t51.2885-19/s150x150/156689363_269505058076642_6448820957073669709_n.jpg?tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_ohc=EtzrL0pAdg8AX9pE_wN&edm=ABQSlwABAAAA&ccb=7-4&oh=e04d45b7651140e7fef61b1f67f1f408&oe=60C65AD1&_nc_sid=b2b2bd', scheme='https', host='scontent-hel3-1.cdninstagram.com', tld='com', host_type='domain', path='/v/t51.2885-19/s150x150/156689363_269505058076642_6448820957073669709_n.jpg', query='tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_ohc=EtzrL0pAdg8AX9pE_wN&edm=ABQSlwABAAAA&ccb=7-4&oh=e04d45b7651140e7fef61b1f67f1f408&oe=60C65AD1&_nc_sid=b2b2bd'),
  'stories': []},
 'created_at_utc': datetime.datetime(2021, 5, 15, 14, 50, 3, tzinfo=datetime.timezone.utc),
 'content_type': 'comment',
 'status': 'Active',
 'has_liked': None,
 'like_count': None}

>>> comments = cl.media_comments(media_id)
>>> comments[0].dict()
 {'pk': 17926777897585108,
 'text': 'Test comment',
 'user': {'pk': 1903424587,
  'username': 'example',
  'full_name': 'Example Example',
  'profile_pic_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t51.2885-19/s150x150/156689363_269505058076642_6448820957073669709_n.jpg?tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_ohc=EtzrL0pAdg8AX9pE_wN&edm=AId3EpQBAAAA&ccb=7-4&oh=e3fbafcdb63cec3535004e85eb3397ae&oe=60C65AD1&_nc_sid=705020', scheme='https', host='scontent-hel3-1.cdninstagram.com', tld='com', host_type='domain', path='/v/t51.2885-19/s150x150/156689363_269505058076642_6448820957073669709_n.jpg', query='tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_ohc=EtzrL0pAdg8AX9pE_wN&edm=AId3EpQBAAAA&ccb=7-4&oh=e3fbafcdb63cec3535004e85eb3397ae&oe=60C65AD1&_nc_sid=705020'),
  'stories': []},
 'created_at_utc': datetime.datetime(2021, 5, 15, 14, 50, 3, tzinfo=datetime.timezone.utc),
 'content_type': 'comment',
 'status': 'Active',
 'has_liked': False,
 'like_count': 0}

>>> (comments_part1, next_min_id) = cl.media_comments_chunk(media_id, 100)
>>> next_min_id
QVFBQmZCa1dxaFB5eFpBY2luVFMwLWdmN2ZCcUV6OF9hQWlIQk12ZWZqUlctZ2pOa1J5YjJ6bFY5Q1doSGNuUmpxSS1DdXRvZ0NLemJrR1hXd2p0dS1JMg==
>>> (comments_part2, next_min_id) = cl.media_comments_chunk(media_id, 100, next_min_id)
>>> next_min_id
QVFEbHpIWmpFc3BNUkgzUFVuOGZOQlhDQ1hHeWlVWHlJSnBhb2FHbFB3YlJtNThnOUlrd01JUWdKRmRwZTRpWWU0bnZmX3VMNHlwcDBkWTJpZjQ2NE9SeQ==

>>> cl.comment_like(17926777897585108)
True

>>> cl.comment_unlike(17926777897585108)
True

>>> cl.comment_bulk_delete(media_id, [17926777897585108])
True
```



================================================
FILE: docs/usage-guide/direct.md
================================================
# Direct

| Method                                                                    | Return                  | Description
| ------------------------------------------------------------------------- | ----------------------- | ----------------------------------
| `direct_threads(amount: int = 20, selected_filter: str = "", thread_message_limit: Optional[int] = None)` <br> Note: selected_filter = "", "flagged" or "unread" | List[DirectThread] | Get all threads from inbox
| direct_pending_inbox(amount: int = 20)                                    | List[DirectThread]      | Get all threads from pending inbox
| direct_thread(thread_id: int, amount: int = 20)                           | DirectThread            | Get Thread with Messages
| direct_messages(thread_id: int, amount: int = 20)                         | List[DirectMessage]     | Get only Messages in Thread
| direct_answer(thread_id: int, text: str)                                  | DirectMessage           | Add Message to exist Thread
| direct_send(text: str, user_ids: List[int] = [], thread_ids: List[int] = []) | DirectMessage        | Send Message to Users or Threads
| direct_search(query: str)                                                 | List[DirectShortThread] | Search threads (for example by username)
| direct_thread_by_participants(user_ids: List[int])                        | DirectThread            | Get thread by user_id
| direct_thread_hide(thread_id: int)                                        | bool                    | Delete (called "hide")
| direct_media_share(media_id: str, user_ids: List[int])                    | DirectMessage           | Share a media to list of users
| direct_story_share(story_id: str, user_ids: List[int], thread_ids: List[int]) | DirectMessage       | Share a story to list of users
| direct_profile_share(user_id: str, user_ids: List[int], thread_ids: List[int]) | DirectMessage      | Share a user profile to list of users
| direct_thread_mark_unread(thread_id: int)                                 | bool                    | Mark a thread as unread
| direct_message_delete(thread_id: int, message_id: int)                    | bool                    | Delete a message from thread
| direct_thread_mute(thread_id: int, revert: bool = False)                  | bool                    | Mute the thread
| direct_thread_unmute(thread_id: int)                                      | bool                    | Unmute the thread
| direct_thread_mute_video_call(thread_id: int, revert: bool = False)       | bool                    | Mute video call for the thread
| direct_thread_unmute_video_call(thread_id: int)                           | bool                    | Unmute video call for the thread
| direct_send_photo(path: Path, user_ids: List[int], thread_ids: List[int]) | DirectMessage           | Send a direct photo to list of users or threads
| direct_send_video(path: Path, user_ids: List[int], thread_ids: List[int]) | DirectMessage           | Send a direct video to list of users or threads
| video_upload_to_direct(path: Path, caption: str, thumbnail: Path, mentions: List[StoryMention], thread_ids: List[int] = [], extra_data: Dict[str, str] = {}) | DirectMessage | Upload video to direct thread as a story and configure it

Example of basic actions:

``` python
>>> from instagrapi import Client
>>> cl = Client()
>>> cl.login(USERNAME, PASSWORD)

>>> thread = cl.direct_threads(1)[0]
>>> thread.pk
18123276039123479

>>> thread.users
[UserShort(pk=123123123, username='something', full_name='Dima Something', profile_pic_url=HttpUrl('https://instagram.frix7-1.fna.fbcdn.net/v/t51.2885-19/s150x150/11374323_1630877790512376_1081658215_a.jpg?_nc_ht=instagram.frix7-1.fna.fbcdn.net&_nc_ohc=k22oMvVv8xEAX-UEVRB&edm=AI8ESKwBAAAA&ccb=7-4&oh=be799948b28f19d85158153d886d16d3&oe=6135D80F&_nc_sid=195af5', scheme='https', host='instagram.frix7-1.fna.fbcdn.net', tld='net', host_type='domain', path='/v/t51.2885-19/s150x150/11374323_1630877790512376_1081658215_a.jpg', query='_nc_ht=instagram.frix7-1.fna.fbcdn.net&_nc_ohc=k22oMvVv8xEAX-UEVRB&edm=AI8ESKwBAAAA&ccb=7-4&oh=be799948b28f19d85158153d886d16d3&oe=6135D80F&_nc_sid=195af5'), profile_pic_url_hd=None, is_private=False, stories=[])]

>>> thread.messages[0]
DirectMessage(id=300761992574947211231231241955932160, user_id=123123123, thread_id=None, timestamp=datetime.datetime(2021, 8, 31, 18, 20, 28, 754135, tzinfo=datetime.timezone.utc), item_type='text', is_shh_mode=False, reactions=None, text='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua', animated_media=None, media=None, media_share=None, reel_share=None, story_share=None, felix_share=None, clip=None, placeholder=None)

>>> cl.direct_pending_inbox(1)[0]
DirectThread(
    pk=17881231232408606,
    id=3402823668123123123949128156938656669726,
    messages=[
        DirectMessage(
            id=30073094913010429825449992959033344,
            user_id=123123123123,
            ...
        )
    ],
    ...
)

>>> cl.direct_thread(thread.id, 1)
DirectThread(
    pk=18103276039108479,
    id=340282366841710300949128373114263369599,
    messages=[
        DirectMessage(
            id=30076199257494728485375741955932160,
            user_id=7789547,
            ...
        )
    ],
    ...
)

>>> message = cl.direct_messages(thread.id, 1)[0]
DirectMessage(id=300712312341231237412312312360, user_id=12312312, thread_id=None, timestamp=datetime.datetime(2021, 8, 31, 18, 20, 28, 754135, tzinfo=datetime.timezone.utc), item_type='text', is_shh_mode=False, reactions=None, text='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua', animated_media=None, media=None, media_share=None, reel_share=None, story_share=None, felix_share=None, clip=None, placeholder=None)

>>> cl.direct_answer(thread.id, 'Hello!')
DirectMessage(id=30076213210116812312341061613568, user_id=None, thread_id=34028236684171031231231231233331238762, timestamp=datetime.datetime(2021, 8, 31, 18, 33, 5, 127298, tzinfo=datetime.timezone.utc), item_type=None, is_shh_mode=None, reactions=None, text=None, animated_media=None, media=None, media_share=None, reel_share=None, story_share=None, felix_share=None, clip=None, placeholder=None)

>>> cl.direct_send('How are you?', user_ids=[cl.user_id])  # send youself
DirectMessage(id=30076213210116812312341061613568, user_id=None, thread_id=34028236684171031231231231233331238762, timestamp=datetime.datetime(2021, 8, 31, 18, 33, 5, 127298, tzinfo=datetime.timezone.utc), item_type=None, is_shh_mode=None, reactions=None, text=None, animated_media=None, media=None, media_share=None, reel_share=None, story_share=None, felix_share=None, clip=None, placeholder=None)

>>> cl.direct_send('How are you?', thread_ids=[thread.id])
DirectMessage(id=30076213210116812312341061613568, user_id=None, thread_id=34028236684171031231231231233331238762, timestamp=datetime.datetime(2021, 8, 31, 18, 33, 5, 127298, tzinfo=datetime.timezone.utc), item_type=None, is_shh_mode=None, reactions=None, text=None, animated_media=None, media=None, media_share=None, reel_share=None, story_share=None, felix_share=None, clip=None, placeholder=None)

>>> cl.direct_thread_by_participants([cl.user_id])
DirectThread(pk=178612312342, id=340282366812312312312341298762, messages=[DirectMessage(id=30076214123123123123123864, user_id=1903424587, thread_id=None, timestamp=datetime.datetime(2021, 8, 31, 18, 33, 49, 107154, ...)

>>> cl.direct_media_share(media.pk, user_ids=[cl.user_id])
DirectMessage(id=3007629312312312312312300374016, user_id=None, thread_id=340282366812313212334410641298762, timestamp=datetime.datetime(2021, 8, 31, 19, 45, 20, 708276, tzinfo=datetime.timezone.utc), item_type=None, is_shh_mode=None, reactions=None, text=None, animated_media=None, media=None, media_share=None, reel_share=None, story_share=None, felix_share=None, clip=None, placeholder=None)

>>> cl.direct_story_share(media.pk, user_ids=[cl.user_id])
DirectMessage(id=30076291231321231369939116032, user_id=None, thread_id=340282312312312334410641298762, timestamp=datetime.datetime(2021, 8, 31, 19, 48, 12, 217677, tzinfo=datetime.timezone.utc), item_type=None, is_shh_mode=None, reactions=None, text=None, animated_media=None, media=None, media_share=None, reel_share=None, story_share=None, felix_share=None, clip=None, placeholder=None)

>>> cl.direct_story_share(media.pk, thread_ids=[thread.id])
DirectMessage(id=30076291231231230352896, user_id=None, thread_id=3402812312312310641298762, timestamp=datetime.datetime(2021, 8, 31, 19, 48, 38, 482706, tzinfo=datetime.timezone.utc), item_type=None, is_shh_mode=None, reactions=None, text=None, animated_media=None, media=None, media_share=None, reel_share=None, story_share=None, felix_share=None, clip=None, placeholder=None)

>>> cl.direct_message_delete(thread.id, message.pk)
True

>>> photo_path = cl.photo_download(cl.media_pk_from_url('https://www.instagram.com/p/BgqFyjqloOr/'))
>>> cl.direct_send_photo(photo_path, user_ids=[cl.user_id])  # or
>>> cl.direct_send_photo(photo_path, thread_ids=[thread.id])
DirectMessage(id=300775273512312312312321568, user_id=None, thread_id=34028236123123123123128762, timestamp=datetime.datetime(2021, 9, 1, 14, 20, 24, 949673, tzinfo=datetime.timezone.utc), item_type=None, is_shh_mode=None, reactions=None, text=None, animated_media=None, media=None, media_share=None, reel_share=None, story_share=None, felix_share=None, clip=None, placeholder=None)

>>> video_path = cl.video_download(cl.media_pk_from_url('https://www.instagram.com/p/B3rFQPblq40/'))
>>> cl.direct_send_video(video_path, user_ids=[cl.user_id])  # or
>>> cl.direct_send_video(video_path, thread_ids=[thread.id])
Analyzing video file "/.../example_2155839952940084788.mp4"
DirectMessage(id=300775489123123123123664, user_id=None, thread_id=34012312312312312398762, timestamp=datetime.datetime(2021, 9, 1, 14, 39, 56, 959454, tzinfo=datetime.timezone.utc), item_type=None, is_shh_mode=None, reactions=None, text=None, animated_media=None, media=None, media_share=None, reel_share=None, story_share=None, felix_share=None, clip=None, placeholder=None)

>>> cl.video_upload_to_direct(video_path, thread_ids=[thread.id])
Analyzing video file "/.../example_2155839952940084788.mp4"
Generating thumbnail "/.../example_2155839952940084788.mp4.jpg"...
DirectMessage(id=3007123123123123664, user_id=None, thread_id=3401212312312312398762, timestamp=datetime.datetime(2021, 9, 1, 14, 39, 56, 959454, tzinfo=datetime.timezone.utc), item_type=None, is_shh_mode=None, reactions=None, text=None, animated_media=None, media=None, media_share=None, reel_share=None, story_share=None, felix_share=None, clip=None, placeholder=None)

>>> cl.direct_thread_mark_unread(340282366841710301949128122292511813703)
True

>>> cl.direct_thread_mute(340282366841710301949128122292511813703)
True

>>> cl.direct_thread_mute_video_call(340282366841710301949128122292511813703)
True

>>> cl.direct_thread_unmute_video_call(340282366841710301949128122292511813703)
True

>>> cl.direct_thread_unmute(340282366841710301949128122292511813703)
True
```



================================================
FILE: docs/usage-guide/fundamentals.md
================================================
# Usage Guide

This section provides detailed descriptions of all the ways `instagrapi` can be used. If you are new to `instagrapi`, the
[Getting Started](../getting-started.md) page provides a gradual introduction of the basic functionality with examples.

## Public vs Private Requests

* `Public` (anonymous request via web api) methods have a suffix `_gql` (Instagram `GraphQL`) or `_a1` (example `https://www.instagram.com/example/?__a=1`)
* `Private` (authorized request via mobile api) methods have `_v1` suffix

The first request to fetch media/user is `public` (anonymous), if instagram raise exception, then use `private` (authorized).

## Detailed Sections

* [Index](../index.md)
* [Getting Started](../getting-started.md)
* [Interactions](interactions.md)
  * [`Media`](media.md) - Publication (also called post): Photo, Video, Album, IGTV and Reels
  * [`Resource`](media.md) - Part of Media (for albums)
  * [`MediaOembed`](media.md) - Short version of Media
  * [`Account`](account.md) - Full private info for your account (e.g. email, phone_number)
  * [`User`](user.md) - Full public user data
  * [`UserShort`](user.md) - Short public user data (used in Usertag, Comment, Media, Direct Message)
  * [`Usertag`](user.md) - Tag user in Media (coordinates + UserShort)
  * [`Location`](location.md) - GEO location (GEO coordinates, name, address)
  * [`Hashtag`](hashtag.md) - Hashtag object (id, name, picture)
  * [`Collection`](collection.md) - Collection of medias (name, picture and list of medias)
  * [`Comment`](comment.md) - Comments to Media
  * [`Highlight`](highlight.md) - Highlights
  * [`Story`](story.md) - Story
  * [`StoryLink`](story.md) - Link (Swipe up)
  * [`StoryLocation`](story.md) - Tag Location in Story (as sticker)
  * [`StoryMention`](story.md) - Mention users in Story (user, coordinates and dimensions)
  * [`StoryHashtag`](story.md) - Hashtag for story (as sticker)
  * [`StorySticker`](story.md) - Tag sticker to story (for example from giphy)
  * [`StoryBuild`](story.md) - [StoryBuilder](https://github.com/subzeroid/instagrapi/blob/master/instagrapi/story.py) return path to photo/video and mention co-ordinates
  * [`DirectThread`](direct.md) - Thread (topic) with messages in Direct Message
  * [`DirectMessage`](direct.md) - Message in Direct Message
  * [`Insight`](insight.md) - Insights for a post
  * [`Track`](track.md) - Music track (for Reels/Clips)
* [Best Practices](best-practices.md)
* [Development Guide](../development-guide.md)
* [Handle Exceptions](handle_exception.md)
* [Exceptions](../exceptions.md)



================================================
FILE: docs/usage-guide/handle_exception.md
================================================
You can handle any exceptions using a generic handler:

``` python
from instagrapi import Client
from instagrapi.exceptions import (
    BadPassword, ReloginAttemptExceeded, ChallengeRequired,
    SelectContactPointRecoveryForm, RecaptchaChallengeForm,
    FeedbackRequired, PleaseWaitFewMinutes, LoginRequired
)


def handle_exception(client, e):
    if isinstance(e, BadPassword):
        client.logger.exception(e)
        client.set_proxy(self.next_proxy().href)
        if client.relogin_attempt > 0:
            self.freeze(str(e), days=7)
            raise ReloginAttemptExceeded(e)
        client.settings = self.rebuild_client_settings()
        return self.update_client_settings(client.get_settings())
    elif isinstance(e, LoginRequired):
        client.logger.exception(e)
        client.relogin()
        return self.update_client_settings(client.get_settings())
    elif isinstance(e, ChallengeRequired):
        api_path = json_value(client.last_json, "challenge", "api_path")
        if api_path == "/challenge/":
            client.set_proxy(self.next_proxy().href)
            client.settings = self.rebuild_client_settings()
        else:
            try:
                client.challenge_resolve(client.last_json)
            except ChallengeRequired as e:
                self.freeze('Manual Challenge Required', days=2)
                raise e
            except (ChallengeRequired, SelectContactPointRecoveryForm, RecaptchaChallengeForm) as e:
                self.freeze(str(e), days=4)
                raise e
            self.update_client_settings(client.get_settings())
        return True
    elif isinstance(e, FeedbackRequired):
        message = client.last_json["feedback_message"]
        if "This action was blocked. Please try again later" in message:
            self.freeze(message, hours=12)
            # client.settings = self.rebuild_client_settings()
            # return self.update_client_settings(client.get_settings())
        elif "We restrict certain activity to protect our community" in message:
            # 6 hours is not enough
            self.freeze(message, hours=12)
        elif "Your account has been temporarily blocked" in message:
            """
            Based on previous use of this feature, your account has been temporarily
            blocked from taking this action.
            This block will expire on 2020-03-27.
            """
            self.freeze(message)
    elif isinstance(e, PleaseWaitFewMinutes):
        self.freeze(str(e), hours=1)
    raise e

cl = Client()
cl.handle_exception = handle_exception
cl.login(USERNAME, PASSWORD)
```

In this way, you can centrally handle errors and not repeat handlers throughout your code.

Full example [here](https://github.com/subzeroid/instagrapi/blob/master/examples/handle_exception.py)



================================================
FILE: docs/usage-guide/hashtag.md
================================================
# Hashtag

Viewing hashtag info and medias by hashtag

| Method                                             | Return              | Description
| -------------------------------------------------- | ------------------- | ---------------------------------------
| hashtag_info(name: str)                            | Hashtag             | Return Hashtag info (id, name, picture)
| hashtag_related_hashtags(name: str)                | List[Hashtag]       | Return list of related Hashtag
| hashtag_medias_top(name: str, amount: int = 9)     | List[Media]         | Return Top posts by Hashtag
| hashtag_medias_recent(name: str, amount: int = 27) | List[Media]         | Return Most recent posts by Hashtag


Example:

``` python
>>> from instagrapi import Client

>>> cl = Client()
>>> cl.login(USERNAME, PASSWORD)

>>> hashtag = cl.hashtag_info('downhill')
>>> hashtag.dict()
{'id': 17841563089103670,
 'name': 'downhill',
 'media_count': 5178255,
 'profile_pic_url': HttpUrl('https://instagram.fhel3-1.fna.fbcdn.net/v/t51.2885-15/e35/s150x150/184304495_294863488920457_8839934375675895594_n.jpg?tp=1&_nc_ht=instagram.fhel3-1.fna.fbcdn.net&_nc_cat=101&_nc_ohc=L3i9yzFUBR8AX_MAXgr&edm=ABZsPhsBAAAA&ccb=7-4&oh=21a944a197506a42658e8273d92740b7&oe=60C37E35&_nc_sid=4efc9f', scheme='https', host='instagram.fhel3-1.fna.fbcdn.net', tld='net', host_type='domain', path='/v/t51.2885-15/e35/s150x150/184304495_294863488920457_8839934375675895594_n.jpg', query='tp=1&_nc_ht=instagram.fhel3-1.fna.fbcdn.net&_nc_cat=101&_nc_ohc=L3i9yzFUBR8AX_MAXgr&edm=ABZsPhsBAAAA&ccb=7-4&oh=21a944a197506a42658e8273d92740b7&oe=60C37E35&_nc_sid=4efc9f')}

>>> medias = cl.hashtag_medias_top('downhill', amount=2)
>>> medias[0].dict()
{'pk': 2574092718364154697,
 'id': '2574092718364154697_376712420',
 'code': 'CO5A7BxA9tJ',
 'taken_at': datetime.datetime(2021, 5, 15, 10, 49, 45, tzinfo=datetime.timezone.utc),
 'media_type': 1,
 'product_type': '',
 'thumbnail_url': HttpUrl('https://instagram.fhel3-1.fna.fbcdn.net/v/t51.2885-15/e35/s1080x1080/186430270_473573763896149_2030909827389015824_n.jpg?tp=1&_nc_ht=instagram.fhel3-1.fna.fbcdn.net&_nc_cat=101&_nc_ohc=4jFHY_INCnMAX-7fObK&edm=AP_V10EBAAAA&ccb=7-4&oh=9fb0c4cdb01a7aa376a96c0df366d844&oe=60C4C01A&_nc_sid=4f375e', scheme='https', host='instagram.fhel3-1.fna.fbcdn.net', tld='net', host_type='domain', path='/v/t51.2885-15/e35/s1080x1080/186430270_473573763896149_2030909827389015824_n.jpg', query='tp=1&_nc_ht=instagram.fhel3-1.fna.fbcdn.net&_nc_cat=101&_nc_ohc=4jFHY_INCnMAX-7fObK&edm=AP_V10EBAAAA&ccb=7-4&oh=9fb0c4cdb01a7aa376a96c0df366d844&oe=60C4C01A&_nc_sid=4f375e'),
 'location': {'pk': 517543,
  'name': 'Sestola',
  'address': '',
  'lng': 10.77328,
  'lat': 44.2266,
  'external_id': 103150459725396,
  'external_id_source': 'facebook_places'},
 'user': {'pk': 376712420,
  'username': 'vascobica',
  'full_name': '⚡Vasco Bica®⚡',
  'profile_pic_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t51.2885-19/s150x150/96211403_922669918147090_5138958292701151232_n.jpg?tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_ohc=tYlGX8kDuSgAX9WtBRF&edm=AP_V10EBAAAA&ccb=7-4&oh=ac96c75846d17519e53923a0ddb3aad0&oe=60C51486&_nc_sid=4f375e', scheme='https', host='scontent-hel3-1.cdninstagram.com', tld='com', host_type='domain', path='/v/t51.2885-19/s150x150/96211403_922669918147090_5138958292701151232_n.jpg', query='tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_ohc=tYlGX8kDuSgAX9WtBRF&edm=AP_V10EBAAAA&ccb=7-4&oh=ac96c75846d17519e53923a0ddb3aad0&oe=60C51486&_nc_sid=4f375e'),
  'stories': []},
 'comment_count': 8,
 'like_count': 327,
 'has_liked': None,
 'caption_text': 'Ready to fight ⚔️\n#js7 \n.\n.\n#swissmountainsports #racing #coppaitaliadh \n#mirandabikeparts\xa0#burning\xa0#jumping \xa0#whipit\xa0#scrubit\xa0#enduro\xa0#mtblife\xa0 #downhill\xa0#mountainbiking\xa0#sliding\xa0#dirt\xa0#dh\xa0 #mtb\xa0#bike\xa0#bikelife\xa0#friends\xa0#mtbswitzerland\xa0#downhillmtb\xa0#valais\xa0 #swissmountains\xa0\xa0#italy #italydownhill',
 'usertags': [{'user': {'pk': 3636959873,
    'username': 'christopherstrm',
    'full_name': 'Christopher Ström',
    'profile_pic_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t51.2885-19/s150x150/173775865_527371595096868_8991176723035066304_n.jpg?tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_ohc=tbsAzTDoLtEAX_HaT9Z&edm=AP_V10EBAAAA&ccb=7-4&oh=94a18b3b4d0d39d9dbda849b4c23a5a9&oe=60C5192F&_nc_sid=4f375e', scheme='https', host='scontent-hel3-1.cdninstagram.com', tld='com', host_type='domain', path='/v/t51.2885-19/s150x150/173775865_527371595096868_8991176723035066304_n.jpg', query='tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_ohc=tbsAzTDoLtEAX_HaT9Z&edm=AP_V10EBAAAA&ccb=7-4&oh=94a18b3b4d0d39d9dbda849b4c23a5a9&oe=60C5192F&_nc_sid=4f375e'),
    'stories': []},
   'x': 0.211352657,
   'y': 0.8478260870000001}],
 'video_url': None,
 'view_count': 0,
 'video_duration': 0.0,
 'title': '',
 'resources': []}

>>> medias = cl.hashtag_medias_recent('downhill', amount=2)
>>> medias[0].dict()
{'pk': 2574205305714324167,
 'id': '2574205305714324167_2984719638',
 'code': 'CO5ahY6BzLH',
 'taken_at': datetime.datetime(2021, 5, 15, 14, 33, 27, tzinfo=datetime.timezone.utc),
 'media_type': 8,
 'product_type': '',
 'thumbnail_url': None,
 'location': {'pk': 703017966745848,
  'name': 'Le Canyon Du Diable',
  'address': '',
  'lng': 3.4480762482,
  'lat': 43.6966105493,
  'external_id': 703017966745848,
  'external_id_source': 'facebook_places'},
 'user': {'pk': 2984719638,
  'username': 'lilian.champion',
  'full_name': 'Lilian 🇨🇵',
  'profile_pic_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t51.2885-19/s150x150/169115203_291696755653751_6779914563403118432_n.jpg?tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_ohc=VEqYwd5W1FYAX_7ID-6&edm=AP_V10EBAAAA&ccb=7-4&oh=7fe193da2e706c0cafd9e1d432734891&oe=60C59786&_nc_sid=4f375e', scheme='https', host='scontent-hel3-1.cdninstagram.com', tld='com', host_type='domain', path='/v/t51.2885-19/s150x150/169115203_291696755653751_6779914563403118432_n.jpg', query='tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_ohc=VEqYwd5W1FYAX_7ID-6&edm=AP_V10EBAAAA&ccb=7-4&oh=7fe193da2e706c0cafd9e1d432734891&oe=60C59786&_nc_sid=4f375e'),
  'stories': []},
 'comment_count': 0,
 'like_count': 0,
 'has_liked': None,
 'caption_text': "Quand on te prend en photo sans que tu aies demandé et que la personne t'envoie tout par mail après...😂😁🤙🏻 Merci l'inconnu du coup \n\n#downhill #mountainlovers #ytowners #vanlife #vanlifefrance",
 'usertags': [],
 'video_url': None,
 'view_count': 0,
 'video_duration': 0.0,
 'title': '',
 'resources': [{'pk': 2574205301050111226,
   'video_url': None,
   'thumbnail_url': HttpUrl('https://instagram.fhel3-1.fna.fbcdn.net/v/t51.2885-15/e35/184312115_2977220092557985_8274386175388868273_n.jpg?tp=1&_nc_ht=instagram.fhel3-1.fna.fbcdn.net&_nc_cat=101&_nc_ohc=YoLLGA0cAhsAX8MxnSo&edm=AP_V10EBAAAA&ccb=7-4&oh=b0f2740aaff1d80c5f5219ffa267a186&oe=60C4273E&_nc_sid=4f375e', scheme='https', host='instagram.fhel3-1.fna.fbcdn.net', tld='net', host_type='domain', path='/v/t51.2885-15/e35/184312115_2977220092557985_8274386175388868273_n.jpg', query='tp=1&_nc_ht=instagram.fhel3-1.fna.fbcdn.net&_nc_cat=101&_nc_ohc=YoLLGA0cAhsAX8MxnSo&edm=AP_V10EBAAAA&ccb=7-4&oh=b0f2740aaff1d80c5f5219ffa267a186&oe=60C4273E&_nc_sid=4f375e'),
   'media_type': 1},
  {'pk': 2574205301083731874,
   'video_url': None,
   'thumbnail_url': HttpUrl('https://instagram.fhel6-1.fna.fbcdn.net/v/t51.2885-15/e35/186524178_143770224434390_4909324648747352588_n.jpg?tp=1&_nc_ht=instagram.fhel6-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=w6z9v4MwYg8AX9FdWk0&edm=AP_V10EBAAAA&ccb=7-4&oh=99295fa82472bf4a425fc49bd03c1310&oe=60C40AFC&_nc_sid=4f375e', scheme='https', host='instagram.fhel6-1.fna.fbcdn.net', tld='net', host_type='domain', path='/v/t51.2885-15/e35/186524178_143770224434390_4909324648747352588_n.jpg', query='tp=1&_nc_ht=instagram.fhel6-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=w6z9v4MwYg8AX9FdWk0&edm=AP_V10EBAAAA&ccb=7-4&oh=99295fa82472bf4a425fc49bd03c1310&oe=60C40AFC&_nc_sid=4f375e'),
   'media_type': 1},
  {'pk': 2574205301066842492,
   'video_url': None,
   'thumbnail_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t51.2885-15/e35/186787154_332065288355469_7843843424299639709_n.jpg?tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_cat=109&_nc_ohc=-qZy9_HakCQAX-Cqk9v&edm=AP_V10EBAAAA&ccb=7-4&oh=031077ab2f56db0bab7ffbc920f80a41&oe=60C4F57B&_nc_sid=4f375e', scheme='https', host='scontent-hel3-1.cdninstagram.com', tld='com', host_type='domain', path='/v/t51.2885-15/e35/186787154_332065288355469_7843843424299639709_n.jpg', query='tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_cat=109&_nc_ohc=-qZy9_HakCQAX-Cqk9v&edm=AP_V10EBAAAA&ccb=7-4&oh=031077ab2f56db0bab7ffbc920f80a41&oe=60C4F57B&_nc_sid=4f375e'),
   'media_type': 1},
  {'pk': 2574205301075310332,
   'video_url': None,
   'thumbnail_url': HttpUrl('https://instagram.fhel3-1.fna.fbcdn.net/v/t51.2885-15/e35/185727252_524026898594344_9165723485744355754_n.jpg?tp=1&_nc_ht=instagram.fhel3-1.fna.fbcdn.net&_nc_cat=104&_nc_ohc=45NguRpEtZQAX83VSGE&edm=AP_V10EBAAAA&ccb=7-4&oh=c8c087ecfba444d9d85f7bd059f42a2a&oe=60C5C3C2&_nc_sid=4f375e', scheme='https', host='instagram.fhel3-1.fna.fbcdn.net', tld='net', host_type='domain', path='/v/t51.2885-15/e35/185727252_524026898594344_9165723485744355754_n.jpg', query='tp=1&_nc_ht=instagram.fhel3-1.fna.fbcdn.net&_nc_cat=104&_nc_ohc=45NguRpEtZQAX83VSGE&edm=AP_V10EBAAAA&ccb=7-4&oh=c8c087ecfba444d9d85f7bd059f42a2a&oe=60C5C3C2&_nc_sid=4f375e'),
   'media_type': 1}]}
```

Low level methods:

| Method                                         | Return  | Description
| ---------------------------------------------- | ------- | --------------------------------------------
| hashtag_info_a1(name: str, max_id: str = None) | Hashtag | Get information about a hashtag by Public Web API
| hashtag_info_gql(name: str, amount: int = 12, end_cursor: str = None) | Hashtag | Get information about a hashtag by Public Graphql API
| hashtag_info_v1(name: str) | Hashtag | Get information about a hashtag by Private Mobile API
| hashtag_medias_a1_chunk(name: str, max_amount: int = 27, tab_key: str = "edge_hashtag_to_top_posts\|edge_hashtag_to_media", end_cursor: str = None) | Tuple[List[Media], str] | Get chunk of medias and end_cursor by Public Web API
| hashtag_medias_a1(name: str, amount: int = 27, tab_key: str = "edge_hashtag_to_top_posts\|edge_hashtag_to_media") | List[Media] | Get medias for a hashtag by Public Web API
| hashtag_medias_v1_chunk(name: str, max_amount: int = 27, tab_key: str = "top\|recent", max_id: str = None) | Tuple[List[Media], str] | Get chunk of medias for a hashtag and max_id (cursor) by Private Mobile API
| hashtag_medias_v1(name: str, amount: int = 27, tab_key: str = "top\|recent") | List[Media] | Get medias for a hashtag by Private Mobile API
| hashtag_medias_top_a1(name: str, amount: int = 9) | List[Media] | Get top medias for a hashtag by Public Web API
| hashtag_medias_top_v1(name: str, amount: int = 9) | List[Media] | Get top medias for a hashtag by Private Mobile API
| hashtag_medias_recent_a1(name: str, amount: int = 71) | List[Media] | Get recent medias for a hashtag by Public Web API
| hashtag_medias_recent_v1(name: str, amount: int = 27) | List[Media] | Get recent medias for a hashtag by Private Mobile API
| hashtag_medias_reels_v1(name: str, amount: int = 27) | List[Media] | Get recent clips (reels) for a hashtag by Private Mobile API

Example for [Request for loading every next time new posts from hashtag](https://github.com/subzeroid/instagrapi/issues/79):

``` python
>>> medias, cursor = cl.hashtag_medias_v1_chunk('test', max_amount=32, tab_key='recent')
>>> len(medias)
32
>>> cursor
QVFDR0dzT3FJT0V4amFjMaQ3czlGVzRKV3FNWDJqaE1mWmltWU5VWGYtbnV6RVpoOUlsR3dCN05RRmpLc2R5SVlCQTNaekV5bUVOV0F4Vno1MDkxN1Nndg==

# NEXT cursor:

>>> medias, cursor = cl.hashtag_medias_v1_chunk('test', max_amount=32, tab_key='recent', max_id=cursor)
>>> len(medias)
32
>>> cursor
QVFEUXpfM0RtaDdmMExPQ0k0UWRlaHFJa2RVdVlaX01LTzhkNF9Dd1N2UlhtVy1vSTZvMERfYW5XN205OTBRNFBCSVJ2ZTVfTG5ZMXVmY0VJbUM5TU9URQ==
```



================================================
FILE: docs/usage-guide/highlight.md
================================================
# Highlight

| Method                                                                         | Return           | Description
| ------------------------------------------------------------------------------ | ---------------- | ----------------------------------
| highlight_pk_from_url(url: str)                                                | int              | Get Highlight PK from URL
| highlight_info(highlight_pk: int)                                              | Highlight        | Get Highlight by pk or id
| user_highlights(user_id: str, amount: int = 0)                                 | List[Highlight]  | Get a user's highlights
| highlight_create(title: str, story_ids: List[str], cover_story_id: str = "", crop_rect: List[float] = [0.0, 0.21830457, 1.0, 0.78094524]) | Highlight | Create highlight
| highlight_change_title(highlight_pk: str, title: str)                          | Highlight        | Change title for highlight
| highlight_change_cover(highlight_pk: str, cover_path: Path)                    | Highlight        | Change cover for highlight
| highlight_add_stories(highlight_pk: str, added_media_ids: List[str])           | Highlight        | Add stories to highlight
| highlight_remove_stories(highlight_pk: str, removed_media_ids: List[str])      | Highlight        | Remove stories from highlight
| highlight_delete(highlight_pk: str)                                            | bool             | Delete highlight

Example:

``` python
>>> cl.highlight_info(17895485201104054).dict()
{
    'pk': 17895485201104054,
    'id': 'highlight:17895485201104054',
    'latest_reel_media': 1622366765,
    'cover_media': {
        'cropped_image_version': {'width': 150, 'height': 150, 'url': 'https://instagram.frix7-1.fna.fbcdn.net/v/t51.2885-...'},
        'crop_rect': [0, 0.21855760773966576, 1, 0.7814423922603342],
        'media_id': '2584323966581791455_8641392340'
    },
    'user': {
        'pk': 8641392340,
        'username': 'bestskatetrick',
        'full_name': 'The Best Skate Tricks',
        'profile_pic_url': HttpUrl('https://instagram.frix7-1.fna.fbcdn.net/v/t51.2885-19/s150x150/6526...'),
        'profile_pic_url_hd': None,
        'is_private': False,
        'stories': []
    },
    'title': 'Picnic 2021',
    'created_at': datetime.datetime(2021, 5, 29, 19, 39, 15, tzinfo=datetime.timezone.utc),
    'is_pinned_highlight': False,
    'media_count': 19,
    'media_ids': [2584323966581791455, 2584328925731679183, 2584328595757338887, ...],  # story ids
    'items': [Story, Story, Story, ...]
}

>>> cl.user_highlights(29817608135)
[Highlight(pk='17907771728171896', id='highlight:17907771728171896', latest_reel_media=1638039687, ...), ...]
```

Change highlight:

``` python
>>> cl.highlight_create("Test", ["2722223419628084989_29817608135"])
Highlight(pk='17920472818962144', id='highlight:17920472818962144', latest_reel_media=1638734336, ...)

>>> cl.highlight_change_title(17907771728171896, "Example title")
Highlight(pk='17907771728171896', id='highlight:17907771728171896', latest_reel_media=1638039687, ...)

>>> cl.highlight_change_cover(17907771728171896, "/tmp/test.jpg")  # recommend 720x720
Highlight(pk='17907771728171896', id='highlight:17907771728171896', ...)

>>> cl.highlight_add_stories(17907771728171896, [2722223419628084989])
Highlight(pk='17907771728171896', id='highlight:17907771728171896', latest_reel_media=1638734336, ...)

>>> cl.highlight_remove_stories(17907771728171896, [2722223419628084989])
Highlight(pk='17907771728171896', id='highlight:17907771728171896', latest_reel_media=1638039687, ...)

>>> cl.highlight_delete(17920472818962144)
True
```



================================================
FILE: docs/usage-guide/insight.md
================================================
# Insights

Get statistics by medias. Common arguments:

* `post_type` - Media type: "ALL", "CAROUSEL_V2", "IMAGE", "SHOPPING", "VIDEO".
* `time_frame` - Time frame for media publishing date: "ONE_WEEK", "ONE_MONTH", "THREE_MONTHS", "SIX_MONTHS", "ONE_YEAR", "TWO_YEARS".
* `data_ordering` - Data ordering in instagram response: "REACH_COUNT", "LIKE_COUNT", "FOLLOW", "SHARE_COUNT", "BIO_LINK_CLICK", "COMMENT_COUNT", "IMPRESSION_COUNT", "PROFILE_VIEW", "VIDEO_VIEW_COUNT", "SAVE_COUNT".

| Method                                                                                             | Return             | Description
| -------------------------------------------------------------------------------------------------- | ------------------ | ------------------------------- 
| insights_media_feed_all(post_type: str = "ALL", time_frame: str = "TWO_YEARS", data_ordering: str = "REACH_COUNT", count: int = 0, sleep: int = 2) | List[Dict] | Return medias with insights
| insights_account()                                                                                 | Dict               | Get statistics by your account
| insights_media(media_pk: int)                                                                      | Dict               | Get statistics by your media


Example:

``` python
from instagrapi import Client

cl = Client()
cl.login(USERNAME, PASSWORD)

cl.insights_media_feed_all("VIDEO", "ONE_WEEK", "LIKE_COUNT", 42)
cl.insights_account()

media_pk = cl.media_pk_from_url('https://www.instagram.com/p/CP5h-I1FuPr/')
cl.insights_media(media_pk)
```



================================================
FILE: docs/usage-guide/interactions.md
================================================
# Interactions

`instagrapi` provides various types of `Interactions` that can be used to control how the program will interact with the `Instagram`:

* [`Media`](media.md) - Media (Photo, Video, Album, IGTV, Reels or Story)
* [`Resource`](media.md) - Part of Media (for albums)
* [`MediaOembed`](media.md) - Short version of Media
* [`Account`](account.md) - Full private info for your account (e.g. email, phone_number)
* [`TOTP`](totp.md) - 2FA TOTP helpers (generate seed, enable/disable TOTP, generate code as Google Authenticator)
* [`User`](user.md) - Full public user data
* [`UserShort`](user.md) - Short public user data (used in Usertag, Comment, Media, Direct)
* [`Usertag`](user.md) - Tag user in Media (coordinates + UserShort)
* [`Location`](location.md) - GEO location (GEO coordinates, name, address)
* [`Hashtag`](hashtag.md) - Hashtag object (id, name, picture)
* [`Collection`](collection.md) - Collection of medias (name, picture and list of medias)
* [`Comment`](comment.md) - Comments to Media
* [`Highlight`](highlight.md) - Highlights
* [`Story`](story.md) - Story
* [`StoryLink`](story.md) - Link (Swipe up)
* [`StoryLocation`](story.md) - Tag Location in Story (as sticker)
* [`StoryMention`](story.md) - Mention users in Story (user, coordinates and dimensions)
* [`StoryHashtag`](story.md) - Hashtag for story (as sticker)
* [`StorySticker`](story.md) - Tag sticker to story (for example from giphy)
* [`StoryBuild`](story.md) - [StoryBuilder](https://github.com/subzeroid/instagrapi/blob/master/instagrapi/story.py) return path to photo/video and mention co-ordinates
* [`DirectThread`](direct.md) - Thread (topic) with messages in Direct
* [`DirectMessage`](direct.md) - Message in Direct
* [`Insight`](insight.md) - Insights for a post
* [`Track`](track.md) - Music track (for Reels/Clips)

## Interacting with Instagram Account

`instagrapi` provides the following `Interactions` that can be used to control and get the information about your `Instagram` account:

* Client(settings: dict = {}, proxy: str = ""): bool - Init `instagrapi` client

``` python
cl.login("instagrapi", "42")
# cl.login("instagrapi", "42", verification_code="123456")  # with 2FA verification_code
# cl.login_by_sessionid("peiWooShooghahdi2Eip7phohph0eeng")
cl.set_proxy("socks5://127.0.0.1:30235")
# cl.set_proxy("http://username:password@127.0.0.1:8080")
# cl.set_proxy("socks5://username:password@127.0.0.1:30235")
# when addressing the proxy via hostname:
# cl.set_proxy("socks5h://username:password@exampleproxy.tld:30235")

print(cl.get_settings())
print(cl.user_info(cl.user_id))
```

We recommend using [these proxies](https://soax.com/?r=sEysufQI)

### Request

| Property            | Description
| ------------------- | --------------------------------------------------------------
| request\_logger     | Logger in which various actions from Instagram are registered
| request\_timeout    | Timeout in seconds between requests (1 second by default)


### Login

| Method                               | Return  | Description
| ------------------------------------ | ------- | -------------------------------------------------
| login(username: str, password: str)  | bool    | Login by username and password (get new cookies if it does not exist in settings)
| login(username: str, password: str, verification\_code: str) | bool | Login by username and password with 2FA verification code (use Google Authenticator or something similar to generate TOTP code, not work with SMS)
| relogin()                            | bool    | Re-login with clean cookies (required cl.username and cl.password)
| login\_by\_sessionid(sessionid: str) | bool    | Login by sessionid from Instagram site
| inject\_sessionid\_to\_public()      | bool    | Inject sessionid from Private Session to Public Session
| logout()                             | bool    | Logout

You can pass settings to the Client (and save cookies), it has the following format:

```python
settings = {
   "uuids": {
      "phone_id": "57d64c41-a916-3fa5-bd7a-3796c1dab122",
      "uuid": "8aa373c6-f316-44d7-b49e-d74563f4a8f3",
      "client_session_id": "6c296d0a-3534-4dce-b5aa-a6a6ab017443",
      "advertising_id": "8dc88b76-dfbc-44dc-abbc-31a6f1d54b04",
      "device_id": "android-e021b636049dc0e9"
   },
   "cookies":  {},  # set here your saved cookies
   "last_login": 1596069420.0000145,
   "device_settings": {
      "cpu": "h1",
      "dpi": "640dpi",
      "model": "h1",
      "device": "RS988",
      "resolution": "1440x2392",
      "app_version": "117.0.0.28.123",
      "manufacturer": "LGE/lge",
      "version_code": "168361634",
      "android_release": "6.0.1",
      "android_version": 23
   },
   "user_agent": "Instagram 117.0.0.28.123 Android (23/6.0.1; ...US; 168361634)"
}

cl = Client(settings)
```

### Settings

Store and manage uuids, device configuration, user agent, authorization data (aka cookies) and other session settings

| Method                         | Return  | Description
| ------------------------------ | ------- | ------------------------------------------------------------------
| get\_settings()                | dict    | Return settings dict
| set\_settings(settings: dict)  | bool    | Set session settings
| load\_settings(path: Path)     | dict    | Load session settings from file
| dump\_settings(path: Path)     | bool    | Serialize and save session settings to file

In order for Instagram [to trust you more](https://github.com/subzeroid/instagrapi/discussions/220), you must always login from one device and one IP (or from a subnet):

```python
cl = Client()
cl.login(USERNAME, PASSWORD)
cl.dump_settings('/tmp/dump.json')
```

Next time:

```python
cl = Client()
cl.load_settings('/tmp/dump.json')
cl.login(USERNAME, PASSWORD)
cl.get_timeline_feed()  # check session
```

### Manage device, proxy and other account settings

| Method                                   | Return | Description
|------------------------------------------|------|----------------------------------------------------------------------------
| set_proxy(dsn: str)                      | dict | Support socks and http/https proxy "scheme://username:password@host:port". We recommend using [these proxies](https://soax.com/?r=sEysufQI)
| private.proxies                          | dict | Stores used proxy servers for private (mobile, v1) requests
| public.proxies                           | dict | Stores used proxy servers for public (web, graphql) requests
| set_device(device: dict)                 | bool | Change device settings ([Android Device Information Generator Online](https://www.myfakeinfo.com/mobile/get-android-device-information.php))
| device                                   | dict | Return device dict which we pass to Instagram
| set_user_agent(user_agent: str = "")     | bool | Change User-Agent header ([User Agents](https://user-agents.net/applications/instagram-app))
| cookie_dict                              | dict | Return cookies
| user_id                                  | int  | Return your user_id (after login)
| base_headers                             | dict | Base headers for Instagram
| set_country(country: str = "US")         | bool | Set country (advice: use the country of your proxy)
| set_country_code(country_code: int = 1)  | bool | Set country calling code. Default: +1 (USA)
| set_locale(locale: str = "en_US")        | bool | Set locale (advice: use the locale of your proxy)
| set_timezone_offset(seconds: int)        | bool | Set timezone offset in seconds

``` python
cl = Client()

# Los Angles user:
cl.set_proxy('http://los:angeles@proxy.address:8080')
cl.set_locale('en_US')
cl.set_timezone_offset(-7 * 60 * 60)  # Los Angeles UTC (GMT) -7 hours == -25200 seconds
cl.get_settings()
{
    ...
    'user_agent': 'Instagram 194.0.0.36.172 Android (26/8.0.0; 480dpi; 1080x1920; Xiaomi; MI 5s; capricorn; qcom; en_US; 301484483)',
    'country': 'US',
    'country_code': 1,
    'locale': 'en_US',
    'timezone_offset': -25200
}

# Moscow user:
cl.set_proxy('socks5://moscow:proxy@address:8080')
cl.set_locale('ru_RU')
cl.set_country_code(7)  # +7
cl.set_timezone_offset(3 * 3600)  # Moscow UTC+3
cl.get_settings()
{
    ...
    'user_agent': 'Instagram 194.0.0.36.172 Android (26/8.0.0; 480dpi; 1080x1920; Xiaomi; MI 5s; capricorn; qcom; ru_RU; 301484483)',
    'country': 'RU',
    'country_code': 7,
    'locale': 'ru_RU',
    'timezone_offset': 10800
}
```

## What's Next?

* [Getting Started](../getting-started.md)
* [Usage Guide](fundamentals.md)
* [Handle Exceptions](handle_exception.md)
* [Challenge Resolver](challenge_resolver.md)
* [Exceptions](../exceptions.md)



================================================
FILE: docs/usage-guide/location.md
================================================
# Location (place)

Viewing location info and medias by location

| Method                                                     | Return         | Description
| ---------------------------------------------------------- | -------------- | ----------------------------------------------------
| location_search(lat: float, lng: float)                    | List[Location] | Search Location by GEO coordinates
| location_complete(location: Location)                      | Location       | Complete blank fields
| location_build(location: Location)                         | String         | Serialized JSON
| location_info(location_pk: int)                            | Location       | Return Location info (pk, name, address, lng, lat, external_id, external_id_source)
| location_medias_top(location_pk: int, amount: int = 9)     | List[Media]    | Return Top posts by Location
| location_medias_recent(location_pk: int, amount: int = 24) | List[Media]    | Return Most recent posts by Location
| fbsearch_places(query: str, lat: float = 40.74, lng: float = -73.94) | List[Location] | >Search places via Facebook Search (40.74/-73.94 - New York, default GEO)


Example:

``` python
>>> from instagrapi import Client

>>> cl = Client()
>>> cl.login(USERNAME, PASSWORD)

>>> location = cl.location_search(59.96, 30.29)[0]
>>> location.dict()
{'pk': None,
 'name': 'Russia, Saint-Petersburg',
 'address': 'Russia, Saint-Petersburg',
 'lng': 30.30605,
 'lat': 59.93318,
 'external_id': 107617247320879,
 'external_id_source': 'facebook_places'}

>>> location = cl.location_complete(location)
>>> location.dict()
{'pk': 107617247320879,
 'name': 'Russia, Saint-Petersburg',
 'address': 'Russia, Saint-Petersburg',
 'lng': 30.30605,
 'lat': 59.93318,
 'external_id': 107617247320879,
 'external_id_source': 'facebook_places'}

>>> cl.location_build(location)
'{"name":"Russia, Saint-Petersburg","address":"Russia, Saint-Petersburg","lat":59.93318,"lng":30.30605,"external_source":"facebook_places","facebook_places_id":107617247320879}'

>>> location = cl.location_info(107617247320879)
>>> location.dict()
{'pk': 107617247320879,
 'name': 'Russia, Saint-Petersburg',
 'address': '',
 'lng': 30.30605,
 'lat': 59.93318,
 'external_id': None,
 'external_id_source': None}

>>> medias = cl.location_medias_top(107617247320879, amount=2)
>>> medias[0].dict()
{'pk': 2574095228556148891,
 'id': '2574095228556148891_8227888596',
 'code': 'CO5BfjkHgCb',
 'taken_at': datetime.datetime(2021, 5, 15, 11, 6, 25, tzinfo=datetime.timezone.utc),
 'media_type': 2,
 'product_type': 'feed',
 'thumbnail_url': HttpUrl('https://instagram.fhel3-1.fna.fbcdn.net/v/t51.2885-15/e35/185874360_510656656615872_846247842213042525_n.jpg?tp=1&_nc_ht=instagram.fhel3-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=vUIk3PZPPrMAX_GGZ7n&edm=AP_V10EBAAAA&ccb=7-4&oh=e418e018b9fc07b7d6b78f0790ddb481&oe=60A24C1F&_nc_sid=4f375e', scheme='https', host='instagram.fhel3-1.fna.fbcdn.net', tld='net', host_type='domain', path='/v/t51.2885-15/e35/185874360_510656656615872_846247842213042525_n.jpg', query='tp=1&_nc_ht=instagram.fhel3-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=vUIk3PZPPrMAX_GGZ7n&edm=AP_V10EBAAAA&ccb=7-4&oh=e418e018b9fc07b7d6b78f0790ddb481&oe=60A24C1F&_nc_sid=4f375e'),
 'location': {'pk': 107617247320879,
  'name': 'Russia, Saint-Petersburg',
  'address': '',
  'lng': 30.30605,
  'lat': 59.93318,
  'external_id': 107617247320879,
  'external_id_source': 'facebook_places'},
 'user': {'pk': 8227888596,
  'username': 'mzefirov',
  'full_name': 'МИХАИЛ ЗЕФИРОВ🌶️🔥ПРО ОТНОШЕНИЯ',
  'profile_pic_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t51.2885-19/s150x150/54513886_664942437287042_6311410572676038656_n.jpg?tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_ohc=mOWHIYJXbMsAX8wXvzf&edm=AP_V10EBAAAA&ccb=7-4&oh=90fa78d26bbb2c577dbc27d012c7cf09&oe=60C6A82B&_nc_sid=4f375e', scheme='https', host='scontent-hel3-1.cdninstagram.com', tld='com', host_type='domain', path='/v/t51.2885-19/s150x150/54513886_664942437287042_6311410572676038656_n.jpg', query='tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_ohc=mOWHIYJXbMsAX8wXvzf&edm=AP_V10EBAAAA&ccb=7-4&oh=90fa78d26bbb2c577dbc27d012c7cf09&oe=60C6A82B&_nc_sid=4f375e'),
  'stories': []},
 'comment_count': 94,
 'like_count': 3995,
 'has_liked': None,
 'caption_text': 'Антонина Роббинс, или немного о мотивации.\n\nСтавь ❤️и делись в сторис... это мотивирует.',
 'usertags': [],
 'video_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t50.2886-16/185466467_1373704339669543_4721533329541547409_n.mp4?_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_cat=107&_nc_ohc=IdbMAqYCjngAX987nBb&edm=AP_V10EBAAAA&ccb=7-4&oe=60A1DADD&oh=7c69dc13e5344f7095a94eb717b1ee9e&_nc_sid=4f375e', scheme='https', host='scontent-hel3-1.cdninstagram.com', tld='com', host_type='domain', path='/v/t50.2886-16/185466467_1373704339669543_4721533329541547409_n.mp4', query='_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_cat=107&_nc_ohc=IdbMAqYCjngAX987nBb&edm=AP_V10EBAAAA&ccb=7-4&oe=60A1DADD&oh=7c69dc13e5344f7095a94eb717b1ee9e&_nc_sid=4f375e'),
 'view_count': 36295,
 'video_duration': 55.433,
 'title': '',
 'resources': []}

>>> medias = cl.location_medias_recent(107617247320879, amount=2)
>>> medias[0].dict()
{'pk': 2574187014843321420,
 'id': '2574187014843321420_5600296444',
 'code': 'CO5WXONKMxM',
 'taken_at': datetime.datetime(2021, 5, 15, 13, 57, 6, tzinfo=datetime.timezone.utc),
 'media_type': 1,
 'product_type': '',
 'thumbnail_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/186279877_479327446453989_5642409805215171470_n.jpg?tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_cat=109&_nc_ohc=Nx9KwOGWXLYAX_bh1Dx&edm=AP_V10EBAAAA&ccb=7-4&oh=999395b5e4a3c688bcb388616f405161&oe=60C4C08C&_nc_sid=4f375e', scheme='https', host='scontent-hel3-1.cdninstagram.com', tld='com', host_type='domain', path='/v/t51.2885-15/e35/p1080x1080/186279877_479327446453989_5642409805215171470_n.jpg', query='tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_cat=109&_nc_ohc=Nx9KwOGWXLYAX_bh1Dx&edm=AP_V10EBAAAA&ccb=7-4&oh=999395b5e4a3c688bcb388616f405161&oe=60C4C08C&_nc_sid=4f375e'),
 'location': {'pk': 107617247320879,
  'name': 'Russia, Saint-Petersburg',
  'address': '',
  'lng': 30.30605,
  'lat': 59.93318,
  'external_id': 107617247320879,
  'external_id_source': 'facebook_places'},
 'user': {'pk': 5600296444,
  'username': 'sultanieriabinina',
  'full_name': 'Султание Беляловна',
  'profile_pic_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t51.2885-19/s150x150/92693550_492095081670507_2163230119093600256_n.jpg?tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_ohc=_8hEZtz-JSIAX_NCxXx&edm=AP_V10EBAAAA&ccb=7-4&oh=17d2d1a8ae00765b8471cde868937c13&oe=60C69D73&_nc_sid=4f375e', scheme='https', host='scontent-hel3-1.cdninstagram.com', tld='com', host_type='domain', path='/v/t51.2885-19/s150x150/92693550_492095081670507_2163230119093600256_n.jpg', query='tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_ohc=_8hEZtz-JSIAX_NCxXx&edm=AP_V10EBAAAA&ccb=7-4&oh=17d2d1a8ae00765b8471cde868937c13&oe=60C69D73&_nc_sid=4f375e'),
  'stories': []},
 'comment_count': 0,
 'like_count': 0,
 'has_liked': None,
 'caption_text': '',
 'usertags': [{'user': {'pk': 3955327494,
    'username': '_parikmakher_irishka3127',
    'full_name': 'ИрИнА',
    'profile_pic_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t51.2885-19/s150x150/176040256_461659781826794_5379061705031591554_n.jpg?tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_ohc=uVHqkpa8v0UAX-cmGUE&edm=AP_V10EBAAAA&ccb=7-4&oh=22db3640b911117484d78422eec4f778&oe=60C523D5&_nc_sid=4f375e', scheme='https', host='scontent-hel3-1.cdninstagram.com', tld='com', host_type='domain', path='/v/t51.2885-19/s150x150/176040256_461659781826794_5379061705031591554_n.jpg', query='tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_ohc=uVHqkpa8v0UAX-cmGUE&edm=AP_V10EBAAAA&ccb=7-4&oh=22db3640b911117484d78422eec4f778&oe=60C523D5&_nc_sid=4f375e'),
    'stories': []},
   'x': 0.352,
   'y': 0.292}],
 'video_url': None,
 'view_count': 0,
 'video_duration': 0.0,
 'title': '',
 'resources': []}

```

Facebook Search:
``` python
>>> place = cl.fbsearch_places('Perch')[2]
>>> place.dict()
{
 'pk': 3824034,
 'name': 'Perch',
 'phone': '',
 'website': '',
 'category': '',
 'hours': {},
 'address': None,
 'city': None,
 'zip': None,
 'lng': -118.25135,
 'lat': 34.04882,
 'external_id': 207298912632228,
 'external_id_source': 'facebook_places'
}

>>> cl.location_info(place.pk).dict()
{
 'pk': 3824034,
 'name': 'Perch',
 'phone': '(213) 802-1770',
 'website': 'http://www.perchla.com',
 'category': '',
 'hours': {},
 'address': '448 S Hill St',
 'city': 'Los Angeles, California',
 'zip': '90013',
 'lng': -118.25135,
 'lat': 34.04882,
 'external_id': None,
 'external_id_source': None
}
```

``` python
>>> place = cl.fbsearch_places("Villa Sirot", 46.7032028502, 4.3093986902)[0]
>>> place.dict()
{'pk': 1001956449,
 'name': 'Villa Sirot',
 'phone': '',
 'website': '',
 'category': '',
 'hours': {},
 'address': None,
 'city': None,
 'zip': None,
 'lng': 4.3093986902426,
 'lat': 46.703202850229,
 'external_id': 165573396905197,
 'external_id_source': 'facebook_places'}

>>> cl.location_info(place.pk).dict()
{'pk': 1001956449,
 'name': 'Villa Sirot',
 'phone': '',
 'website': None,
 'category': 'Local Business',
 'hours': {'status': '',
  'current_status': '',
  'hours_today': '',
  'schedule': []},
 'address': None,
 'city': None,
 'zip': None,
 'lng': None,
 'lat': None,
 'external_id': 165573396905197,
 'external_id_source': None}

```

Low level methods:

| Method                                         | Return  | Description
| ---------------------------------------------- | ------- | --------------------------------------------
| location_info_a1(location_pk: int) | Location | Get a location using location pk (Public Web API)
| location_info_v1(location_pk: int) | Location | Get a location using location pk (Private Mobile API)
| location_medias_a1_chunk(location_pk: int, max_amount: int = 24, sleep: float = 0.5, tab_key: str = "edge_location_to_top_posts\|edge_location_to_media", max_id: str = None) | Tuple[List[Media], str] | Get chunk of medias and end_cursor (Public Web API)
| location_medias_a1(location_pk: int, amount: int = 24, sleep: float = 0.5, tab_key: str = "edge_location_to_top_posts\|edge_location_to_media") | List[Media] | Get medias for a location (Public Web API)
| location_medias_v1_chunk(location_pk: int, max_amount: int = 63, tab_key: str = "ranked\|recent", max_id: str = None) | Tuple[List[Media], str] Get chunk of medias for a location and max_id (cursor) by Private Mobile API
| location_medias_v1(location_pk: int, amount: int = 63, tab_key: str = "ranked\|recent") | List[Media] | Get medias for a location (Private Mobile API)
| location_medias_top_a1(location_pk: int, amount: int = 9, sleep: float = 0.5) | List[Media] | Get top medias for a location (Public Web API)
| location_medias_top_v1(location_pk: int, amount: int = 21) | List[Media] | Get top medias for a location (Private Mobile API)
| location_medias_recent_a1(location_pk: int, amount: int = 24, sleep: float = 0.5) | List[Media] | Get recent medias for a location (Public Web API)
| location_medias_recent_v1(location_pk: int, amount: int = 63) | List[Media] | Get recent medias for a location (Private Mobile API)



================================================
FILE: docs/usage-guide/media.md
================================================
# Media

Viewing, downloading, uploading and editing publications

In terms of Instagram, this is called Media, usually users call it publications or posts

### Basic terms:

* `media_id` - String ID `"{media_id}_{user_id}"`, e.g. `"2277033926878261772_1903424587"`
* `media_pk` - Integer ID (real media id), e.g. `2277033926878261772`
* `code` - Short code (slug for media), e.g. `BjNLpA1AhXM` from `"https://www.instagram.com/p/BjNLpA1AhXM/"`
* `url` - URL to media publication, e.g. `"https://www.instagram.com/p/BjNLpA1AhXM/"`

### Media types:

* `Photo` - When media_type=1
* `Video` - When media_type=2 and product_type=feed
* `IGTV`  - When media_type=2 and product_type=igtv
* `Reel`  - When media_type=2 and product_type=clips
* `Album` - When media_type=8

## Viewing and editing publication

| Method                                                          | Return             | Description
| --------------------------------------------------------------- | ------------------ | --------------------------------------------
| media_id(media_pk: int)                                         | str                | Return media_id by media_pk (e.g. 2277033926878261772 -> 2277033926878261772_1903424587)
| media_pk(media_id: str)                                         | int                | Return media_pk by media_id (e.g. 2277033926878261772_1903424587 -> 2277033926878261772)
| media_pk_from_code(code: str)                                   | int                | Return media_pk
| media_pk_from_url(url: str)                                     | int                | Return media_pk
| user_medias(user_id: str, amount: int = 20)                     | List\[Media]       | Get list of medias by user_id
| user_medias_paginated(user_id: str, amount: int = 0, end_cursor: str = "")           | Tuple\[List\[Media], str] | Get one page of medias by user_id
| user_clips(user_id: str, amount: int = 50)                      | List\[Media]       | Get list of clips (reels) by user_id
| usertag_medias(user_id: str, amount: int = 20)                  | List\[Media]       | Get medias where a user is tagged
| media_info(media_pk: int)                                       | Media              | Return media info
| media_delete(media_pk: int)                                     | bool               | Delete media
| media_edit(media_pk: int, caption: str, title: str, usertags: List[Usertag], location: Location) | dict | Change caption for media
| media_user(media_pk: int)                                       | User | Get user info for media
| media_oembed(url: str)                                          | MediaOembed        | Return short media info by media URL
| media_like(media_id: str)                                       | bool               | Like media
| media_unlike(media_id: str)                                     | bool               | Unlike media
| media_seen(media_ids: List[str], skipped_media_ids: List[str])  | bool               | Mark a media as seen
| media_likers(media_id: str)                                     | List\[UserShort]   | Return list of users who liked this post (due to Instagram limitations, this may not return a complete list)
| media_archive(media_id: str)                                    | bool               | Archive a media
| media_unarchive(media_id: str)                                  | bool               | Unarchive a media
| media_pin(media_id: str)                                        | bool               | Pin a media to user profile
| media_unpin(media_id: str)                                      | bool               | Unpin a media to user profile

Low level methods:

| Method                                                          | Return       | Description
| --------------------------------------------------------------- | ------------ | --------------------------------------------
| media_info_a1(media_pk: int, max_id: str = None)                | Media        | Get Media from PK by Public Web API
| media_info_gql(media_pk: int)                                   | Media        | Get Media from PK by Public Graphql API
| media_info_v1(media_pk: int)                                    | Media        | Get Media from PK by Private Mobile API
| user_medias_gql(user_id: str, amount: int = 50, sleep: int = 2) | List\[Media] | Get a user's media by Public Graphql API
| user_medias_paginated_gql(user_id: str, amount: int = 50, sleep: int = 2, end_cursor=None) | Tuple\[List\[Media], str] | Get a page of user's media by Public Graphql API
| user_medias_v1(user_id: str, amount: int = 18)                  | List\[Media] | Get a user's media by Private Mobile API
| user_medias_paginated_v1(user_id: str, amount: int = 0, end_cursor="") | Tuple\[List\[Media], str] | Get a page of user's media by Private Mobile API
| user_clips_v1(user_id: str, amount: int = 50)                  | List\[Media] | Get a user's clip by Private Mobile API
| user_clips_paginated_v1(user_id: str, amount: int = 50, end_cursor="") | Tuple\[List\[Media], str] | Get a page of user's clip by Private Mobile API
| user_videos_v1(user_id: str, amount: int = 50)                  | List\[Media] | Get a user's video by Private Mobile API
| user_videos_paginated_v1(ser_id: int, amount: int = 50, end_cursor="") | Tuple\[List\[Media], str] | Get a page of user's video by Private Mobile API
| usertag_medias_gql(user_id: str, amount: int = 20)              | List\[Media] | Get medias where a user is tagged by Public Graphql API
| usertag_medias_v1(user_id: str, amount: int = 20)               | List\[Media] | Get medias where a user is tagged by Private Mobile API

### Example:

``` python
>>> from instagrapi import Client
>>> cl = Client()
>>> cl.login(USERNAME, PASSWORD)

>>> cl.media_pk_from_code("B-fKL9qpeab")
2278584739065882267

>>> cl.media_pk_from_code("B8jnuB2HAbyc0q001y3F9CHRSoqEljK_dgkJjo0")
2243811726252050162

>>> cl.media_pk_from_url("https://www.instagram.com/p/BjNLpA1AhXM/")
1787135824035452364

>>> cl.media_info(1787135824035452364).dict()
{'pk': 1787135824035452364,
 'id': '1787135824035452364_1903424587',
 'code': 'BjNLpA1AhXM',
 'taken_at': datetime.datetime(2018, 5, 25, 15, 46, 53, tzinfo=datetime.timezone.utc),
 'media_type': 8,
 'product_type': '',
 'thumbnail_url': None,
 'location': {'pk': 260916528,
  'name': 'Foros, Crimea',
  'address': '',
  'lng': 33.7878,
  'lat': 44.3914,
  'external_id': 181364832764479,
  'external_id_source': 'facebook_places'},
 'user': {'pk': 1903424587,
  'username': 'example',
  'full_name': 'Example Example',
  'profile_pic_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t51.2885-19/s150x150/123884060_...&oe=5FD7600E')},
 'comment_count': 0,
 'like_count': 48,
 'caption_text': '@mind__flowers в Форосе под дождём, 24 мая 2018 #downhill #skateboarding #downhillskateboarding #crimea #foros',
 'usertags': [],
 'video_url': None,
 'view_count': 0,
 'video_duration': 0.0,
 'title': '',
 'resources': [{'pk': 1787135361353462176,
   'video_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t50.2886-16/33464086_3755...0e2362', scheme='https', ...),
   'thumbnail_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t51.2885-15/e35/3220311...AE7332', scheme='https', ...),
   'media_type': 2},
  {'pk': 1787135762219834098,
   'video_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t50.2886-16/32895...61320_n.mp4', scheme='https', ...),
   'thumbnail_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t51.2885-15/e35/3373413....8480_n.jpg', scheme='https', ...),
   'media_type': 2},
  {'pk': 1787133803186894424,
   'video_url': None,
   'thumbnail_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t51.2885-15/e35/324307712_n.jpg...', scheme='https', ...),
   'media_type': 1}]}

>>> cl.media_oembed("https://www.instagram.com/p/B3mr1-OlWMG/").dict()
{'version': '1.0',
 'title': 'В гостях у ДК @delai_krasivo_kaifui',
 'author_name': 'example',
 'author_url': 'https://www.instagram.com/example',
 'author_id': 1903424587,
 'media_id': '2154602296692269830_1903424587',
 'provider_name': 'Instagram',
 'provider_url': 'https://www.instagram.com',
 'type': 'rich',
 'width': 658,
 'height': None,
 'html': '<blockquote>...',
 'thumbnail_url': 'https://instagram.frix7-1.fna.fbcdn.net/v...0655800983_n.jpg',
 'thumbnail_width': 640,
 'thumbnail_height': 480,
 'can_view': True}


>>> cl.media_archive('2155832952940083788_1903424587')
True

>>> cl.media_unarchive('2155832952940083788_1903424587')
True

>>> cl.user_medias_gql(1903424587, amount=1)[0].dict()
{'pk': 2592252466151482347,
 'id': '2592252466151482347_1903424587',
 'code': 'CP5h-I1FuPr',
 'taken_at': datetime.datetime(2021, 6, 9, 12, 9, 56, tzinfo=datetime.timezone.utc),
 'media_type': 8,
 'product_type': '',
 'thumbnail_url': None,
 'location': None,
 'user': {'pk': 1903424587,
  'username': 'example',
  'full_name': '',
  'profile_pic_url': None,
  'profile_pic_url_hd': None,
  'stories': []},
 'comment_count': 5,
 'like_count': 63,
 'has_liked': None,
 'caption_text': 'Любимые подвески ♥️ @daewon1song @tensortrucks',
 'usertags': [{'user': {'pk': 53860445,
    'username': 'tensortrucks',
    'full_name': '',
    'profile_pic_url': None,
    'profile_pic_url_hd': None,
    'stories': []},
   'x': 0.3146666667,
   'y': 0.368159204}],
 'video_url': None,
 'view_count': 0,
 'video_duration': 0.0,
 'title': '',
 'resources': [{'pk': 2592252463089480898,
   'video_url': None,
   'thumbnail_url': HttpUrl('https://instagram.fhel5-1.fna.fbcdn.net/v/t51.2885-15/e35/s1080x1080/198404255_317668533141074_749682826672118306_n.jpg?_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=f8FR-bZNbp8AX-A6YQ4&edm=APU89FABAAAA&ccb=7-4&oh=864bb145a4fa7e523f5cc22f9ac5d015&oe=61145E4F&_nc_sid=86f79a', scheme='https', host='instagram.fhel5-1.fna.fbcdn.net', tld='net', host_type='domain', path='/v/t51.2885-15/e35/s1080x1080/198404255_317668533141074_749682826672118306_n.jpg', query='_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=f8FR-bZNbp8AX-A6YQ4&edm=APU89FABAAAA&ccb=7-4&oh=864bb145a4fa7e523f5cc22f9ac5d015&oe=61145E4F&_nc_sid=86f79a'),
   'media_type': 1},
  {'pk': 2592252463081081550,
   'video_url': None,
   'thumbnail_url': HttpUrl('https://instagram.fhel5-1.fna.fbcdn.net/v/t51.2885-15/e35/s1080x1080/198228498_303261361473979_3031095263106513772_n.jpg?_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_cat=107&_nc_ohc=C9SeKrAO6poAX-nXhCG&edm=APU89FABAAAA&ccb=7-4&oh=6aab825e12fef746449be22c322762a1&oe=61132FB0&_nc_sid=86f79a', scheme='https', host='instagram.fhel5-1.fna.fbcdn.net', tld='net', host_type='domain', path='/v/t51.2885-15/e35/s1080x1080/198228498_303261361473979_3031095263106513772_n.jpg', query='_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_cat=107&_nc_ohc=C9SeKrAO6poAX-nXhCG&edm=APU89FABAAAA&ccb=7-4&oh=6aab825e12fef746449be22c322762a1&oe=61132FB0&_nc_sid=86f79a'),
   'media_type': 1},
  {'pk': 2592252463056089912,
   'video_url': None,
   'thumbnail_url': HttpUrl('https://instagram.fhel5-1.fna.fbcdn.net/v/t51.2885-15/e35/s1080x1080/199142152_323583732599636_4553823395468898634_n.jpg?_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_cat=108&_nc_ohc=_feIkorChpsAX_wzTff&edm=APU89FABAAAA&ccb=7-4&oh=a22a2f5b30772fbbb02db92b9394e981&oe=61147D59&_nc_sid=86f79a', scheme='https', host='instagram.fhel5-1.fna.fbcdn.net', tld='net', host_type='domain', path='/v/t51.2885-15/e35/s1080x1080/199142152_323583732599636_4553823395468898634_n.jpg', query='_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_cat=108&_nc_ohc=_feIkorChpsAX_wzTff&edm=APU89FABAAAA&ccb=7-4&oh=a22a2f5b30772fbbb02db92b9394e981&oe=61147D59&_nc_sid=86f79a'),
   'media_type': 1}]}

# Use paginated interface to resume fetch from stored cursor

>>> end_cursor = None
... for page in range(3):
...     medias, end_cursor = client.user_medias_paginated(1903424587, 5, end_cursor=end_cursor)
...     print([ m.taken_at.date().isoformat() for m in medias ])
...

['2021-06-09', '2019-10-16', '2019-10-14', '2019-06-13', '2019-06-06']
['2019-06-05', '2019-03-23', '2019-03-23', '2018-11-15', '2018-10-16']
['2018-10-16', '2018-10-11', '2018-10-09', '2018-10-09', '2018-08-02']

```

## Download media

| Method                                                       | Return  | Description                                                         |
| ------------------------------------------------------------ | ------- | ------------------------------------------------------------------- |
| photo_download(media_pk: int, folder: Path)                  | Path    | Download photo (path to photo with best resoluton)                  |
| photo_download_by_url(url: str, filename: str, folder: Path) | Path    | Download photo by URL (path to photo with best resoluton)           |
| video_download(media_pk: int, folder: Path)                  | Path    | Download video (path to video with best resoluton)                  |
| video_download_by_url(url: str, filename: str, folder: Path) | Path    | Download Video by URL (path to video with best resoluton)           |
| album_download(media_pk: int, folder: Path)                  | Path    | Download Album (multiple paths to photo/video with best resolutons) |
| album_download_by_urls(urls: List[str], folder: Path)        | Path    | Download Album by URLs (multiple paths to photo/video)              |
| igtv_download(media_pk: int, folder: Path)                   | Path    | Download IGTV (path to video with best resoluton)                   |
| igtv_download_by_url(url: str, filename: str, folder: Path)  | Path    | Download IGTV by URL (path to video with best resoluton)            |
| clip_download(media_pk: int, folder: Path)                   | Path    | Download Reels Clip (path to video with best resoluton)             |
| clip_download_by_url(url: str, filename: str, folder: Path)  | Path    | Download Reels Clip by URL (path to video with best resoluton)      |

### Example:

``` python

>>> from instagrapi import Client
>>> cl = Client()
>>> cl.login(USERNAME, PASSWORD)

>>> cl.media_pk_from_url("https://www.instagram.com/p/BqNQJleFoSJ/")
1913256444155036809

>>> video_url = cl.media_info(1913256444155036809).video_url
>>> cl.video_download_by_url(video_url, folder='/tmp')
PosixPath('/tmp/45588546_367538213983456_6830188946193737023_n.mp4')

```

``` python

>>> cl.media_pk_from_url("http://www.instagram.com/p/BjNLpA1AhXM/")
1787135824035452364

>>> cl.album_download(1787135824035452364)
[PosixPath('/app/example_1787135361353462176.mp4'),
 PosixPath('/app/example_1787135762219834098.mp4'),
 PosixPath('/app/example_1787133803186894424.jpg')]

```

## Upload media

Upload medias to your feed. Common arguments:

* `path` - Path to source file
* `caption`  - Text for you post
* `usertags` - List[Usertag] of mention users (see `Usertag` in [types.py](https://github.com/subzeroid/instagrapi/blob/master/instagrapi/types.py))
* `location` - Location (e.g. `Location(name='Test', lat=42.0, lng=42.0)`)

| Method                                                                                                                                 | Return  | Description
| -------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------
| photo_upload(path: Path, caption: str, upload_id: str, usertags: List[Usertag], location: Location, extra_data: Dict = {})             | Media   | Upload photo (Support JPG files)
| video_upload(path: Path, caption: str, thumbnail: Path, usertags: List[Usertag], location: Location, extra_data: Dict = {})            | Media   | Upload video (Support MP4 files)
| album_upload(paths: List[Path], caption: str, usertags: List[Usertag], location: Location, extra_data: Dict = {})                      | Media   | Upload Album (Support JPG/MP4 files)
| igtv_upload(path: Path, title: str, caption: str, thumbnail: Path, usertags: List[Usertag], location: Location, extra_data: Dict = {}) | Media   | Upload IGTV (Support MP4 files)
| clip_upload(path: Path, caption: str, thumbnail: Path, usertags: List[Usertag], location: Location, extra_data: Dict = {})             | Media   | Upload Reels Clip (Support MP4 files)
| clip_upload_as_reel_with_music(path: Path, caption: str, track: Track, extra_data: Dict = {}) | Media | Upload Reels Clip as reel with music metadata


In `extra_data`, you can pass additional media settings, for example:

| Method                        | Type   | Description
| ----------------------------- | ------ | ------------------
| custom_accessibility_caption  | String | [Set alternative text](https://github.com/subzeroid/instagrapi/issues/351) `{"custom_accessibility_caption": "ALT TEXT HERE"}`
| like_and_view_counts_disabled | Int    | [Disable like and view counts](https://github.com/subzeroid/instagrapi/issues/382) `{"like_and_view_counts_disabled": 1}`
| disable_comments              | Int    | Disable comments `{"disable_comments": 1}`
| invite_coauthor_user_id       | Int    | Add a coauthor to the post `{"invite_coauthor_user_id": "USER ID OF COAUTHOR HERE"}`. You also need to add this user to `usertags`

### Example:

``` python
>>> from instagrapi import Client

>>> cl = Client()
>>> cl.login(USERNAME, PASSWORD)

>>> media = cl.photo_upload(
    "/app/image.jpg",
    "Test caption for photo with #hashtags and mention users such @example",
    extra_data={
        "custom_accessibility_caption": "alt text example",
        "like_and_view_counts_disabled": 1,
        "disable_comments": 1,
    }
)

>>> media.dict()
{'pk': 2573347427873726764,
 'id': '2573347427873726764_1903424587',
 'code': 'CO2Xdn6FCEs',
 'taken_at': datetime.datetime(2021, 5, 14, 10, 9, tzinfo=datetime.timezone.utc),
 'media_type': 1,
 'product_type': 'feed',
 'thumbnail_url': HttpUrl('https://instagram.fhel5-1.fna.fbcdn.net/v/t51.2885-15/e35/185486538_463522984736407_6315244509641560230_n.jpg?se=8&tp=1&_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_cat=107&_nc_ohc=6tBMsh9HlmMAX9zI_jc&edm=ACqnv0EBAAAA&ccb=7-4&oh=2b46f1e9fbd2416eb7d08b398e0f639e&oe=60C30437&_nc_sid=9ec724&ig_cache_key=MjU3MzM0NzQyNzg3MzcyNjc2NA%3D%3D.2-ccb7-4', scheme='https', host='instagram.fhel5-1.fna.fbcdn.net', tld='net', host_type='domain', path='/v/t51.2885-15/e35/185486538_463522984736407_6315244509641560230_n.jpg', query='se=8&tp=1&_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_cat=107&_nc_ohc=6tBMsh9HlmMAX9zI_jc&edm=ACqnv0EBAAAA&ccb=7-4&oh=2b46f1e9fbd2416eb7d08b398e0f639e&oe=60C30437&_nc_sid=9ec724&ig_cache_key=MjU3MzM0NzQyNzg3MzcyNjc2NA%3D%3D.2-ccb7-4'),
 'location': None,
 'user': {'pk': 1903424587,
  'username': 'example',
  'full_name': 'Example Example',
  'profile_pic_url': HttpUrl('https://instagram.fhel5-1.fna.fbcdn.net/v/t51.2885-19/s150x150/156689363_269505058076642_6448820957073669709_n.jpg?tp=1&_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_ohc=EtzrL0pAdg8AX-Xq8yS&edm=ACqnv0EBAAAA&ccb=7-4&oh=e2fd6a9d362f8587ea8123f23b248f1b&oe=60C2CB91&_nc_sid=9ec724', scheme='https', host='instagram.fhel5-1.fna.fbcdn.net', tld='net', host_type='domain', path='/v/t51.2885-19/s150x150/156689363_269505058076642_6448820957073669709_n.jpg', query='tp=1&_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_ohc=EtzrL0pAdg8AX-Xq8yS&edm=ACqnv0EBAAAA&ccb=7-4&oh=e2fd6a9d362f8587ea8123f23b248f1b&oe=60C2CB91&_nc_sid=9ec724'),
  'stories': []},
 'comment_count': 0,
 'like_count': 0,
 'has_liked': None,
 'caption_text': 'Test caption for photo with #hashtags and mention users such @example',
 'usertags': [],
 'video_url': None,
 'view_count': 0,
 'video_duration': 0.0,
 'title': '',
 'resources': []}
```

Now let's mention users (Usertag) and location:

``` python
>>> from instagrapi import Client
>>> from instagrapi.types import Usertag, Location

>>> cl = Client()
>>> cl.login(USERNAME, PASSWORD)

>>> example = cl.user_info_by_username('example')
>>> media = cl.photo_upload(
    "/app/image.jpg",
    "Test caption for photo with #hashtags and mention users such @example",
    usertags=[Usertag(user=example, x=0.5, y=0.5)],
    location=Location(name='Russia, Saint-Petersburg', lat=59.96, lng=30.29)
)

>>> media.dict()
{'pk': 2573355619819242434,
 'id': '2573355619819242434_1903424587',
 'code': 'CO2ZU1QFMPC',
 'taken_at': datetime.datetime(2021, 5, 14, 10, 25, 16, tzinfo=datetime.timezone.utc),
 'media_type': 1,
 'product_type': 'feed',
 'thumbnail_url': HttpUrl('https://instagram.fhel5-1.fna.fbcdn.net/v/t51.2885-15/e35/185426950_474602463640866_4228057388625412955_n.jpg?se=8&tp=1&_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_cat=106&_nc_ohc=7NrVvAEG7f4AX_XPaOK&edm=ACqnv0EBAAAA&ccb=7-4&oh=bd2c90c2dcb693184e07c2777e09bb0b&oe=60C4E326&_nc_sid=9ec724&ig_cache_key=MjU3MzM1NTYxOTgxOTI0MjQzNA%3D%3D.2-ccb7-4', scheme='https', host='instagram.fhel5-1.fna.fbcdn.net', tld='net', host_type='domain', path='/v/t51.2885-15/e35/185426950_474602463640866_4228057388625412955_n.jpg', query='se=8&tp=1&_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_cat=106&_nc_ohc=7NrVvAEG7f4AX_XPaOK&edm=ACqnv0EBAAAA&ccb=7-4&oh=bd2c90c2dcb693184e07c2777e09bb0b&oe=60C4E326&_nc_sid=9ec724&ig_cache_key=MjU3MzM1NTYxOTgxOTI0MjQzNA%3D%3D.2-ccb7-4'),
 'location': {'pk': 107617247320879,
  'name': 'Russia, Saint-Petersburg',
  'address': 'Russia, Saint-Petersburg',
  'lng': 30.30605,
  'lat': 59.93318,
  'external_id': 107617247320879,
  'external_id_source': 'facebook_places'},
 'user': {'pk': 1903424587,
  'username': 'example',
  'full_name': 'Example Example',
  'profile_pic_url': HttpUrl('https://instagram.fhel5-1.fna.fbcdn.net/v/t51.2885-19/s150x150/156689363_269505058076642_6448820957073669709_n.jpg?tp=1&_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_ohc=EtzrL0pAdg8AX-Xq8yS&edm=ACqnv0EBAAAA&ccb=7-4&oh=e2fd6a9d362f8587ea8123f23b248f1b&oe=60C2CB91&_nc_sid=9ec724', scheme='https', host='instagram.fhel5-1.fna.fbcdn.net', tld='net', host_type='domain', path='/v/t51.2885-19/s150x150/156689363_269505058076642_6448820957073669709_n.jpg', query='tp=1&_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_ohc=EtzrL0pAdg8AX-Xq8yS&edm=ACqnv0EBAAAA&ccb=7-4&oh=e2fd6a9d362f8587ea8123f23b248f1b&oe=60C2CB91&_nc_sid=9ec724'),
  'stories': []},
 'comment_count': 0,
 'like_count': 0,
 'has_liked': None,
 'caption_text': 'Test caption for photo with #hashtags and mention users such @example',
 'usertags': [{'user': {'pk': 1903424587,
    'username': 'example',
    'full_name': 'Example Example',
    'profile_pic_url': HttpUrl('https://instagram.fhel5-1.fna.fbcdn.net/v/t51.2885-19/s150x150/156689363_269505058076642_6448820957073669709_n.jpg?tp=1&_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_ohc=EtzrL0pAdg8AX-Xq8yS&edm=ACqnv0EBAAAA&ccb=7-4&oh=e2fd6a9d362f8587ea8123f23b248f1b&oe=60C2CB91&_nc_sid=9ec724', scheme='https', host='instagram.fhel5-1.fna.fbcdn.net', tld='net', host_type='domain', path='/v/t51.2885-19/s150x150/156689363_269505058076642_6448820957073669709_n.jpg', query='tp=1&_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_ohc=EtzrL0pAdg8AX-Xq8yS&edm=ACqnv0EBAAAA&ccb=7-4&oh=e2fd6a9d362f8587ea8123f23b248f1b&oe=60C2CB91&_nc_sid=9ec724'),
    'stories': []},
   'x': 0.5,
   'y': 0.5}],
 'video_url': None,
 'view_count': 0,
 'video_duration': 0.0,
 'title': '',
 'resources': []}
```

Reels:

```python
>>> clips = cl.user_clips_v1(25025320, amount=2)
>>> clips[0].dict()

{'pk': '3052048407587698594',
 'id': '3052048407587698594_25025320',
 'code': 'CpbDdszj7ei',
 'taken_at': datetime.datetime(2023, 3, 5, 21, 50, 4, tzinfo=datetime.timezone.utc),
 'media_type': 2,
 'product_type': 'clips',
 'thumbnail_url': HttpUrl('https://scontent-den4-1.cdninstagram.com/v/t51.2885-15/333966975_152901010970043_8971338145148712917_n.jpg?stp=dst-jpg_e15_p150x150&_nc_ht=scontent-den4-1.cdninstagram.com&_nc_cat=1&_nc_ohc=rRuJ7u4YrqEAX-UEMFq&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=MzA1MjA0ODQwNzU4NzY5ODU5NA%3D%3D.2-ccb7-5&oh=00_AfC_tNEWVjJLM5RQYUiQJFHQZSmvnDtAcpzs42DRSYt1pQ&oe=6409C451&_nc_sid=4a9e64', scheme='https', host='scontent-den4-1.cdninstagram.com', tld='com', host_type='domain', port='443', path='/v/t51.2885-15/333966975_152901010970043_8971338145148712917_n.jpg', query='stp=dst-jpg_e15_p150x150&_nc_ht=scontent-den4-1.cdninstagram.com&_nc_cat=1&_nc_ohc=rRuJ7u4YrqEAX-UEMFq&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=MzA1MjA0ODQwNzU4NzY5ODU5NA%3D%3D.2-ccb7-5&oh=00_AfC_tNEWVjJLM5RQYUiQJFHQZSmvnDtAcpzs42DRSYt1pQ&oe=6409C451&_nc_sid=4a9e64'),
 'location': {'pk': 213011753,
  'name': 'Sydney, Australia',
  'phone': '',
  'website': '',
  'category': '',
  'hours': {},
  'address': '',
  'city': '',
  'zip': None,
  'lng': 151.20797,
  'lat': -33.86751,
  'external_id': 110884905606108,
  'external_id_source': 'facebook_places'},
....
}
```



================================================
FILE: docs/usage-guide/notes.md
================================================
# Notes *WIP*

| Method                      | Return            | Description                     |
| --------------------------- | ----------------- | ------------------------------- |
| get_notes()                 | List[Note]        | Retrieve direct Notes           |
| create_note(text: str, audience: int = 0) | Note | Post a new Note                 |
| delete_note(note_id: int)   | bool              | Delete a posted Note            |
| update_last_seen_note()     | bool              | Update the last seen time |

Example:

``` python
>>> note = cl.create_note("Hello from Instagrapi, everyone can see it!", 0)
>>> print(note.dict())
{'id': '17849203563031468', 
'text': 'Hello from Instagrapi, everyone can see it!', 
'user_id': 12312312312, 
'user': {
  'pk': '12312312312', 
  'username': 'something', 
  'full_name': 'merimi on top', 
  'profile_pic_url': HttpUrl('https://scontent-dus1-1.cdninstagram.com/v/t51.2885-19/364347953_6289474204435297_7603222331512295081_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent-dus1-1.cdninstagram.com&_nc_cat=101&_nc_ohc=DVaE0MQwn0YAX8-S8dm&edm=AE-H4JwBAAAA&ccb=7-5&oh=00_AfAnH4mHGMl7B5tqzU7b9PMz9qSC4QE_-EX067lwPHnN1w&oe=64DDA1CB&_nc_sid=cff473', ), 
  'profile_pic_url_hd': None, 
  'is_private': False, 
  'stories': []}, 
'audience': 0, 
'created_at': datetime.datetime(2023, 8, 13, 14, 33, 43, tzinfo=datetime.timezone.utc),
'expires_at': datetime.datetime(2023, 8, 14, 14, 33, 43, tzinfo=datetime.timezone.utc), 
'is_emoji_only': False, 
'has_translation': False, 
'note_style': 0}
>>> notes = cl.get_notes()
>>> print(notes)
[Note(id='17849203563031468', text='Hello from Instagrapi, everyone can see it!', ..., has_translation=False, note_style=0), Note(id='17902958207826742', text='Am so happy 💃💃💃💃🙈🤭', ..., has_translation=False, note_style=0)]

>>> cl.last_seen_update_note()

>>> cl.delete_note(note.id)
```

## Get Notes  |  Post Notes  |  Delete Notes
- *Get Notes from Direct*
- *Publish a new note with the ability to select an audience*
- *Delete posted Notes*
- *Update last seen of Notes*

The note should not exceed 60 characters. The rate in between Notes requests should be fairly high *(*i.e : 1 request/ 2 min)* to avoid triggering Instagram API

Common arguments:

* `note_id` - ID of the Note object
* `text` - Content of the Note 
* `audience` - Who can see the note **(0 = Followers you follow back, 1 = Close Friends only)**



================================================
FILE: docs/usage-guide/story.md
================================================
# Story

| Method                                                                 | Return          | Description
| ---------------------------------------------------------------------- | --------------- | ----------------------------------
| user_stories(user_id: str, amount: int = None)                         | List[Story]     | Get list of stories by user_id
| story_info(story_pk: int, use_cache: bool = True)                      | Story           | Return story info
| story_delete(story_pk: int)                                            | bool            | Delete story
| story_seen(story_pks: List[int], skipped_story_pks: List[int])         | bool            | Mark a story as seen
| story_pk_from_url(url: str)                                            | int             | Get Story (media) PK from URL
| story_download(story_pk: int, filename: str = "", folder: Path = "")   | Path            | Download story media by media_type
| story_download_by_url(url: str, filename: str = "", folder: Path = "") | Path            | Download story media using URL to file (mp4 or jpg)
| story_viewers(story_pk: int, amount: int = 20)                         | List[UserShort] | List of story viewers (via Private API)
| story_like(story_id: str, revert: bool = False)                        | bool            | Like a story
| story_unlike(story_id: str)                                            | bool            | Unlike a story

Example:

``` python
>>> cl.story_download(cl.story_pk_from_url('https://www.instagram.com/stories/example/2581281926631793076/'))
PosixPath('/app/189361307_229642088942817_9180243596650100310_n.mp4')

>>> s = cl.story_info(2581281926631793076)

>>> cl.story_download_by_url(s.video_url)  # url to mp4 file
PosixPath('/app/189361307_229642088942817_9180243596650100310_n.mp4')

>>> cl.story_download_by_url(s.thumbnail_url)  # URL to jpg file
PosixPath('/app/191260083_2908005872746895_8988438451809588865_n.jpg')
```

## Upload Stories

Upload medias to your stories.

The story file should be at 9:16 resolution (e.g. 720x1280).
If you have a different resolution, then you need to prepare a file or use the StoryBuilder, which is written about below.

Common arguments:

* `path` - Path to media file
* `caption` - Caption for story (now use to fetch mentions)
* `thumbnail` - Thumbnail instead capture from source file
* `mentions` - Tag profiles in story
* `locations` - Add locations to story
* `links` - "Swipe Up" links (now use first)
* `hashtags` - Add hashtags to story
* `stickers` - Add stickers to story
* `polls` - Add polls to story

| Method                               | Return   | Description
| ------------------------------------ | -------- | -------------
| photo_upload_to_story(path: Path, caption: str, upload_id: str, mentions: List[Usertag], locations: List[StoryLocation], links: List[StoryLink], hashtags: List[StoryHashtag], stickers: List[StorySticker], polls: List[StoryPoll], extra_data: Dict[str, str] = {})  | Story  | Upload photo (Support JPG files)
| video_upload_to_story(path: Path, caption: str, thumbnail: Path, mentions: List[Usertag], locations: List[StoryLocation], links: List[StoryLink], hashtags: List[StoryHashtag], stickers: List[StorySticker], polls: List[StoryPoll], extra_data: Dict[str, str] = {}) | Story  | Upload video (Support MP4 files)

In `extra_data`, you can pass additional story settings, for example:

| Method            | Type   | Description
| ----------------- | ------ | ------------------
| audience          | String | [Publish story for close friends](https://github.com/subzeroid/instagrapi/issues/1210) `{"audience": "besties"}`


Examples:

``` python
from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag

cl = Client()
cl.login(USERNAME, PASSWORD)

media_pk = cl.media_pk_from_url('https://www.instagram.com/p/CGgDsi7JQdS/')
media_path = cl.video_download(media_pk)
example = cl.user_info_by_username('example')
hashtag = cl.hashtag_info('dhbastards')

cl.video_upload_to_story(
    media_path,
    "Credits @example",
    mentions=[StoryMention(user=example, x=0.49892962, y=0.703125, width=0.8333333333333334, height=0.125)],
    links=[StoryLink(webUri='https://github.com/subzeroid/instagrapi')],
    hashtags=[StoryHashtag(hashtag=hashtag, x=0.23, y=0.32, width=0.5, height=0.22)],
    medias=[StoryMedia(media_pk=media_pk, x=0.5, y=0.5, width=0.6, height=0.8)],
    polls=[StoryPoll(x = 0.5, y = 0.5, width = 0.7, height = 0.5, question = "Question", options = ["Option 1", "Option 2", "Option 3"])],
)
```

## Build Story to Upload

If you want to format your story correctly (correct resolution, user mentions, etc) use StoryBuilder:

| Method                                                | Return     | Description                              |
| ----------------------------------------------------- | ---------- | ---------------------------------------- |
| StoryBuilder.build_clip(clip: moviepy.Clip, max_duration: int = 0) | StoryBuild | Build CompositeVideoClip with background and mentioned users. Return MP4 file and mentions with coordinates |
| StoryBuilder.video(max_duration: int = 0)            | StoryBuild | Call build_clip(VideoClip, max_duration) |
| StoryBuilder.photo(max_duration: int = 0)            | StoryBuild | Call build_clip(ImageClip, max_duration) |

Example:

``` python
from instagrapi.types import StoryMention, StoryMedia, StoryLink
from instagrapi.story import StoryBuilder

media_pk = cl.media_pk_from_url('https://www.instagram.com/p/CGgDsi7JQdS/')
media_path = cl.video_download(media_pk)
example = cl.user_info_by_username('example')

buildout = StoryBuilder(
    media_path,
    'Credits @example',
    [StoryMention(user=example)],
    Path('/path/to/background_720x1280.jpg')
).video(15)  # seconds

cl.video_upload_to_story(
    buildout.path,
    "Credits @example",
    mentions=buildout.mentions,
    links=[StoryLink(webUri='https://github.com/subzeroid/instagrapi')],
    medias=[StoryMedia(media_pk=media_pk)]
)
```

Result:

![](https://raw.githubusercontent.com/example/instagrapi/master/examples/dhb.gif)

Photo upload:

``` python
cl.photo_upload_to_story('/app/image.jpg')
```

Upload photo as video:

``` python
buildout = StoryBuilder('/app/image.jpg').photo()
cl.video_upload_to_story(buildout.path)
```

Like & unlike story:

```python
pk = cl.story_pk_from_url("https://instagram.com/stories/purely.anand/2884886531427631361/")
info = cl.story_info(pk).dict()

cl.story_like(info['id']) # To like story
cl.story_unlike(info['id']) # To unlike story

# another way to unlike story
cl.story_like(info['id'], revert=True)
```

More stories here [https://www.instagram.com/wrclive/](https://www.instagram.com/wrclive/)



================================================
FILE: docs/usage-guide/totp.md
================================================
# TOTP

TOTP setup and code generation

| Method                              | Return    | Description
| ----------------------------------- | --------- | ----------------------------------------------------------
| totp_generate_seed()                | str       | Generate 2FA TOTP seed
| totp_enable(verification_code: str) | List[str] | Enable TOTP 2FA (return backup keys, save it)
| totp_disable()                      | bool      | Disable TOTP 2FA
| totp_generate_code(seed: str)       | str       | Generate 2FA TOTP code (you can use it instead of Google Authenticator)


Example:

``` python
>>> from instagrapi import Client
>>> cl = Client()
>>> cl.login(USERNAME, PASSWORD)

>>> seed = cl.totp_generate_seed()
"67EIYPWCIJDTTVX632NEODKEU2PY5BIW"

>>> code = cl.totp_generate_code(seed)
"123456"

>>> cl.totp_enable(code)
["1234 5678", "1234 5678", "1234 5678", "1234 5678", "1234 5678"]

>>> cl.totp_disable()
True
```



================================================
FILE: docs/usage-guide/track.md
================================================
# Track

Viewing and downloading tracks

| Method                                                                 | Return      | Description
| ---------------------------------------------------------------------- | ----------- | --------------------------------------------
| track_info_by_canonical_id(music_canonical_id: str)                    | Track       | Get Track by music_canonical_id
| track_download_by_url(url: str, filename: str = "", folder: Path = "") | Path        | Download track by URL
| search_music(query: str)                                               | List[Track] | Return list of tracks

### Example:

```python
>>> from instagrapi import Client
>>> cl = Client()
>>> cl.login(USERNAME, PASSWORD)

>>> [media.clips_metadata['music_canonical_id'] for media in cl.reels(amount=10)]

['18159860503036324',
 '18245182426110798',
 '18156435169051995',
 '18274086877034385',
 '18243482860109137',
 '18244791958105000',
 '18310451203035205',
 '18293984647065921',
 '18154598032011335',
 '18301950994013617']

>>> cl.track_info_by_canonical_id(18159860503036324).dict()
{
'id': '2398788493765573',
'title': 'A Little Bit Goes a Long Way',
'subtitle': '',
'display_artist': 'Yheti',
'audio_cluster_id': 1054108181594434,
'artist_id': None,
'cover_artwork_uri': None,
'cover_artwork_thumbnail_uri': None,
'progressive_download_url': None,
'fast_start_progressive_download_url': None,
'reactive_audio_download_url': None,
'highlight_start_times_in_ms': [38500],
'is_explicit': False,
'dash_manifest': '<?xml version="1.0" encoding="UTF-8"?>\n<!--Generated with https://github.com/google/shaka-packager version v1.6.0-release-->\n<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:cenc="urn:mpeg:cenc:2013" xsi:schemaLocation="urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd" profiles="urn:mpeg:dash:profile:isoff-on-demand:2011" minBufferTime="PT2S" type="static" mediaPresentationDuration="PT182.137S">\n  <Period id="0">\n    <AdaptationSet id="0" contentType="audio" subsegmentAlignment="true">\n      <Representation id="0" bandwidth="130017" codecs="mp4a.40.2" mimeType="audio/mp4" audioSamplingRate="48000">\n        <AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>\n        <BaseURL>https://scontent-cph2-1.xx.fbcdn.net/v/t39.12897-6/84846439_2484536748531420_3971102873273499648_n.m4a?_nc_cat=101&amp;ccb=1-7&amp;_nc_sid=02c1ff&amp;_nc_ohc=N6k7lDt_6TAAX_yKEoV&amp;_nc_ad=z-m&amp;_nc_cid=0&amp;_nc_ht=scontent-cph2-1.xx&amp;oh=00_AT9Cly5G-kzGxRceunBi8NUl5eFLEqwlMEJbWnxykUTO0Q&amp;oe=62DF3A6E</BaseURL>\n        <SegmentBase indexRange="741-1864" timescale="48000">\n          <Initialization range="0-740"/>\n        </SegmentBase>\n      </Representation>\n    </AdaptationSet>\n  </Period>\n</MPD>\n',
'uri': HttpUrl('https://scontent-cph2-1.xx.fbcdn.net/v/t39.12897-6/84846439_2484536748531420_3971102873273499648_n.m4a?_nc_cat=101&ccb=1-7&_nc_sid=02c1ff&_nc_ohc=N6k7lDt_6TAAX_yKEoV&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent-cph2-1.xx&oh=00_AT9Cly5G-kzGxRceunBi8NUl5eFLEqwlMEJbWnxykUTO0Q&oe=62DF3A6E', scheme='https', host='scontent-cph2-1.xx.fbcdn.net', tld='net', host_type='domain', port='443', path='/v/t39.12897-6/84846439_2484536748531420_3971102873273499648_n.m4a', query='_nc_cat=101&ccb=1-7&_nc_sid=02c1ff&_nc_ohc=N6k7lDt_6TAAX_yKEoV&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent-cph2-1.xx&oh=00_AT9Cly5G-kzGxRceunBi8NUl5eFLEqwlMEJbWnxykUTO0Q&oe=62DF3A6E'),
'has_lyrics': False,
'audio_asset_id': 2398788493765573,
'duration_in_ms': 182094,
'dark_message': None,
'allows_saving': True,
'territory_validity_periods': {}
}

>>> track_uri = cl.track_info_by_canonical_id(18159860503036324).uri
HttpUrl('https://scontent-cph2-1.xx.fbcdn.net/v/t39.12897-6/84846439_2484536748531420_3971102873273499648_n.m4a?_nc_cat=101&ccb=1-7&_nc_sid=02c1ff&_nc_ohc=N6k7lDt_6TAAX_yKEoV&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent-cph2-1.xx&oh=00_AT9Cly5G-kzGxRceunBi8NUl5eFLEqwlMEJbWnxykUTO0Q&oe=62DF3A6E', scheme='https', host='scontent-cph2-1.xx.fbcdn.net', tld='net', host_type='domain', port='443', path='/v/t39.12897-6/84846439_2484536748531420_3971102873273499648_n.m4a', query='_nc_cat=101&ccb=1-7&_nc_sid=02c1ff&_nc_ohc=N6k7lDt_6TAAX_yKEoV&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent-cph2-1.xx&oh=00_AT9Cly5G-kzGxRceunBi8NUl5eFLEqwlMEJbWnxykUTO0Q&oe=62DF3A6E')

>>> cl.track_download_by_url(track_uri, folder="/tmp")
PosixPath('/tmp/84846439_2484536748531420_3971102873273499648_n.m4a')

>>> cl.search_music("love")[0].dict()
{
'id': '354372829354341',
'title': 'Love Your Voice',
'subtitle': '',
'display_artist': 'JONY',
'audio_cluster_id': 410742646320351,
'artist_id': None,
'cover_artwork_uri': HttpUrl('https://cdn.fbsbx.com/v/t65.14500-21/191897578_1074647849725858_3973554110966662866_n.jpg?stp=cp0_dst-jpg_e15_p526x296_q65&_nc_cat=1&ccb=1-7&_nc_sid=cbead8&_nc_ohc=ugygksMclf4AX_u7L7g&_nc_ht=cdn.fbsbx.com&oh=00_AT89FBXl6h7Q6zytlI5cA4UIG_zQkK_DsOqyUqyXk1zyIg&oe=62DAEA82', scheme='https', host='cdn.fbsbx.com', tld='com', host_type='domain', port='443', path='/v/t65.14500-21/191897578_1074647849725858_3973554110966662866_n.jpg', query='stp=cp0_dst-jpg_e15_p526x296_q65&_nc_cat=1&ccb=1-7&_nc_sid=cbead8&_nc_ohc=ugygksMclf4AX_u7L7g&_nc_ht=cdn.fbsbx.com&oh=00_AT89FBXl6h7Q6zytlI5cA4UIG_zQkK_DsOqyUqyXk1zyIg&oe=62DAEA82'),
'cover_artwork_thumbnail_uri': HttpUrl('https://cdn.fbsbx.com/v/t65.14500-21/191897578_1074647849725858_3973554110966662866_n.jpg?stp=cp0_dst-jpg_e15_q65_s168x128&_nc_cat=1&ccb=1-7&_nc_sid=cbead8&_nc_ohc=ugygksMclf4AX_u7L7g&_nc_ht=cdn.fbsbx.com&oh=00_AT81eLXWBA5EaM20EhaMldwlyzKG1X1zA_nYNkYWf6c5cg&oe=62DAEA82', scheme='https', host='cdn.fbsbx.com', tld='com', host_type='domain', port='443', path='/v/t65.14500-21/191897578_1074647849725858_3973554110966662866_n.jpg', query='stp=cp0_dst-jpg_e15_q65_s168x128&_nc_cat=1&ccb=1-7&_nc_sid=cbead8&_nc_ohc=ugygksMclf4AX_u7L7g&_nc_ht=cdn.fbsbx.com&oh=00_AT81eLXWBA5EaM20EhaMldwlyzKG1X1zA_nYNkYWf6c5cg&oe=62DAEA82'),
'progressive_download_url': HttpUrl('https://scontent-cph2-1.xx.fbcdn.net/v/t39.12897-6/199073207_321615622853093_2366400633227710754_n.m4a?_nc_cat=1&ccb=1-7&_nc_sid=02c1ff&_nc_ohc=UxUNJHpsoy4AX-eA1Bm&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent-cph2-1.xx&oh=00_AT_IpjsOwgCikt0wNx1nS7FzEJE-1pKkzNZSXIpKCzkZhg&oe=62DE2CA8', scheme='https', host='scontent-cph2-1.xx.fbcdn.net', tld='net', host_type='domain', port='443', path='/v/t39.12897-6/199073207_321615622853093_2366400633227710754_n.m4a', query='_nc_cat=1&ccb=1-7&_nc_sid=02c1ff&_nc_ohc=UxUNJHpsoy4AX-eA1Bm&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent-cph2-1.xx&oh=00_AT_IpjsOwgCikt0wNx1nS7FzEJE-1pKkzNZSXIpKCzkZhg&oe=62DE2CA8'),
'fast_start_progressive_download_url': HttpUrl('https://scontent-cph2-1.xx.fbcdn.net/v/t39.12897-6/199073207_321615622853093_2366400633227710754_n.m4a?_nc_cat=1&ccb=1-7&_nc_sid=02c1ff&_nc_ohc=UxUNJHpsoy4AX-eA1Bm&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent-cph2-1.xx&oh=00_AT_IpjsOwgCikt0wNx1nS7FzEJE-1pKkzNZSXIpKCzkZhg&oe=62DE2CA8', scheme='https', host='scontent-cph2-1.xx.fbcdn.net', tld='net', host_type='domain', port='443', path='/v/t39.12897-6/199073207_321615622853093_2366400633227710754_n.m4a', query='_nc_cat=1&ccb=1-7&_nc_sid=02c1ff&_nc_ohc=UxUNJHpsoy4AX-eA1Bm&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent-cph2-1.xx&oh=00_AT_IpjsOwgCikt0wNx1nS7FzEJE-1pKkzNZSXIpKCzkZhg&oe=62DE2CA8'),
'reactive_audio_download_url': None,
'highlight_start_times_in_ms': [20000, 35500, 86500],
'is_explicit': False,
'dash_manifest': '<?xml version="1.0" encoding="UTF-8"?>\n<!--Generated with https://github.com/google/shaka-packager version v1.6.0-release-->\n<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:cenc="urn:mpeg:cenc:2013" xsi:schemaLocation="urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd" profiles="urn:mpeg:dash:profile:isoff-on-demand:2011" minBufferTime="PT2S" type="static" mediaPresentationDuration="PT150.372S">\n  <Period id="0">\n    <AdaptationSet id="0" contentType="audio" subsegmentAlignment="true">\n      <Representation id="0" bandwidth="130029" codecs="mp4a.40.2" mimeType="audio/mp4" audioSamplingRate="48000">\n        <AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>\n        <BaseURL>https://scontent-cph2-1.xx.fbcdn.net/v/t39.12897-6/198992520_981513595929106_5731656525090532090_n.m4a?_nc_cat=1&amp;ccb=1-7&amp;_nc_sid=02c1ff&amp;_nc_ohc=ZZ6zJXs2dkAAX-B0LDK&amp;_nc_ad=z-m&amp;_nc_cid=0&amp;_nc_ht=scontent-cph2-1.xx&amp;oh=00_AT8j4tjiUNSVWv9qbkg9Ro9MzAGeW9_wXU4e0ncV0MhdZQ&amp;oe=62DECA6E</BaseURL>\n        <SegmentBase indexRange="741-1672" timescale="48000">\n          <Initialization range="0-740"/>\n        </SegmentBase>\n      </Representation>\n    </AdaptationSet>\n  </Period>\n</MPD>\n',
'uri': HttpUrl('https://scontent-cph2-1.xx.fbcdn.net/v/t39.12897-6/198992520_981513595929106_5731656525090532090_n.m4a?_nc_cat=1&ccb=1-7&_nc_sid=02c1ff&_nc_ohc=ZZ6zJXs2dkAAX-B0LDK&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent-cph2-1.xx&oh=00_AT8j4tjiUNSVWv9qbkg9Ro9MzAGeW9_wXU4e0ncV0MhdZQ&oe=62DECA6E', scheme='https', host='scontent-cph2-1.xx.fbcdn.net', tld='net', host_type='domain', port='443', path='/v/t39.12897-6/198992520_981513595929106_5731656525090532090_n.m4a', query='_nc_cat=1&ccb=1-7&_nc_sid=02c1ff&_nc_ohc=ZZ6zJXs2dkAAX-B0LDK&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent-cph2-1.xx&oh=00_AT8j4tjiUNSVWv9qbkg9Ro9MzAGeW9_wXU4e0ncV0MhdZQ&oe=62DECA6E'),
'has_lyrics': True,
'audio_asset_id': 354372829354341,
'duration_in_ms': 150329,
'dark_message': None,
'allows_saving': True,
'territory_validity_periods': {}
}

```


================================================
FILE: docs/usage-guide/user.md
================================================
# User

View a list of a user's medias, following and followers

* `user_id` - Integer ID of user, example `1903424587`

| Method                                        | Return                | Description                                                  |
|-----------------------------------------------|-----------------------|--------------------------------------------------------------|
| user_followers(user_id: str, amount: int = 0) | Dict\[int, UserShort] | Get dict of followers users (amount=0 - fetch all followers) |
| user_following(user_id: str, amount: int = 0) | Dict\[int, UserShort] | Get dict of following users (amount=0 - fetch all)           |
| search_followers(user_id: str, query: str)    | List[UserShort]       | Search by followers                                          |
| search_following(user_id: str, query: str)    | List[UserShort]       | Search by following                                          |
| user_info(user_id: str)                       | User                  | Get user info                                                |
| user_info_by_username(username: str)          | User                  | Get user info by username                                    |
| user_follow(user_id: str)                     | bool                  | Follow user                                                  |
| user_unfollow(user_id: str)                   | bool                  | Unfollow user                                                |
| user_id_from_username(username: str)          | int                   | Get user_id by username                                      |
| username_from_user_id(user_id: str)           | str                   | Get username by user_id                                      |
| user_remove_follower(user_id: str)            | bool                  | Remove your follower                                         |
| mute_posts_from_follow(user_id: str)          | bool                  | Mute posts from following user                               |
| unmute_posts_from_follow(user_id: str)        | bool                  | Unmute posts from following user                             |
| mute_stories_from_follow(user_id: str)        | bool                  | Mute stories from following user                             |
| enable_posts_notifications(user_id: str)      | bool                  | Enable post notifications of user                            |
| disable_posts_notifications(user_id: str)     | bool                  | Disable post notifications of user                           |
| enable_videos_notifications(user_id: str)     | bool                  | Enable videos notifications of user                          |
| disable_videos_notifications(user_id: str)    | bool                  | Disable videos notifications of user                         |
| enable_reels_notifications(user_id: str)      | bool                  | Enable reels notifications of user                           |
| disable_reels_notifications(user_id: str)     | bool                  | Disable reels notifications of user                          |
| enable_stories_notifications(user_id: str)    | bool                  | Enable stories notifications of user                         |
| disable_stories_notifications(user_id: str)   | bool                  | Disable stories notifications of user                        |
| close_friend_add(user_id: str)                | bool                  | Add to Close Friends List                                    |
| close_friend_remove(user_id: str)             | bool                  | Remove from Close Friends List                               |

Low level methods:

| Method                                                                              | Return                      | Description                                                                |
|-------------------------------------------------------------------------------------|-----------------------------|----------------------------------------------------------------------------|
| user_followers_gql_chunk(user_id: str, max_amount: int = 0, end_cursor: str = None) | Tuple[List[UserShort], str] | Get user's followers information by Public Graphql API and end_cursor      |
| user_followers_gql(user_id: str, amount: int = 0)                                   | List[UserShort]             | Get user's followers information by Public Graphql API                     |
| user_followers_v1_chunk(user_id: str, max_amount: int = 0, max_id: str = "")        | Tuple[List[UserShort], str] | Get user's followers information by Private Mobile API and max_id (cursor) |
| user_followers_v1(user_id: str, amount: int = 0)                                    | List[UserShort]             | Get user's followers information by Private Mobile API                     |
| user_following_v1(user_id: str, amount: int = 0)                                    | List[UserShort]             | Get user's following users information by Private Mobile API               |
| user_following_gql(user_id: str, amount: int = 0)                                   | List[UserShort]             | Get user's following information by Public Graphql API                     |
| search_followers_v1(user_id: str, query: str)                                       | List[UserShort]             | Search by followers by Private Mobile API                                  |
| search_following_v1(user_id: str, query: str)                                       | List[UserShort]             | Search by following by Private Mobile API                                  |

Example:

``` python
>>> cl.user_followers(cl.user_id).keys()
dict_keys([5563084402, 43848984510, 1498977320, ...])

>>> cl.user_following(cl.user_id)
{
  8530498223: UserShort(
    pk=8530498223,
    username="something",
    full_name="Example description",
    profile_pic_url=HttpUrl(
      'https://instagram.frix7-1.fna.fbcdn.net/v/t5...9217617140_n.jpg',
      scheme='https',
      host='instagram.frix7-1.fna.fbcdn.net',
      ...
    ),
  ),
  49114585: UserShort(
    pk=49114585,
    username='gx1000',
    full_name='GX1000',
    profile_pic_url=HttpUrl(
      'https://scontent-hel3-1.cdninstagram.com/v/t51.2885-19/10388...jpg',
      scheme='https',
      host='scontent-hel3-1.cdninstagram.com',
      ...
    )
  ),
  ...
}

>>> cl.user_info_by_username('example').dict()
{'pk': 1903424587,
 'username': 'example',
 'full_name': 'Example Example',
 'is_private': False,
 'profile_pic_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t51.2885-19/s150x150/123884060_803537687159702_2508263208740189974_n.jpg?...', scheme='https', host='scontent-hel3-1.cdninstagram.com', tld='com', host_type='domain', ...'),
 'is_verified': False,
 'media_count': 102,
 'follower_count': 576,
 'following_count': 538,
 'biography': 'Engineer: Python, JavaScript, Erlang',
 'external_url': HttpUrl('https://example.org/', scheme='https', host='example.org', tld='com', host_type='domain', path='/'),
 'is_business': False}

```

Example: We go around the list of our followers and unfollow from them:

``` python
from instagrapi import Client
cl = Client()
cl.login(USERNAME, PASSWORD)

followers = cl.user_followers(cl.user_id)
for user_id in followers.keys():
    cl.user_unfollow(user_id)
```



================================================
FILE: examples/bot.py
================================================
import os
from time import sleep
from typing import Dict, List

from instagrapi import Client
from instagrapi.types import UserShort

IG_USERNAME = ""
IG_PASSWORD = ""
IG_CREDENTIAL_PATH = "./ig_settings.json"
SLEEP_TIME = "600"  # in seconds


class Bot:
    _cl = None

    def __init__(self):
        self._cl = Client()
        if os.path.exists(IG_CREDENTIAL_PATH):
            self._cl.load_settings(IG_CREDENTIAL_PATH)
            self._cl.login(IG_USERNAME, IG_PASSWORD)
        else:
            self._cl.login(IG_USERNAME, IG_PASSWORD)
            self._cl.dump_settings(IG_CREDENTIAL_PATH)

    def follow_by_username(self, username) -> bool:
        """
        Follow a user

        Parameters
        ----------
        username: str
            Username for an Instagram account

        Returns
        -------
        bool
            A boolean value
        """
        userid = self._cl.user_id_from_username(username)
        return self._cl.user_follow(userid)

    def unfollow_by_username(self, username) -> bool:
        """
        Unfollow a user

        Parameters
        ----------
        username: str
            Username for an Instagram account

        Returns
        -------
        bool
            A boolean value
        """
        userid = self._cl.user_id_from_username(username)
        return self._cl.user_unfollow(userid)

    def get_followers(self, amount: int = 0) -> Dict[int, UserShort]:
        """
        Get bot's followers

        Parameters
        ----------
        amount: int, optional
            Maximum number of media to return, default is 0 - Inf

        Returns
        -------
        Dict[int, UserShort]
            Dict of user_id and User object
        """
        return self._cl.user_followers(self._cl.user_id, amount=amount)

    def get_followers_usernames(self, amount: int = 0) -> List[str]:
        """
        Get bot's followers usernames

        Parameters
        ----------
        amount: int, optional
            Maximum number of media to return, default is 0 - Inf

        Returns
        -------
        List[str]
            List of usernames
        """
        followers = self._cl.user_followers(self._cl.user_id, amount=amount)
        return [user.username for user in followers.values()]

    def get_following(self, amount: int = 0) -> Dict[int, UserShort]:
        """
        Get bot's followed users

        Parameters
        ----------
        amount: int, optional
            Maximum number of media to return, default is 0 - Inf

        Returns
        -------
        Dict[int, UserShort]
            Dict of user_id and User object
        """
        return self._cl.user_following(self._cl.user_id, amount=amount)

    def get_following_usernames(self, amount: int = 0) -> List[str]:
        """
        Get bot's followed usernames

        Parameters
        ----------
        amount: int, optional
            Maximum number of media to return, default is 0 - Inf

        Returns
        -------
        List[str]
            List of usernames
        """
        following = self._cl.user_following(self._cl.user_id, amount=amount)
        return [user.username for user in following.values()]

    def update(self):
        """
        Do something
        """
        pass


if __name__ == "__main__":
    bot = Bot()

    bot.follow_by_username("futbot__")

    while True:
        """
        Infnit loop
        """
        bot.update()
        sleep(SLEEP_TIME)



================================================
FILE: examples/challenge_resolvers.py
================================================
"""
Example to handle Email/SMS challenges
"""
import email
import imaplib
import re
import random

from instagrapi import Client
from instagrapi.mixins.challenge import ChallengeChoice

CHALLENGE_EMAIL = ""
CHALLENGE_PASSWORD = ""

IG_USERNAME = ""
IG_PASSWORD = ""


def get_code_from_email(username):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(CHALLENGE_EMAIL, CHALLENGE_PASSWORD)
    mail.select("inbox")
    result, data = mail.search(None, "(UNSEEN)")
    assert result == "OK", "Error1 during get_code_from_email: %s" % result
    ids = data.pop().split()
    for num in reversed(ids):
        mail.store(num, "+FLAGS", "\\Seen")  # mark as read
        result, data = mail.fetch(num, "(RFC822)")
        assert result == "OK", "Error2 during get_code_from_email: %s" % result
        msg = email.message_from_string(data[0][1].decode())
        payloads = msg.get_payload()
        if not isinstance(payloads, list):
            payloads = [msg]
        code = None
        for payload in payloads:
            body = payload.get_payload(decode=True).decode()
            if "<div" not in body:
                continue
            match = re.search(">([^>]*?({u})[^<]*?)<".format(u=username), body)
            if not match:
                continue
            print("Match from email:", match.group(1))
            match = re.search(r">(\d{6})<", body)
            if not match:
                print('Skip this email, "code" not found')
                continue
            code = match.group(1)
            if code:
                return code
    return False


def get_code_from_sms(username):
    while True:
        code = input(f"Enter code (6 digits) for {username}: ").strip()
        if code and code.isdigit():
            return code
    return None


def challenge_code_handler(username, choice):
    if choice == ChallengeChoice.SMS:
        return get_code_from_sms(username)
    elif choice == ChallengeChoice.EMAIL:
        return get_code_from_email(username)
    return False


def change_password_handler(username):
    # Simple way to generate a random string
    chars = list("abcdefghijklmnopqrstuvwxyz1234567890!&£@#")
    password = "".join(random.sample(chars, 10))
    return password


if __name__ == "__main__":
    cl = Client()
    cl.challenge_code_handler = challenge_code_handler
    cl.change_password_handler = change_password_handler
    cl.login(IG_USERNAME, IG_PASSWORD)



================================================
FILE: examples/download_all_medias.py
================================================
import os

from instagrapi import Client

ACCOUNT_USERNAME = os.environ.get("IG_USERNAME")
ACCOUNT_PASSWORD = os.environ.get("IG_PASSWORD")


def main(username: str, amount: int = 5) -> dict:
    """
    Download all medias from instagram profile
    """
    amount = int(amount)
    cl = Client()
    cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
    user_id = cl.user_id_from_username(username)
    medias = cl.user_medias(user_id)
    result = {}
    i = 0
    for m in medias:
        if i >= amount:
            break
        paths = []
        if m.media_type == 1:
            # Photo
            paths.append(cl.photo_download(m.pk))
        elif m.media_type == 2 and m.product_type == "feed":
            # Video
            paths.append(cl.video_download(m.pk))
        elif m.media_type == 2 and m.product_type == "igtv":
            # IGTV
            paths.append(cl.video_download(m.pk))
        elif m.media_type == 2 and m.product_type == "clips":
            # Reels
            paths.append(cl.video_download(m.pk))
        elif m.media_type == 8:
            # Album
            for path in cl.album_download(m.pk):
                paths.append(path)
        result[m.pk] = paths
        print(f"http://instagram.com/p/{m.code}/", paths)
        i += 1
    return result


if __name__ == "__main__":
    username = input("Enter username: ")
    while True:
        amount = input("How many posts to process (default: 5)? ").strip()
        if amount == "":
            amount = "5"
        if amount.isdigit():
            break
    main(username, amount)



================================================
FILE: examples/handle_exception.py
================================================
from instagrapi import Client
from instagrapi.exceptions import (
    BadPassword,
    ChallengeRequired,
    FeedbackRequired,
    LoginRequired,
    PleaseWaitFewMinutes,
    RecaptchaChallengeForm,
    ReloginAttemptExceeded,
    SelectContactPointRecoveryForm,
)


class Account:
    username = ""
    password = ""

    def get_client(self):
        """We return the client class, in which we automatically handle exceptions
        You can move the "handle_exception" above or into an external module
        """

        def handle_exception(client, e):
            if isinstance(e, BadPassword):
                client.logger.exception(e)
                client.set_proxy(self.next_proxy().href)
                if client.relogin_attempt > 0:
                    self.freeze(str(e), days=7)
                    raise ReloginAttemptExceeded(e)
                client.settings = self.rebuild_client_settings()
                return self.update_client_settings(client.get_settings())
            elif isinstance(e, LoginRequired):
                client.logger.exception(e)
                client.relogin()
                return self.update_client_settings(client.get_settings())
            elif isinstance(e, ChallengeRequired):
                api_path = client.last_json.get("challenge", {}).get("api_path")
                if api_path == "/challenge/":
                    client.set_proxy(self.next_proxy().href)
                    client.settings = self.rebuild_client_settings()
                else:
                    try:
                        client.challenge_resolve(client.last_json)
                    except ChallengeRequired as e:
                        self.freeze("Manual Challenge Required", days=2)
                        raise e
                    except (
                        ChallengeRequired,
                        SelectContactPointRecoveryForm,
                        RecaptchaChallengeForm,
                    ) as e:
                        self.freeze(str(e), days=4)
                        raise e
                    self.update_client_settings(client.get_settings())
                return True
            elif isinstance(e, FeedbackRequired):
                message = client.last_json["feedback_message"]
                if "This action was blocked. Please try again later" in message:
                    self.freeze(message, hours=12)
                    # client.settings = self.rebuild_client_settings()
                    # return self.update_client_settings(client.get_settings())
                elif "We restrict certain activity to protect our community" in message:
                    # 6 hours is not enough
                    self.freeze(message, hours=12)
                elif "Your account has been temporarily blocked" in message:
                    """
                    Based on previous use of this feature, your account has been temporarily
                    blocked from taking this action.
                    This block will expire on 2020-03-27.
                    """
                    self.freeze(message)
            elif isinstance(e, PleaseWaitFewMinutes):
                self.freeze(str(e), hours=1)
            raise e

        cl = Client()
        cl.handle_exception = handle_exception
        cl.login(self.username, self.password)
        return cl



================================================
FILE: examples/medias.py
================================================
from typing import List

from instagrapi import Client
from instagrapi.types import Media

HASHTAGS = ["instacool"]
IG_USERNAME = ""
IG_PASSWORD = ""
IG_CREDENTIAL_PATH = "credential.json"


def get_logger(name, **kwargs):
    import logging

    logging.basicConfig(**kwargs)
    logger = logging.getLogger(name)
    logger.debug(f"start logging '{name}'")
    return logger


def filter_medias(
    medias: List[Media],
    like_count_min=None,
    like_count_max=None,
    comment_count_min=None,
    comment_count_max=None,
    days_ago_max=None,
):
    from datetime import datetime, timedelta

    medias = list(
        filter(
            lambda x: True
            if like_count_min is None
            else x.like_count >= like_count_min,
            medias,
        )
    )
    medias = list(
        filter(
            lambda x: True
            if like_count_max is None
            else x.like_count <= like_count_max,
            medias,
        )
    )
    medias = list(
        filter(
            lambda x: True
            if comment_count_min is None
            else x.comment_count >= comment_count_min,
            medias,
        )
    )
    medias = list(
        filter(
            lambda x: True
            if comment_count_max is None
            else x.comment_count <= comment_count_max,
            medias,
        )
    )
    if days_ago_max is not None:
        days_back = datetime.now() - timedelta(days=days_ago_max)
        medias = list(
            filter(
                lambda x: days_ago_max is None
                or x.taken_at is None
                or x.taken_at > days_back.astimezone(x.taken_at.tzinfo),
                medias,
            )
        )

    return list(medias)


def get_medias(
    hashtags,
    ht_type="top",
    amount=27,
):
    ht_medias = []
    for hashtag in hashtags:
        if ht_type == "top":
            ht_medias.extend(
                cl.hashtag_medias_top(name=hashtag, amount=amount if amount <= 9 else 9)
            )
        elif ht_type == "recent":
            ht_medias.extend(cl.hashtag_medias_recent(name=hashtag, amount=amount))
    return list(dict([(media.pk, media) for media in ht_medias]).values())


if __name__ == "__main__":
    import os

    log = get_logger(
        "example_media",
        **{
            "level": "DEBUG",
            "format": "%(asctime)s %(levelname)s %(name)s: %(message)s",
        },
    )
    cl = Client()
    if os.path.exists(IG_CREDENTIAL_PATH):
        cl.load_settings(IG_CREDENTIAL_PATH)
        cl.login(IG_USERNAME, IG_PASSWORD)
    else:
        cl.login(IG_USERNAME, IG_PASSWORD)
        cl.dump_settings(IG_CREDENTIAL_PATH)

    m = get_medias(HASHTAGS, amount=4)
    m = filter_medias(m, like_count_min=1, days_ago_max=365)
    log.info(len(m))



================================================
FILE: examples/next_proxy.py
================================================
"""
An example when you need to change proxy

https://github.com/subzeroid/instagrapi/discussions/299
"""
import random

from requests.exceptions import ProxyError
from urllib3.exceptions import HTTPError

from instagrapi import Client
from instagrapi.exceptions import (
    ClientConnectionError,
    ClientForbiddenError,
    ClientLoginRequired,
    ClientThrottledError,
    GenericRequestError,
    PleaseWaitFewMinutes,
    RateLimitError,
    SentryBlock,
)


def next_proxy():
    return random.choice(
        [
            "http://username:password@147.123123.123:412345",
            "http://username:password@147.123123.123:412346",
            "http://username:password@147.123123.123:412347",
        ]
    )


cl = Client(proxy=next_proxy())

try:
    cl.login("USERNAME", "PASSWORD")
except (ProxyError, HTTPError, GenericRequestError, ClientConnectionError):
    # Network level
    cl.set_proxy(next_proxy())
except (SentryBlock, RateLimitError, ClientThrottledError):
    # Instagram limit level
    cl.set_proxy(next_proxy())
except (ClientLoginRequired, PleaseWaitFewMinutes, ClientForbiddenError):
    # Logical level
    cl.set_proxy(next_proxy())



================================================
FILE: examples/session_login.py
================================================
"""Examples for session persistence and sessionid login."""

import os
from instagrapi import Client

IG_USERNAME = os.environ.get("IG_USERNAME")
IG_PASSWORD = os.environ.get("IG_PASSWORD")
SESSION_FILE = "session.json"


def login_with_persistence() -> Client:
    """Return Client logged in using saved session settings."""
    cl = Client()
    if os.path.exists(SESSION_FILE):
        cl.load_settings(SESSION_FILE)
    cl.login(IG_USERNAME, IG_PASSWORD)
    cl.dump_settings(SESSION_FILE)
    return cl


def login_with_sessionid(sessionid: str) -> Client:
    """Return Client logged in only with a sessionid."""
    cl = Client()
    cl.login_by_sessionid(sessionid)
    return cl


def list_and_download(username: str, amount: int = 10):
    """Download recent posts from the specified account."""
    cl = login_with_persistence()
    user_id = cl.user_id_from_username(username)
    for media in cl.user_medias(user_id, amount=amount):
        if media.media_type == 1:
            cl.photo_download(media.pk)
        elif media.media_type == 2:
            cl.video_download(media.pk)
        elif media.media_type == 8:
            cl.album_download(media.pk)


if __name__ == "__main__":
    target = input("Target username: ")
    list_and_download(target)



================================================
FILE: instagrapi/__init__.py
================================================
import logging
from urllib.parse import urlparse

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from instagrapi.mixins.account import AccountMixin
from instagrapi.mixins.album import DownloadAlbumMixin, UploadAlbumMixin
from instagrapi.mixins.auth import LoginMixin
from instagrapi.mixins.bloks import BloksMixin
from instagrapi.mixins.challenge import ChallengeResolveMixin
from instagrapi.mixins.clip import DownloadClipMixin, UploadClipMixin
from instagrapi.mixins.collection import CollectionMixin
from instagrapi.mixins.comment import CommentMixin
from instagrapi.mixins.direct import DirectMixin
from instagrapi.mixins.explore import ExploreMixin
from instagrapi.mixins.fbsearch import FbSearchMixin
from instagrapi.mixins.fundraiser import FundraiserMixin
from instagrapi.mixins.hashtag import HashtagMixin
from instagrapi.mixins.highlight import HighlightMixin
from instagrapi.mixins.igtv import DownloadIGTVMixin, UploadIGTVMixin
from instagrapi.mixins.insights import InsightsMixin
from instagrapi.mixins.location import LocationMixin
from instagrapi.mixins.media import MediaMixin
from instagrapi.mixins.multiple_accounts import MultipleAccountsMixin
from instagrapi.mixins.note import NoteMixin
from instagrapi.mixins.notification import NotificationMixin
from instagrapi.mixins.password import PasswordMixin
from instagrapi.mixins.photo import DownloadPhotoMixin, UploadPhotoMixin
from instagrapi.mixins.private import PrivateRequestMixin
from instagrapi.mixins.public import (
    ProfilePublicMixin,
    PublicRequestMixin,
    TopSearchesPublicMixin,
)
from instagrapi.mixins.share import ShareMixin
from instagrapi.mixins.signup import SignUpMixin
from instagrapi.mixins.story import StoryMixin
from instagrapi.mixins.timeline import ReelsMixin
from instagrapi.mixins.totp import TOTPMixin
from instagrapi.mixins.track import TrackMixin
from instagrapi.mixins.user import UserMixin
from instagrapi.mixins.video import DownloadVideoMixin, UploadVideoMixin

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Used as fallback logger if another is not provided.
DEFAULT_LOGGER = logging.getLogger("instagrapi")


class Client(
    PublicRequestMixin,
    ChallengeResolveMixin,
    PrivateRequestMixin,
    TopSearchesPublicMixin,
    ProfilePublicMixin,
    LoginMixin,
    ShareMixin,
    TrackMixin,
    FbSearchMixin,
    HighlightMixin,
    DownloadPhotoMixin,
    UploadPhotoMixin,
    DownloadVideoMixin,
    UploadVideoMixin,
    DownloadAlbumMixin,
    NotificationMixin,
    UploadAlbumMixin,
    DownloadIGTVMixin,
    UploadIGTVMixin,
    MediaMixin,
    UserMixin,
    InsightsMixin,
    CollectionMixin,
    AccountMixin,
    DirectMixin,
    LocationMixin,
    HashtagMixin,
    CommentMixin,
    StoryMixin,
    PasswordMixin,
    SignUpMixin,
    DownloadClipMixin,
    UploadClipMixin,
    ReelsMixin,
    ExploreMixin,
    BloksMixin,
    TOTPMixin,
    MultipleAccountsMixin,
    NoteMixin,
    FundraiserMixin,
):
    proxy = None

    def __init__(
        self,
        settings: dict = {},
        proxy: str | None = None,
        delay_range: list | None = None,
        logger=DEFAULT_LOGGER,
        **kwargs,
    ):

        super().__init__(**kwargs)

        self.settings = settings
        self.logger = logger
        self.delay_range = delay_range

        self.set_proxy(proxy)

        self.init()

    def set_proxy(self, dsn: str | None):
        if dsn:
            assert isinstance(
                dsn, str
            ), f'Proxy must been string (URL), but now "{dsn}" ({type(dsn)})'
            self.proxy = dsn
            proxy_href = "{scheme}{href}".format(
                scheme="http://" if not urlparse(self.proxy).scheme else "",
                href=self.proxy,
            )
            self.public.proxies = self.private.proxies = {
                "http": proxy_href,
                "https": proxy_href,
            }
            return True
        self.public.proxies = self.private.proxies = {}
        return False



================================================
FILE: instagrapi/config.py
================================================
API_DOMAIN = "i.instagram.com"

# Instagram 134.0.0.26.121
# Android (26/8.0.0;
# 480dpi; 1080x1920; Xiaomi;
# MI 5s; capricorn; qcom; en_US; 205280538)
USER_AGENT_BASE = (
    "Instagram {app_version} "
    "Android ({android_version}/{android_release}; "
    "{dpi}; {resolution}; {manufacturer}; "
    "{model}; {device}; {cpu}; {locale}; {version_code})"
)
# Instagram 76.0.0.15.395 (iPhone9,2; iOS 10_0_2; en_US; en-US; scale=2.61; 1080x1920) AppleWebKit/420+
# Instagram 208.0.0.32.135 (iPhone; iOS 14_7_1; en_US; en-US; scale=2.61; 1080x1920) AppleWebKit/605.1.15

SOFTWARE = (
    "{model}-user+{android_release}+OPR1.170623.032+V10.2.3.0.OAGMIXM+release-keys"
)

# QUERY_HASH_PROFILE = 'c9100bf9110dd6361671f113dd02e7d6'
# QUERY_HASH_MEDIAS = '42323d64886122307be10013ad2dcc44'
# QUERY_HASH_IGTVS = 'bc78b344a68ed16dd5d7f264681c4c76'
# QUERY_HASH_STORIES = '5ec1d322b38839230f8e256e1f638d5f'
# QUERY_HASH_HIGHLIGHTS_FOLDERS = 'ad99dd9d3646cc3c0dda65debcd266a7'
# QUERY_HASH_HIGHLIGHTS_STORIES = '5ec1d322b38839230f8e256e1f638d5f'
# QUERY_HASH_FOLLOWERS = 'c76146de99bb02f6415203be841dd25a'
# QUERY_HASH_FOLLOWINGS = 'd04b0a864b4b54837c0d870b0e77e076'
# QUERY_HASH_HASHTAG = '174a5243287c5f3a7de741089750ab3b'
# QUERY_HASH_COMMENTS = '33ba35852cb50da46f5b5e889df7d159'
# QUERY_HASH_TAGGED_MEDIAS = 'be13233562af2d229b008d2976b998b5'

LOGIN_EXPERIMENTS = (
    "ig_android_reg_nux_headers_cleanup_universe,"
    "ig_android_device_detection_info_upload,"
    "ig_android_nux_add_email_device,"
    "ig_android_gmail_oauth_in_reg,"
    "ig_android_device_info_foreground_reporting,"
    "ig_android_device_verification_fb_signup,"
    "ig_android_direct_main_tab_universe_v2,"
    "ig_android_passwordless_account_password_creation_universe,"
    "ig_android_direct_add_direct_to_android_native_photo_share_sheet,"
    "ig_growth_android_profile_pic_prefill_with_fb_pic_2,"
    "ig_account_identity_logged_out_signals_global_holdout_universe,"
    "ig_android_quickcapture_keep_screen_on,"
    "ig_android_device_based_country_verification,"
    "ig_android_login_identifier_fuzzy_match,"
    "ig_android_reg_modularization_universe,"
    "ig_android_security_intent_switchoff,"
    "ig_android_device_verification_separate_endpoint,"
    "ig_android_suma_landing_page,"
    "ig_android_sim_info_upload,"
    "ig_android_smartlock_hints_universe,"
    "ig_android_fb_account_linking_sampling_freq_universe,"
    "ig_android_retry_create_account_universe,"
    "ig_android_caption_typeahead_fix_on_o_universe"
)

SUPPORTED_CAPABILITIES = [
    {
        "value": (
            "119.0,120.0,121.0,122.0,123.0,124.0,125.0,126.0,127.0,128.0,"
            "129.0,130.0,131.0,132.0,133.0,134.0,135.0,136.0,137.0,138.0,"
            "139.0,140.0,141.0,142.0"
        ),
        "name": "SUPPORTED_SDK_VERSIONS",
    },
    {"value": "14", "name": "FACE_TRACKER_VERSION"},
    {"value": "ETC2_COMPRESSION", "name": "COMPRESSION"},
    {"value": "gyroscope_enabled", "name": "gyroscope"},
]



================================================
FILE: instagrapi/exceptions.py
================================================
class ClientError(Exception):
    response = None
    code = None
    message = ""

    def __init__(self, *args, **kwargs):
        args = list(args)
        if len(args) > 0:
            self.message = str(args.pop(0))
        for key in list(kwargs.keys()):
            setattr(self, key, kwargs.pop(key))
        if not self.message:
            self.message = "{title} ({body})".format(
                title=getattr(self, "reason", "Unknown"),
                body=getattr(self, "error_type", vars(self)),
            )
        super().__init__(self.message, *args, **kwargs)
        if self.response:
            self.code = self.response.status_code


class ClientUnknownError(ClientError):
    pass


class WrongCursorError(ClientError):
    message = "You specified a non-existent cursor"


class ClientStatusFail(ClientError):
    pass


class ClientErrorWithTitle(ClientError):
    pass


class ResetPasswordError(ClientError):
    pass


class GenericRequestError(ClientError):
    """Sorry, there was a problem with your request"""


class ClientGraphqlError(ClientError):
    """Raised due to graphql issues"""


class ClientJSONDecodeError(ClientError):
    """Raised due to json decoding issues"""


class ClientConnectionError(ClientError):
    """Raised due to network connectivity-related issues"""


class ClientBadRequestError(ClientError):
    """Raised due to a HTTP 400 response"""


class ClientUnauthorizedError(ClientError):
    """Raised due to a HTTP 401 response"""


class ClientForbiddenError(ClientError):
    """Raised due to a HTTP 403 response"""


class ClientNotFoundError(ClientError):
    """Raised due to a HTTP 404 response"""


class ClientThrottledError(ClientError):
    """Raised due to a HTTP 429 response"""


class ClientRequestTimeout(ClientError):
    """Raised due to a HTTP 408 response"""


class ClientIncompleteReadError(ClientError):
    """Raised due to incomplete read HTTP response"""


class ClientLoginRequired(ClientError):
    """Instagram redirect to https://www.instagram.com/accounts/login/"""


class ReloginAttemptExceeded(ClientError):
    pass


class PrivateError(ClientError):
    """For Private API and last_json logic"""


class NotFoundError(PrivateError):
    reason = "Not found"


class FeedbackRequired(PrivateError):
    pass


class ChallengeError(PrivateError):
    pass


class ChallengeRedirection(ChallengeError):
    pass


class ChallengeRequired(ChallengeError):
    pass


class ChallengeSelfieCaptcha(ChallengeError):
    pass


class ChallengeUnknownStep(ChallengeError):
    pass


class SelectContactPointRecoveryForm(ChallengeError):
    pass


class RecaptchaChallengeForm(ChallengeError):
    pass


class SubmitPhoneNumberForm(ChallengeError):
    pass


class LegacyForceSetNewPasswordForm(ChallengeError):
    pass


class LoginRequired(PrivateError):
    """Instagram request relogin
    Example:
    {'message': 'login_required',
    'response': <Response [403]>,
    'error_title': "You've Been Logged Out",
    'error_body': 'Please log back in.',
    'logout_reason': 8,
    'status': 'fail'}
    """


class SentryBlock(PrivateError):
    pass


class RateLimitError(PrivateError):
    pass


class ProxyAddressIsBlocked(PrivateError):
    """Instagram has blocked your IP address, use a quality proxy provider (not free, not shared)"""


class BadPassword(PrivateError):
    pass


class BadCredentials(PrivateError):
    pass


class PleaseWaitFewMinutes(PrivateError):
    pass


class UnknownError(PrivateError):
    pass


class TrackNotFound(NotFoundError):
    pass


class MediaError(PrivateError):
    pass


class MediaNotFound(NotFoundError, MediaError):
    pass


class StoryNotFound(NotFoundError, MediaError):
    pass


class UserError(PrivateError):
    pass


class UserNotFound(NotFoundError, UserError):
    pass


class CollectionError(PrivateError):
    pass


class CollectionNotFound(NotFoundError, CollectionError):
    pass


class DirectError(PrivateError):
    pass


class DirectThreadNotFound(NotFoundError, DirectError):
    pass


class DirectMessageNotFound(NotFoundError, DirectError):
    pass


class VideoTooLongException(PrivateError):
    pass


class VideoNotDownload(PrivateError):
    pass


class VideoNotUpload(PrivateError):
    pass


class VideoConfigureError(VideoNotUpload):
    pass


class VideoConfigureStoryError(VideoConfigureError):
    pass


class PhotoNotUpload(PrivateError):
    pass


class PhotoConfigureError(PhotoNotUpload):
    pass


class PhotoConfigureStoryError(PhotoConfigureError):
    pass


class IGTVNotUpload(PrivateError):
    pass


class IGTVConfigureError(IGTVNotUpload):
    pass


class ClipNotUpload(PrivateError):
    pass


class ClipConfigureError(ClipNotUpload):
    pass


class AlbumNotDownload(PrivateError):
    pass


class AlbumUnknownFormat(PrivateError):
    pass


class AlbumConfigureError(PrivateError):
    pass


class HashtagError(PrivateError):
    pass


class HashtagNotFound(NotFoundError, HashtagError):
    pass


class LocationError(PrivateError):
    pass


class LocationNotFound(NotFoundError, LocationError):
    pass


class TwoFactorRequired(PrivateError):
    pass


class HighlightNotFound(NotFoundError, PrivateError):
    pass


class NoteNotFound(NotFoundError):
    reason = "Not found"


class PrivateAccount(PrivateError):
    """This Account is Private"""


class InvalidTargetUser(PrivateError):
    """Invalid target user"""


class InvalidMediaId(PrivateError):
    """Invalid media_id"""


class MediaUnavailable(PrivateError):
    """Media is unavailable"""


class ValidationError(AssertionError):
    pass


class EmailInvalidError(ClientError):
    pass


class EmailNotAvailableError(ClientError):
    pass


class EmailVerificationSendError(ClientError):
    pass


class AgeEligibilityError(ClientError):
    pass


class CaptchaChallengeRequired(ClientError):
    """Captcha challenge required, and no solver is configured or available."""
    def __init__(self, message="Captcha challenge required, but no solver configured or available.", challenge_details=None, **kwargs):
        self.challenge_details = challenge_details if challenge_details else {}
        # Example of extracting common details:
        # self.site_key = self.challenge_details.get('site_key')
        # self.challenge_url = self.challenge_details.get('challenge_url') # URL where captcha is presented
        super().__init__(message, **kwargs)



================================================
FILE: instagrapi/extractors.py
================================================
import datetime
import html
import json
import re
from copy import deepcopy

from .types import (
    Account,
    Broadcast,
    Collection,
    Comment,
    DirectMedia,
    DirectMessage,
    DirectResponse,
    DirectShortThread,
    DirectThread,
    Guide,
    Hashtag,
    Highlight,
    Location,
    Media,
    MediaOembed,
    MediaXma,
    ReplyMessage,
    Resource,
    Story,
    StoryHashtag,
    StoryLink,
    StoryLocation,
    StoryMedia,
    StoryMention,
    Track,
    User,
    UserShort,
    Usertag,
)
from .utils import InstagramIdCodec, json_value

MEDIA_TYPES_GQL = {"GraphImage": 1, "GraphVideo": 2, "GraphSidecar": 8, "StoryVideo": 2}


def extract_media_v1(data):
    """Extract media from Private API"""
    media = deepcopy(data)
    if "video_versions" in media:
        # Select Best Quality by Resolutiuon
        media["video_url"] = sorted(
            media["video_versions"], key=lambda o: o["height"] * o["width"]
        )[-1]["url"]
    if media["media_type"] == 2 and not media.get("product_type"):
        media["product_type"] = "feed"
    if "image_versions2" in media:
        media["thumbnail_url"] = sorted(
            media["image_versions2"]["candidates"],
            key=lambda o: o["height"] * o["width"],
        )[-1]["url"]
    if media["media_type"] == 8:
        # remove thumbnail_url and video_url for albums
        # see resources
        media.pop("thumbnail_url", "")
        media.pop("video_url", "")
    location = media.get("location")
    media["location"] = location and extract_location(location)
    media["user"] = extract_user_short(media.get("user"))
    media["usertags"] = sorted(
        [
            extract_usertag(usertag)
            for usertag in media.get("usertags", {}).get("in", [])
        ],
        key=lambda tag: tag.user.pk,
    )
    media["like_count"] = media.get("like_count", 0)
    media["has_liked"] = media.get("has_liked", False)
    media["sponsor_tags"] = [tag["sponsor"] for tag in media.get("sponsor_tags") or []]
    media["play_count"] = media.get("play_count", 0)
    media["coauthor_producers"] = media.get("coauthor_producers", [])
    return Media(
        caption_text=(media.get("caption") or {}).get("text", ""),
        resources=[
            extract_resource_v1(edge) for edge in media.get("carousel_media", [])
        ],
        **media,
    )


def extract_media_v1_xma(data):
    """Extract media from Private API"""
    media = deepcopy(data)

    # media["media_type"] = 10
    media["video_url"] = media.get("target_url", "")
    media["title"] = media.get("title_text", "")
    media["preview_url"] = media.get("preview_url", "")
    media["preview_url_mime_type"] = media.get("preview_url_mime_type", "")
    media["header_icon_url"] = media.get("header_icon_url", "")
    media["header_icon_width"] = media.get("header_icon_width", 0)
    media["header_icon_height"] = media.get("header_icon_height", 0)
    media["header_title_text"] = media.get("header_title_text", "")
    media["preview_media_fbid"] = media.get("preview_media_fbid", "")

    return MediaXma(
        **media,
    )


def extract_media_gql(data):
    """Extract media from GraphQL"""
    media = deepcopy(data)
    user = extract_user_short(media["owner"])
    # if "full_name" in user:
    #     user = extract_user_short(user)
    # else:
    #     user["pk"] = user.pop("id")
    try:
        media["media_type"] = MEDIA_TYPES_GQL[media["__typename"]]
    except KeyError:
        media["media_type"] = 0
    if media.get("media_type") == 2 and not media.get("product_type"):
        media["product_type"] = "feed"
    sorted_resources = sorted(
        # display_resources - user feed, thumbnail_resources - hashtag feed
        media.get("display_resources", media.get("thumbnail_resources", [])),
        key=lambda o: o["config_width"] * o["config_height"],
    )
    if sorted_resources:
        media["thumbnail_url"] = sorted_resources[-1]["src"]
    elif "thumbnail_src" in media:
        media["thumbnail_url"] = media["thumbnail_src"]
    if media.get("media_type") == 8:
        # remove thumbnail_url and video_url for albums
        # see resources
        media.pop("thumbnail_url", "")
        media.pop("video_url", "")
    location = media.pop("location", None)
    media_id = media.get("id")
    media["pk"] = media_id
    media["id"] = f"{media_id}_{user.pk}"
    return Media(
        code=media.get("shortcode"),
        taken_at=media.get("taken_at_timestamp"),
        location=extract_location(location) if location else None,
        user=user,
        view_count=media.get("video_view_count", 0),
        comment_count=json_value(media, "edge_media_to_comment", "count"),
        like_count=json_value(media, "edge_media_preview_like", "count"),
        caption_text=json_value(
            media, "edge_media_to_caption", "edges", 0, "node", "text", default=""
        ),
        usertags=sorted(
            [
                extract_usertag(usertag["node"])
                for usertag in media.get("edge_media_to_tagged_user", {}).get(
                    "edges", []
                )
            ],
            key=lambda tag: tag.user.pk,
        ),
        resources=[
            extract_resource_gql(edge["node"])
            for edge in media.get("edge_sidecar_to_children", {}).get("edges", [])
        ],
        sponsor_tags=[
            extract_user_short(edge["node"]["sponsor"])
            for edge in media.get("edge_media_to_sponsor_user", {}).get("edges", [])
        ],
        **media,
    )


def extract_resource_v1(data):
    if "video_versions" in data:
        data["video_url"] = sorted(
            data["video_versions"], key=lambda o: o["height"] * o["width"]
        )[-1]["url"]
    data["thumbnail_url"] = sorted(
        data["image_versions2"]["candidates"],
        key=lambda o: o["height"] * o["width"],
    )[-1]["url"]
    return Resource(**data)


def extract_resource_gql(data):
    data["media_type"] = MEDIA_TYPES_GQL[data["__typename"]]
    return Resource(pk=data["id"], thumbnail_url=data["display_url"], **data)


def extract_usertag(data):
    """Extract user tag"""
    x, y = data.get("position", [data.get("x"), data.get("y")])
    return Usertag(user=extract_user_short(data["user"]), x=x, y=y)


def extract_user_short(data):
    """Extract User Short info"""
    data["pk"] = data.get("id", data.get("pk", None))
    assert data["pk"], f'User without pk "{data}"'
    return UserShort(**data)


def extract_broadcast_channel(data):
    """ Extract broadcast channel infos """
    channels = data["pinned_channels_info"]["pinned_channels_list"]
    return [Broadcast(**channel) for channel in channels]


def extract_user_gql(data):
    """For Public GraphQL API"""
    data["broadcast_channel"] = extract_broadcast_channel(data)
    return User(
        pk=data["id"],
        media_count=data["edge_owner_to_timeline_media"]["count"],
        follower_count=data["edge_followed_by"]["count"],
        following_count=data["edge_follow"]["count"],
        is_business=data["is_business_account"],
        public_email=data["business_email"],
        contact_phone_number=data["business_phone_number"],
        **data,
    )


def extract_user_v1(data):
    """For Private API"""
    data["broadcast_channel"] = extract_broadcast_channel(data)
    data["external_url"] = data.get("external_url") or None
    versions = data.get("hd_profile_pic_versions")
    pic_hd = versions[-1] if versions else data.get("hd_profile_pic_url_info", {})
    data["profile_pic_url_hd"] = pic_hd.get("url")
    return User(**data)


def extract_location(data):
    """Extract location info"""
    if not data:
        return None
    data["pk"] = data.get("id", data.get("pk", data.get("location_id", None)))
    data["external_id"] = data.get("external_id", data.get("facebook_places_id"))
    data["external_id_source"] = data.get(
        "external_id_source", data.get("external_source")
    )
    data["address"] = data.get("address", data.get("location_address"))
    data["city"] = data.get("city", data.get("location_city"))
    data["zip"] = data.get("zip", data.get("location_zip"))
    address_json = data.get("address_json", "{}")
    if isinstance(address_json, str):
        address = json.loads(address_json)
        if isinstance(address, dict) and address:
            data["address"] = address.get("street_address")
            data["city"] = address.get("city_name")
            data["zip"] = address.get("zip_code")
    return Location(**data)


def extract_comment(data):
    """Extract comment"""
    data["has_liked"] = data.get("has_liked_comment")
    data["like_count"] = data.get("comment_like_count")
    return Comment(**data)


def extract_collection(data):
    """Extract collection for authorized account
    Example:
    {'collection_id': '17851406186124602',
    'collection_name': 'Repost',
    'collection_type': 'MEDIA',
    'collection_media_count': 1,
    'cover_media': {...}
    """
    data = {key.replace("collection_", ""): val for key, val in data.items()}
    # data['pk'] = data.get('id')
    return Collection(**data)


def extract_media_oembed(data):
    """Return short version of Media"""
    return MediaOembed(**data)


def extract_direct_thread(data):
    data["pk"] = data.get("thread_v2_id")
    data["id"] = data.get("thread_id")
    data["messages"] = []
    for item in data["items"]:
        item["thread_id"] = data["id"]
        data["messages"].append(extract_direct_message(item))
    data["users"] = [extract_user_short(u) for u in data["users"]]
    inviter = data.get("inviter")
    if inviter:
        data["inviter"] = extract_user_short(inviter)
    else:
        data["inviter"] = None
    data["left_users"] = data.get("left_users", [])
    data["last_activity_at"] = datetime.datetime.fromtimestamp(
        data["last_activity_at"] // 1_000_000
    )
    
    # Convert last_seen_at timestamps
    last_seen_at = data.get("last_seen_at", {})
    for user_id, seen_info in last_seen_at.items():
        if "timestamp" in seen_info:
            seen_info["timestamp"] = datetime.datetime.fromtimestamp(
                int(seen_info["timestamp"]) // 1_000_000
            )
        if "created_at" in seen_info:
            seen_info["created_at"] = datetime.datetime.fromtimestamp(
                int(seen_info["created_at"]) // 1_000_000
            )
        # Convert disappearing messages seen state timestamps
        disappearing_state = seen_info.get("disappearing_messages_seen_state")
        if disappearing_state:
            if "timestamp" in disappearing_state:
                disappearing_state["timestamp"] = datetime.datetime.fromtimestamp(
                    int(disappearing_state["timestamp"]) // 1_000_000
                )
            if "created_at" in disappearing_state:
                disappearing_state["created_at"] = datetime.datetime.fromtimestamp(
                    int(disappearing_state["created_at"]) // 1_000_000
                )
    
    return DirectThread(**data)


def extract_direct_short_thread(data):
    data["users"] = [extract_user_short(u) for u in data["users"]]
    data["id"] = data.get("thread_id")
    return DirectShortThread(**data)


def extract_direct_response(data):
    return DirectResponse(**data)


def extract_reply_message(data):
    data["id"] = data.get("item_id")
    if "media_share" in data:
        ms = data["media_share"]
        if not ms.get("code"):
            ms["code"] = InstagramIdCodec.encode(ms["id"])
        data["media_share"] = extract_media_v1(ms)
    if "media" in data:
        data["media"] = extract_direct_media(data["media"])
    clip = data.get("clip", {})
    if clip:
        if "clip" in clip:
            # Instagram ¯\_(ツ)_/¯
            clip = clip.get("clip")
        data["clip"] = extract_media_v1(clip)

    data["timestamp"] = datetime.datetime.fromtimestamp(data["timestamp"] // 1_000_000)
    data["user_id"] = str(data["user_id"])

    return ReplyMessage(**data)


def extract_direct_message(data):
    data["id"] = data.get("item_id")
    if "replied_to_message" in data:
        data["reply"] = extract_reply_message(data["replied_to_message"])
    if "media_share" in data:
        ms = data["media_share"]
        if not ms.get("code"):
            ms["code"] = InstagramIdCodec.encode(ms["id"])
        data["media_share"] = extract_media_v1(ms)
    if "media" in data:
        data["media"] = extract_direct_media(data["media"])
    if "voice_media" in data:
        if "media" in data["voice_media"]:
            data["media"] = extract_direct_media(data["voice_media"]["media"])
    clip = data.get("clip", {})
    if clip:
        if "clip" in clip:
            # Instagram ¯\_(ツ)_/¯
            clip = clip.get("clip")
        data["clip"] = extract_media_v1(clip)
    xma_media_share = data.get("xma_media_share", {})
    if xma_media_share:
        data["xma_share"] = extract_media_v1_xma(xma_media_share[0])

    # Convert main timestamp
    data["timestamp"] = datetime.datetime.fromtimestamp(
        int(data["timestamp"]) // 1_000_000
    )
    data["user_id"] = str(data.get("user_id", ""))
    data["client_context"] = data.get("client_context", "")

    # Convert reaction timestamps
    reactions = data.get("reactions", {})
    if reactions and "emojis" in reactions:
        for emoji_reaction in reactions["emojis"]:
            if "timestamp" in emoji_reaction:
                emoji_reaction["timestamp"] = datetime.datetime.fromtimestamp(
                    int(emoji_reaction["timestamp"]) // 1_000_000
                )

    # Convert visual media timestamps
    visual_media = data.get("visual_media", {})
    if visual_media and "media" in visual_media:
        media = visual_media["media"]
        if "expiring_media_action_summary" in media and media["expiring_media_action_summary"]:
            media["expiring_media_action_summary"]["timestamp"] = datetime.datetime.fromtimestamp(
                int(media["expiring_media_action_summary"]["timestamp"]) // 1_000_000
            )
        
        # Convert image candidates URL expiration timestamps
        if "image_versions2" in media and media["image_versions2"]:
            candidates = media["image_versions2"].get("candidates", [])
            for candidate in candidates:
                if "url_expiration_timestamp_us" in candidate and candidate["url_expiration_timestamp_us"]:
                    candidate["url_expiration_timestamp_us"] = datetime.datetime.fromtimestamp(
                        int(candidate["url_expiration_timestamp_us"]) // 1_000_000
                    )
        
        # Convert video versions URL expiration timestamps
        if "video_versions" in media and media["video_versions"]:
            for video_version in media["video_versions"]:
                if "url_expiration_timestamp_us" in video_version and video_version["url_expiration_timestamp_us"]:
                    video_version["url_expiration_timestamp_us"] = datetime.datetime.fromtimestamp(
                        int(video_version["url_expiration_timestamp_us"]) // 1_000_000
                    )
    
    # Convert top-level visual media expiring action summary timestamp
    if visual_media and "expiring_media_action_summary" in visual_media and visual_media["expiring_media_action_summary"]:
        visual_media["expiring_media_action_summary"]["timestamp"] = datetime.datetime.fromtimestamp(
            int(visual_media["expiring_media_action_summary"]["timestamp"]) // 1_000_000
        )

    return DirectMessage(**data)


def extract_direct_media(data):
    media = deepcopy(data)
    if "video_versions" in media:
        # Select Best Quality by Resolutiuon
        media["video_url"] = sorted(
            media["video_versions"], key=lambda o: o["height"] * o["width"]
        )[-1]["url"]
    if "image_versions2" in media:
        media["thumbnail_url"] = sorted(
            media["image_versions2"]["candidates"],
            key=lambda o: o["height"] * o["width"],
        )[-1]["url"]
    if "user" in media:
        media["user"] = extract_user_short(media.get("user"))
    if "audio" in media:
        media["audio_url"] = media["audio"].get("audio_src")
    return DirectMedia(**media)


def extract_account(data):
    data["pk"] = str(data["pk"])
    data["external_url"] = data.get("external_url") or None
    return Account(**data)


def extract_hashtag_gql(data):
    data["media_count"] = data.get("edge_hashtag_to_media", {}).get("count")
    data["profile_pic_url"] = data.get("profile_pic_url") or None
    return Hashtag(**data)


def extract_hashtag_v1(data):
    data["allow_following"] = data.get("allow_following") == 1
    data["profile_pic_url"] = data.get("profile_pic_url") or None
    return Hashtag(**data)


def extract_story_v1(data):
    """Extract story from Private API"""
    story = deepcopy(data)
    story["pk"] = str(story.get("pk"))
    if "video_versions" in story:
        # Select Best Quality by Resolutiuon
        story["video_url"] = sorted(
            story["video_versions"], key=lambda o: o["height"] * o["width"]
        )[-1]["url"]
    if story["media_type"] == 2 and not story.get("product_type"):
        story["product_type"] = "story"
    if "image_versions2" in story:
        story["thumbnail_url"] = sorted(
            story["image_versions2"]["candidates"],
            key=lambda o: o["height"] * o["width"],
        )[-1]["url"]
    story["mentions"] = [
        StoryMention(**mention) for mention in story.get("reel_mentions", [])
    ]
    story["locations"] = [
        StoryLocation(**location) for location in story.get("story_locations", [])
    ]
    story["hashtags"] = [
        StoryHashtag(**hashtag) for hashtag in story.get("story_hashtags", [])
    ]
    story["stickers"] = data.get("story_link_stickers") or []
    feed_medias = []
    story_feed_medias = data.get("story_feed_media") or []
    for feed_media in story_feed_medias:
        feed_media["media_pk"] = int(feed_media["media_id"])
        feed_medias.append(StoryMedia(**feed_media))
    story["medias"] = feed_medias
    story["links"] = []
    for cta in story.get("story_cta", []):
        for link in cta.get("links", []):
            story["links"].append(StoryLink(**link))
    story["user"] = extract_user_short(story.get("user"))
    story["sponsor_tags"] = [tag["sponsor"] for tag in story.get("sponsor_tags", [])]
    story["is_paid_partnership"] = story.get("is_paid_partnership")
    return Story(**story)


def extract_story_gql(data):
    """Extract story from Public API"""
    story = deepcopy(data)
    if "video_resources" in story:
        # Select Best Quality by Resolutiuon
        story["video_url"] = sorted(
            story["video_resources"],
            key=lambda o: o["config_height"] * o["config_width"],
        )[-1]["src"]
    story["product_type"] = "story"
    story["thumbnail_url"] = story.get("display_url")
    story["mentions"] = []
    story["medias"] = []
    for item in story.get("tappable_objects", []):
        if item["__typename"] == "GraphTappableMention":
            item["id"] = 1
            item["user"] = extract_user_short(item)
            story["mentions"].append(StoryMention(**item))
        if item["__typename"] == "GraphTappableFeedMedia":
            media = item.get("media")
            if media:
                item["media_pk"] = int(media["id"])
                item["media_code"] = media["shortcode"]
            story["medias"].append(StoryMedia(**item))
    story["locations"] = []
    story["hashtags"] = []
    story["stickers"] = []
    story["links"] = []
    story_cta_url = story.get("story_cta_url", [])
    if story_cta_url:
        story["links"] = [StoryLink(**{"webUri": story_cta_url})]
    story["user"] = extract_user_short(story.get("owner"))
    story["pk"] = str(story["id"])
    story["id"] = f"{story['id']}_{story['owner']['id']}"
    story["code"] = InstagramIdCodec.encode(story["pk"])
    story["taken_at"] = story["taken_at_timestamp"]
    story["media_type"] = 2 if story["is_video"] else 1
    story["sponsor_tags"] = [
        extract_user_short(edge["node"]["sponsor"])
        for edge in story.get("edge_media_to_sponsor_user", {}).get("edges", [])
    ]
    return Story(**story)


def extract_highlight_v1(data):
    highlight = deepcopy(data)
    highlight["pk"] = highlight["id"].split(":")[1]
    highlight["items"] = [extract_story_v1(item) for item in highlight.get("items", [])]
    return Highlight(**highlight)


def extract_guide_v1(data):
    item = deepcopy(data.get("summary") or {})
    item["cover_media"] = extract_media_v1(item["cover_media"])
    return Guide(**item)


def extract_track(data):
    data["cover_artwork_uri"] = data.get("cover_artwork_uri") or None
    data["cover_artwork_thumbnail_uri"] = (
        data.get("cover_artwork_thumbnail_uri") or None
    )
    items = re.findall(r"<BaseURL>(.+?)</BaseURL>", data["dash_manifest"])
    data["uri"] = html.unescape(items[0]) if items else None
    data["territory_validity_periods"] = data.get("territory_validity_periods") or {}
    return Track(**data)



================================================
FILE: instagrapi/image_util.py
================================================
# Copyright (c) 2017 https://github.com/ping
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import io
import os
import re
import shutil
import tempfile

try:
    from PIL import Image
except ImportError:
    raise Exception("You don't have PIL installed. Please install PIL or Pillow>=8.1.1")

import requests


def calc_resize(max_size, curr_size, min_size=(0, 0)):
    """
    Calculate if resize is required based on the max size desired
    and the current size

    :param max_size: tuple of (width, height)
    :param curr_size: tuple of (width, height)
    :param min_size: tuple of (width, height)
    :return:
    """
    max_width, max_height = max_size or (0, 0)
    min_width, min_height = min_size or (0, 0)

    if (max_width and min_width > max_width) or (
        max_height and min_height > max_height
    ):
        raise ValueError("Invalid min / max sizes.")

    orig_width, orig_height = curr_size
    if (
        max_width
        and max_height
        and (orig_width > max_width or orig_height > max_height)
    ):
        resize_factor = min(
            1.0 * max_width / orig_width, 1.0 * max_height / orig_height
        )
        new_width = int(resize_factor * orig_width)
        new_height = int(resize_factor * orig_height)
        return new_width, new_height

    elif (
        min_width
        and min_height
        and (orig_width < min_width or orig_height < min_height)
    ):
        resize_factor = max(
            1.0 * min_width / orig_width, 1.0 * min_height / orig_height
        )
        new_width = int(resize_factor * orig_width)
        new_height = int(resize_factor * orig_height)
        return new_width, new_height


def calc_crop(aspect_ratios, curr_size):
    """
    Calculate if cropping is required based on the desired aspect
    ratio and the current size.

    :param aspect_ratios: single float value or tuple of (min_ratio, max_ratio)
    :param curr_size: tuple of (width, height)
    :return:
    """
    try:
        if len(aspect_ratios) == 2:
            min_aspect_ratio = float(aspect_ratios[0])
            max_aspect_ratio = float(aspect_ratios[1])
        else:
            raise ValueError("Invalid aspect ratios")
    except TypeError:
        # not a min-max range
        min_aspect_ratio = float(aspect_ratios)
        max_aspect_ratio = float(aspect_ratios)

    curr_aspect_ratio = 1.0 * curr_size[0] / curr_size[1]
    if not min_aspect_ratio <= curr_aspect_ratio <= max_aspect_ratio:
        curr_width = curr_size[0]
        curr_height = curr_size[1]
        if curr_aspect_ratio > max_aspect_ratio:
            # media is too wide
            new_height = curr_height
            new_width = max_aspect_ratio * new_height
        else:
            # media is too tall
            new_width = curr_width
            new_height = new_width / min_aspect_ratio
        left = int((curr_width - new_width) / 2)
        top = int((curr_height - new_height) / 2)
        right = int((curr_width + new_width) / 2)
        bottom = int((curr_height + new_height) / 2)
        return left, top, right, bottom


def is_remote(media):
    """Detect if media specified is a url"""
    if re.match(r"^https?://", media):
        return True
    return False


def prepare_image(
    img,
    max_size=(1080, 1350),
    aspect_ratios=(4.0 / 5.0, 90.0 / 47.0),
    save_path=None,
    **kwargs
):
    """
    Prepares an image file for posting.
    Defaults for size and aspect ratio from https://help.instagram.com/1469029763400082

    :param img: file path
    :param max_size: tuple of (max_width,  max_height)
    :param aspect_ratios: single float value or tuple of (min_ratio, max_ratio)
    :param save_path: optional output file path
    :param kwargs:
             - **min_size**: tuple of (min_width,  min_height)
    :return:
    """
    min_size = kwargs.pop("min_size", (320, 167))
    if is_remote(img):
        res = requests.get(img, timeout=5)
        im = Image.open(io.BytesIO(res.content))
    else:
        im = Image.open(img)

    if aspect_ratios:
        crop_box = calc_crop(aspect_ratios, im.size)
        if crop_box:
            im = im.crop(crop_box)

    new_size = calc_resize(max_size, im.size, min_size=min_size)
    if new_size:
        im = im.resize(new_size)

    if im.mode != "RGB":
        # Removes transparency (alpha)
        im = im.convert("RGBA")
        im2 = Image.new("RGB", im.size, (255, 255, 255))
        im2.paste(im, (0, 0), im)
        im = im2
    if save_path:
        im.save(save_path)

    b = io.BytesIO()
    im.save(b, "JPEG")
    return b.getvalue(), im.size


def prepare_video(
    vid,
    thumbnail_frame_ts=0.0,
    max_size=(1080, 1350),
    aspect_ratios=(4.0 / 5.0, 90.0 / 47.0),
    max_duration=60.0,
    save_path=None,
    skip_reencoding=False,
    **kwargs
):
    """
    Prepares a video file for posting.
    Defaults for size and aspect ratio from https://help.instagram.com/1469029763400082

    :param vid: file path
    :param thumbnail_frame_ts: the frame of clip corresponding to time t (in seconds) to be used as the thumbnail
    :param max_size: tuple of (max_width,  max_height)
    :param aspect_ratios: single float value or tuple of (min_ratio, max_ratio)
    :param max_duration: maximum video duration in seconds
    :param save_path: optional output video file path
    :param skip_reencoding: if set to True, the file will not be re-encoded
        if there are no modifications required. Default: False.
    :param kwargs:
         - **min_size**: tuple of (min_width,  min_height)
         - **progress_bar**: bool flag to show/hide progress bar
         - **save_only**: bool flag to return only the path to the saved video file. Requires save_path be set.
         - **preset**: Sets the time that FFMPEG will spend optimizing the compression.
         Choices are: ultrafast, superfast, veryfast, faster, fast, medium,
         slow, slower, veryslow, placebo. Note that this does not impact
         the quality of the video, only the size of the video file. So
         choose ultrafast when you are in a hurry and file size does not matter.
    :return:
    """
    from moviepy.video.fx.all import crop, resize
    from moviepy.video.io.VideoFileClip import VideoFileClip

    min_size = kwargs.pop("min_size", (612, 320))
    progress_bar = True if kwargs.pop("progress_bar", None) else False
    save_only = kwargs.pop("save_only", False)
    preset = kwargs.pop("preset", "medium")
    if save_only and not save_path:
        raise ValueError('"save_path" cannot be empty.')
    if save_path:
        if not save_path.lower().endswith(".mp4"):
            raise ValueError("You must specify a .mp4 save path")

    vid_is_modified = False  # flag to track if re-encoding can be skipped

    temp_video_file = tempfile.NamedTemporaryFile(
        prefix="ipae_", suffix=".mp4", delete=False
    )

    if is_remote(vid):
        # Download remote file
        res = requests.get(vid, timeout=5)
        temp_video_file.write(res.content)
        video_src_filename = temp_video_file.name
    else:
        shutil.copyfile(vid, temp_video_file.name)
        video_src_filename = vid

    vidclip = VideoFileClip(temp_video_file.name)

    if vidclip.duration < 3 * 1.0:
        raise ValueError("Duration is too short")

    if vidclip.duration > max_duration * 1.0:
        vidclip = vidclip.subclip(0, max_duration)
        vid_is_modified = True

    if thumbnail_frame_ts > vidclip.duration:
        raise ValueError("Invalid thumbnail frame")

    if aspect_ratios:
        crop_box = calc_crop(aspect_ratios, vidclip.size)
        if crop_box:
            vidclip = crop(
                vidclip, x1=crop_box[0], y1=crop_box[1], x2=crop_box[2], y2=crop_box[3]
            )
            vid_is_modified = True

    if max_size or min_size:
        new_size = calc_resize(max_size, vidclip.size, min_size=min_size)
        if new_size:
            vidclip = resize(vidclip, newsize=new_size)
            vid_is_modified = True

    temp_vid_output_file = tempfile.NamedTemporaryFile(
        prefix="ipae_", suffix=".mp4", delete=False
    )
    if vid_is_modified or not skip_reencoding:
        # write out
        vidclip.write_videofile(
            temp_vid_output_file.name,
            codec="libx264",
            audio=True,
            audio_codec="aac",
            verbose=False,
            progress_bar=progress_bar,
            preset=preset,
            remove_temp=True,
        )
    else:
        # no reencoding
        shutil.copyfile(video_src_filename, temp_vid_output_file.name)

    if save_path:
        shutil.copyfile(temp_vid_output_file.name, save_path)

    # Temp thumbnail img filename
    temp_thumbnail_file = tempfile.NamedTemporaryFile(
        prefix="ipae_", suffix=".jpg", delete=False
    )
    vidclip.save_frame(temp_thumbnail_file.name, t=thumbnail_frame_ts)

    video_duration = vidclip.duration
    video_size = vidclip.size
    del vidclip  # clear it out

    video_thumbnail_content = temp_thumbnail_file.read()

    if not save_only:
        video_content_len = os.path.getsize(temp_vid_output_file.name)
        video_content = temp_vid_output_file.read()
    else:
        video_content_len = os.path.getsize(save_path)
        video_content = save_path  # return the file path instead

    if video_content_len > 50 * 1024 * 1000:
        raise ValueError("Video file is too big.")

    return video_content, video_size, video_duration, video_thumbnail_content


if __name__ == "__main__":  # pragma: no cover
    # pylint: disable-all
    import argparse

    parser = argparse.ArgumentParser(description="Demo media.py")
    parser.add_argument("-i", "--image", dest="image", type=str)
    parser.add_argument("-v", "--video", dest="video", type=str)
    parser.add_argument("-video-story", dest="videostory", type=str)

    args = parser.parse_args()

    if args.image:
        photo_data, size = prepare_image(
            args.image, max_size=(1000, 800), aspect_ratios=0.9
        )
        print("Image dimensions: {0:d}x{1:d}".format(size[0], size[1]))

    def print_vid_info(video_data, size, duration, thumbnail_data):
        print(
            "vid file size: {0:d}, thumbnail file size: {1:d}, , "
            "vid dimensions: {2:d}x{3:d}, duration: {4:f}".format(
                len(video_data), len(thumbnail_data), size[0], size[1], duration
            )
        )

    if args.video:
        print("Example 1: Resize video to aspect ratio 1, duration 10s")
        video_data, size, duration, thumbnail_data = prepare_video(
            args.video, aspect_ratios=1.0, max_duration=10, save_path="example1.mp4"
        )
        print_vid_info(video_data, size, duration, thumbnail_data)

        print("Example 2: Resize video to no greater than 480x480")
        video_data, size, duration, thumbnail_data = prepare_video(
            args.video, thumbnail_frame_ts=2.0, max_size=(480, 480)
        )
        print_vid_info(video_data, size, duration, thumbnail_data)

        print("Example 3: Leave video intact and speed up retrieval")
        video_data, size, duration, thumbnail_data = prepare_video(
            args.video, max_size=None, skip_reencoding=True
        )
        print_vid_info(video_data, size, duration, thumbnail_data)

    if args.videostory:
        print("Generate a video suitable for posting as a story")
        video_data, size, duration, thumbnail_data = prepare_video(
            args.videostory,
            aspect_ratios=(3.0 / 4),
            max_duration=14.9,
            min_size=(612, 612),
            max_size=(1080, 1080),
            save_path="story.mp4",
        )
        print_vid_info(video_data, size, duration, thumbnail_data)



================================================
FILE: instagrapi/story.py
================================================
import tempfile
from pathlib import Path
from typing import List
from urllib.parse import urlparse

from .types import StoryBuild, StoryMention, StorySticker

try:
    from moviepy import CompositeVideoClip, ImageClip, TextClip, VideoFileClip
except ImportError:
    try:
        from moviepy.editor import (
            CompositeVideoClip,
            ImageClip,
            TextClip,
            VideoFileClip,
        )
    except ImportError:
        raise Exception("Please install moviepy>=1.0.3 and retry")

try:
    from PIL import Image
except ImportError:
    raise Exception("You don't have PIL installed. Please install PIL or Pillow>=8.1.1")


class StoryBuilder:
    """
    Helpers for Story building
    """

    width = 720
    height = 1280

    def __init__(
        self,
        path: Path,
        caption: str = "",
        mentions: List[StoryMention] = [],
        bgpath: Path = None,
    ):
        """
        Initialization function

        Parameters
        ----------
        path: Path
            Path for a file
        caption: str, optional
            Media caption, default value is ""
        mentions: List[StoryMention], optional
            List of mentions to be tagged on this upload, default is empty list
        bgpath: Path
            Path for a background image, default value is ""

        Returns
        -------
        Void
        """
        self.path = Path(path)
        self.caption = caption
        self.mentions = mentions
        self.bgpath = Path(bgpath) if bgpath else None

    def build_main(
        self,
        clip,
        max_duration: int = 0,
        font: str = "Arial",
        fontsize: int = 100,
        color: str = "white",
        link: str = "",
    ) -> StoryBuild:
        """
        Build clip

        Parameters
        ----------
        clip: (VideoFileClip, ImageClip)
            An object of either VideoFileClip or ImageClip
        max_duration: int, optional
            Duration of the clip if a video clip, default value is 0
        font: str, optional
            Name of font for text clip
        fontsize: int, optional
            Size of font
        color: str, optional
            Color of text

        Returns
        -------
        StoryBuild
            An object of StoryBuild
        """
        clips = []
        stickers = []
        # Background
        if self.bgpath:
            assert self.bgpath.exists(), f"Wrong path to background {self.bgpath}"
            background = ImageClip(str(self.bgpath))
            clips.append(background)
        # Media clip
        clip_left = (self.width - clip.size[0]) / 2
        clip_top = (self.height - clip.size[1]) / 2
        if clip_top > 90:
            clip_top -= 50
        media_clip = clip.set_position((clip_left, clip_top))
        clips.append(media_clip)
        mention = self.mentions[0] if self.mentions else None
        # Text clip
        caption = self.caption
        if self.mentions:
            mention = self.mentions[0]
            if getattr(mention, "user", None):
                caption = f"@{mention.user.username}"
        if caption:
            text_clip = TextClip(
                caption,
                color=color,
                font=font,
                kerning=-1,
                fontsize=fontsize,
                method="label",
            )
            text_clip_left = (self.width - 600) / 2
            text_clip_top = clip_top + clip.size[1] + 50
            offset = (text_clip_top + text_clip.size[1]) - self.height
            if offset > 0:
                text_clip_top -= offset + 90
            text_clip = (
                text_clip.resize(width=600)
                .set_position((text_clip_left, text_clip_top))
                .fadein(3)
            )
            clips.append(text_clip)
        if link:
            url = urlparse(link)
            link_clip = TextClip(
                url.netloc,
                color="blue",
                bg_color="white",
                font=font,
                kerning=-1,
                fontsize=32,
                method="label",
            )
            link_clip_left = (self.width - 400) / 2
            link_clip_top = clip.size[1] / 2
            link_clip = (
                link_clip.resize(width=400)
                .set_position((link_clip_left, link_clip_top))
                .fadein(3)
            )
            link_sticker = StorySticker(
                # x=160.0, y=641.0, z=0, width=400.0, height=88.0,
                x=round(link_clip_left / self.width, 7),  # e.g. 0.49953705
                y=round(link_clip_top / self.height, 7),  # e.g. 0.5
                z=0,
                width=round(link_clip.size[0] / self.width, 7),  # e.g. 0.50912
                height=round(link_clip.size[1] / self.height, 7),  # e.g. 0.06875
                rotation=0.0,
                # id="link_sticker_default",
                type="story_link",
                extra=dict(
                    link_type="web",
                    url=str(link),  # e.g. "https//github.com/"
                    tap_state_str_id="link_sticker_default",
                ),
            )
            stickers.append(link_sticker)
            clips.append(link_clip)
        # Mentions
        mentions = []
        if mention:
            mention.x = 0.49892962  # approximately center
            mention.y = (text_clip_top + text_clip.size[1] / 2) / self.height
            mention.width = text_clip.size[0] / self.width
            mention.height = text_clip.size[1] / self.height
            mentions = [mention]
        duration = max_duration
        if getattr(clip, "duration", None):
            if duration > int(clip.duration) or not duration:
                duration = int(clip.duration)
        destination = tempfile.mktemp(".mp4")
        cvc = (
            CompositeVideoClip(clips, size=(self.width, self.height))
            .set_fps(24)
            .set_duration(duration)
        )
        cvc.write_videofile(destination, codec="libx264", audio=True, audio_codec="aac")
        paths = []
        if duration > 15:
            for i in range(duration // 15 + (1 if duration % 15 else 0)):
                path = tempfile.mktemp(".mp4")
                start = i * 15
                rest = duration - start
                end = start + (rest if rest < 15 else 15)
                sub = cvc.subclip(start, end)
                sub.write_videofile(
                    path, codec="libx264", audio=True, audio_codec="aac"
                )
                paths.append(path)
        return StoryBuild(
            mentions=mentions, path=destination, paths=paths, stickers=stickers
        )

    def video(
        self,
        max_duration: int = 0,
        font: str = "Arial",
        fontsize: int = 100,
        color: str = "white",
        link: str = "",
    ):
        """
        Build CompositeVideoClip from source video

        Parameters
        ----------
        max_duration: int, optional
            Duration of the clip if a video clip, default value is 0
        font: str, optional
            Name of font for text clip
        fontsize: int, optional
            Size of font
        color: str, optional
            Color of text

        Returns
        -------
        StoryBuild
            An object of StoryBuild
        """
        clip = VideoFileClip(str(self.path), has_mask=True)
        build = self.build_main(clip, max_duration, font, fontsize, color, link)
        clip.close()
        return build

    def photo(
        self,
        max_duration: int = 0,
        font: str = "Arial",
        fontsize: int = 100,
        color: str = "white",
        link: str = "",
    ):
        """
        Build CompositeVideoClip from source video

        Parameters
        ----------
        max_duration: int, optional
            Duration of the clip if a video clip, default value is 0
        font: str, optional
            Name of font for text clip
        fontsize: int, optional
            Size of font
        color: str, optional
            Color of text

        Returns
        -------
        StoryBuild
            An object of StoryBuild
        """

        with Image.open(self.path) as im:
            image_width, image_height = im.size

        width_reduction_percent = self.width / float(image_width)
        height_in_ratio = int((float(image_height) * float(width_reduction_percent)))

        clip = ImageClip(str(self.path)).resize(
            width=self.width, height=height_in_ratio
        )
        return self.build_main(clip, max_duration or 15, font, fontsize, color, link)



================================================
FILE: instagrapi/types.py
================================================
from datetime import datetime
from typing import Dict, List, Optional, Union

from pydantic import (
    BaseModel,
    ConfigDict,
    FilePath,
    HttpUrl,
    ValidationError,
    field_validator,
)


class TypesBaseModel(BaseModel):
    model_config = ConfigDict(
        coerce_numbers_to_str=True
    )  # (jarrodnorwell) fixed city_id issue


def validate_external_url(cls, v):
    if v is None or (v.startswith("http") and "://" in v) or isinstance(v, str):
        return v
    raise ValidationError(
        "external_url must be a URL or string"
    )  # Corrected 'been' to 'be'


class Resource(TypesBaseModel):
    pk: str
    video_url: Optional[HttpUrl] = None  # for Video and IGTV
    thumbnail_url: HttpUrl
    media_type: int


class BioLink(TypesBaseModel):
    link_id: str
    url: str
    lynx_url: Optional[str] = None
    link_type: Optional[str] = None
    title: Optional[str] = None
    is_pinned: Optional[bool] = None
    open_external_url_with_in_app_browser: Optional[bool] = None


class Broadcast(TypesBaseModel):
    title: str
    thread_igid: str
    subtitle: str
    invite_link: str
    is_member: bool
    group_image_uri: str
    group_image_background_uri: str
    thread_subtype: int
    number_of_members: int
    creator_igid: Optional[str] = None
    creator_username: str


class User(TypesBaseModel):
    pk: str
    username: str
    full_name: str
    is_private: bool
    profile_pic_url: HttpUrl
    profile_pic_url_hd: Optional[HttpUrl] = None
    is_verified: bool
    media_count: int
    follower_count: int
    following_count: int
    biography: Optional[str] = ""
    bio_links: List[BioLink] = []
    external_url: Optional[str] = None
    account_type: Optional[int] = None
    is_business: bool

    broadcast_channel: List[Broadcast] = []

    public_email: Optional[str] = None
    contact_phone_number: Optional[str] = None
    public_phone_country_code: Optional[str] = None
    public_phone_number: Optional[str] = None
    business_contact_method: Optional[str] = None
    business_category_name: Optional[str] = None
    category_name: Optional[str] = None
    category: Optional[str] = None

    address_street: Optional[str] = None
    city_id: Optional[str] = None
    city_name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    zip: Optional[str] = None
    instagram_location_id: Optional[str] = None
    interop_messaging_user_fbid: Optional[str] = None

    @field_validator("external_url")
    @classmethod
    def validate_external_url(cls, v):
        if v is None or (v.startswith("http") and "://" in v) or isinstance(v, str):
            return v
        raise ValidationError("external_url must be a URL or string")


class Account(TypesBaseModel):
    pk: str
    username: str
    full_name: str
    is_private: bool
    profile_pic_url: HttpUrl
    is_verified: bool
    biography: Optional[str] = ""
    external_url: Optional[str] = None
    is_business: bool
    birthday: Optional[str] = None
    phone_number: Optional[str] = None
    gender: Optional[int] = None
    email: Optional[str] = None

    @field_validator("external_url")
    @classmethod
    def validate_external_url(cls, v):
        if v is None or (v.startswith("http") and "://" in v) or isinstance(v, str):
            return v
        raise ValidationError("external_url must be a URL or string")


class UserShort(TypesBaseModel):
    def __hash__(self):
        return hash(self.pk)

    def __eq__(self, other):
        if isinstance(other, UserShort):
            return self.pk == other.pk
        return NotImplemented

    pk: str
    username: Optional[str] = None
    full_name: Optional[str] = ""
    profile_pic_url: Optional[HttpUrl] = None
    profile_pic_url_hd: Optional[HttpUrl] = None
    is_private: Optional[bool] = None
    # is_verified: bool  # not found in hashtag_medias_v1
    # stories: List = [] # not found in fbsearch_suggested_profiles


class Usertag(TypesBaseModel):
    user: UserShort
    x: float
    y: float


class Location(TypesBaseModel):
    pk: Optional[int] = None
    name: str
    phone: Optional[str] = ""
    website: Optional[str] = ""
    category: Optional[str] = ""
    hours: Optional[dict] = {}  # opening hours
    address: Optional[str] = ""
    city: Optional[str] = ""
    zip: Optional[str] = ""
    lng: Optional[float] = None
    lat: Optional[float] = None
    external_id: Optional[int] = None
    external_id_source: Optional[str] = None
    # address_json: Optional[dict] = {}
    # profile_pic_url: Optional[HttpUrl]
    # directory: Optional[dict] = {}


class SharedMediaImageCandidate(TypesBaseModel):
    """Image candidate for shared media clips with video features"""

    estimated_scans_sizes: List[int] = []
    height: int
    scans_profile: str
    url: str
    width: int


class ScrubberSpritesheetInfo(TypesBaseModel):
    """Spritesheet information for video scrubbing"""

    file_size_kb: int
    max_thumbnails_per_sprite: int
    rendered_width: int
    sprite_height: int
    sprite_urls: List[str]
    sprite_width: int
    thumbnail_duration: float
    thumbnail_height: int
    thumbnail_width: int
    thumbnails_per_row: int
    total_thumbnail_num_per_sprite: int
    video_length: float


class ScrubberSpritesheetInfoCandidates(TypesBaseModel):
    """Container for spritesheet information candidates"""

    default: ScrubberSpritesheetInfo


class AdditionalCandidates(TypesBaseModel):
    """Additional candidates structure in image_versions2"""

    first_frame: Optional[SharedMediaImageCandidate] = None
    igtv_first_frame: Optional[SharedMediaImageCandidate] = None
    smart_frame: Optional[SharedMediaImageCandidate] = None


class SharedMediaImageVersions(TypesBaseModel):
    """Complete image_versions2 structure for shared media clips"""

    additional_candidates: Optional[AdditionalCandidates] = None
    candidates: List[SharedMediaImageCandidate] = []
    scrubber_spritesheet_info_candidates: Optional[
        ScrubberSpritesheetInfoCandidates
    ] = None


class ClipsAchievementsInfo(TypesBaseModel):
    """Information about achievements in clips"""

    num_earned_achievements: Optional[int] = None
    show_achievements: bool = False


class AudioReattributionInfo(TypesBaseModel):
    """Audio reattribution settings"""

    should_allow_restore: bool = False


class ClipsAdditionalAudioInfo(TypesBaseModel):
    """Additional audio information for clips"""

    additional_audio_username: Optional[str] = None
    audio_reattribution_info: AudioReattributionInfo


class ClipsAudioRankingInfo(TypesBaseModel):
    """Audio ranking information for clips"""

    best_audio_cluster_id: str


class ClipsBrandedContentTagInfo(TypesBaseModel):
    """Branded content tag information for clips"""

    can_add_tag: bool = False


class ClipsContentAppreciationInfo(TypesBaseModel):
    """Content appreciation information for clips"""

    enabled: bool = False
    entry_point_container: Optional[str] = None


class ClipsMashupInfo(TypesBaseModel):
    """Mashup information for clips"""

    can_toggle_mashups_allowed: bool = False
    formatted_mashups_count: Optional[str] = None
    has_been_mashed_up: bool = False
    has_nonmimicable_additional_audio: bool = False
    is_creator_requesting_mashup: bool = False
    is_light_weight_check: bool = True
    is_light_weight_reuse_allowed_check: bool = False
    is_pivot_page_available: bool = False
    is_reuse_allowed: bool = True
    mashup_type: Optional[str] = None
    mashups_allowed: bool = True
    non_privacy_filtered_mashups_media_count: int = 0
    privacy_filtered_mashups_media_count: Optional[int] = None
    original_media: Optional[dict] = None


class ClipsConsumptionInfo(TypesBaseModel):
    """Consumption information for clips original sound"""

    display_media_id: Optional[str] = None
    is_bookmarked: bool = False
    is_trending_in_clips: bool = False
    should_mute_audio_reason: str = ""
    should_mute_audio_reason_type: Optional[str] = None
    user_notes: Optional[str] = None


class ClipsFbDownstreamUseXpostMetadata(TypesBaseModel):
    """Facebook downstream use xpost metadata for clips"""

    downstream_use_xpost_deny_reason: str = "NONE"


class ClipsIgArtist(TypesBaseModel):
    """Instagram artist information for clips original sound"""

    pk: int
    pk_id: str
    id: str
    username: str
    full_name: str
    is_private: bool = False
    is_verified: bool = False
    profile_pic_id: str
    profile_pic_url: str
    strong_id__: str


class ClipsOriginalSoundInfo(TypesBaseModel):
    """Original sound information for clips"""

    allow_creator_to_rename: bool = True
    audio_asset_id: int
    attributed_custom_audio_asset_id: Optional[int] = None
    can_remix_be_shared_to_fb: bool = True
    can_remix_be_shared_to_fb_expansion: bool = True
    dash_manifest: str
    duration_in_ms: int
    formatted_clips_media_count: Optional[str] = None
    hide_remixing: bool = False
    is_audio_automatically_attributed: bool = False
    is_eligible_for_audio_effects: bool = True
    is_eligible_for_vinyl_sticker: bool = True
    is_explicit: bool = False
    is_original_audio_download_eligible: bool = True
    is_reuse_disabled: bool = False
    is_xpost_from_fb: bool = False
    music_canonical_id: Optional[str] = None
    oa_owner_is_music_artist: bool = False
    original_audio_subtype: str = "default"
    original_audio_title: str = "Original audio"
    original_media_id: int
    progressive_download_url: str
    should_mute_audio: bool = False
    time_created: int
    trend_rank: Optional[int] = None
    previous_trend_rank: Optional[int] = None
    overlap_duration_in_ms: Optional[int] = None
    audio_asset_start_time_in_ms: Optional[int] = None
    ig_artist: ClipsIgArtist
    audio_filter_infos: List[dict] = []
    audio_parts: List[dict] = []
    audio_parts_by_filter: List[dict] = []
    consumption_info: ClipsConsumptionInfo
    xpost_fb_creator_info: Optional[dict] = None
    fb_downstream_use_xpost_metadata: ClipsFbDownstreamUseXpostMetadata


class ClipsMetadata(TypesBaseModel):
    """Complete clips metadata structure for Media objects"""

    clips_creation_entry_point: str = "clips"
    featured_label: Optional[str] = None
    is_public_chat_welcome_video: bool = False
    professional_clips_upsell_type: int = 0
    show_tips: Optional[str] = None
    achievements_info: ClipsAchievementsInfo
    additional_audio_info: ClipsAdditionalAudioInfo
    asset_recommendation_info: Optional[dict] = None
    audio_ranking_info: ClipsAudioRankingInfo
    audio_type: str = "original_sounds"
    branded_content_tag_info: ClipsBrandedContentTagInfo
    breaking_content_info: Optional[dict] = None
    breaking_creator_info: Optional[dict] = None
    challenge_info: Optional[dict] = None
    content_appreciation_info: ClipsContentAppreciationInfo
    contextual_highlight_info: Optional[dict] = None
    cutout_sticker_info: List[dict] = []
    disable_use_in_clips_client_cache: bool = False
    external_media_info: Optional[dict] = None
    is_fan_club_promo_video: bool = False
    is_shared_to_fb: bool = False
    mashup_info: ClipsMashupInfo
    merchandising_pill_info: Optional[dict] = None
    music_canonical_id: str
    music_info: Optional[dict] = None
    nux_info: Optional[dict] = None
    original_sound_info: Optional[ClipsOriginalSoundInfo] = None
    originality_info: Optional[dict] = None
    reels_on_the_rise_info: Optional[dict] = None
    reusable_text_attribute_string: Optional[str] = None
    reusable_text_info: Optional[dict] = None
    shopping_info: Optional[dict] = None
    show_achievements: bool = False
    template_info: Optional[dict] = None
    may_have_template_info: Optional[dict] = None
    viewer_interaction_settings: Optional[dict] = None


class Media(TypesBaseModel):
    pk: Union[str, int]
    id: str
    code: str
    taken_at: datetime
    media_type: int
    image_versions2: Optional[SharedMediaImageVersions] = None
    product_type: Optional[str] = ""  # igtv or feed
    thumbnail_url: Optional[HttpUrl] = None
    location: Optional[Location] = None
    user: UserShort
    comment_count: Optional[int] = 0
    comments_disabled: Optional[bool] = False
    commenting_disabled_for_viewer: Optional[bool] = False
    like_count: int
    play_count: Optional[int] = None
    has_liked: Optional[bool] = None
    caption_text: str
    accessibility_caption: Optional[str] = None
    usertags: List[Usertag]
    sponsor_tags: List[UserShort]
    video_url: Optional[HttpUrl] = None  # for Video and IGTV
    view_count: Optional[int] = 0  # for Video and IGTV
    video_duration: Optional[float] = 0.0  # for Video and IGTV
    title: Optional[str] = ""
    resources: List[Resource] = []
    clips_metadata: Optional[ClipsMetadata] = None


class MediaXma(TypesBaseModel):
    # media_type: int
    video_url: HttpUrl  # for Video and IGTV
    title: Optional[str] = ""
    preview_url: Optional[str] = None
    preview_url_mime_type: Optional[str] = None
    header_icon_url: Optional[str] = None
    header_icon_width: Optional[int] = None
    header_icon_height: Optional[int] = None
    header_title_text: Optional[str] = None
    preview_media_fbid: Optional[str] = None

    @field_validator("preview_url", "header_icon_url")
    @classmethod
    def validate_url_fields(cls, v):
        """Validate URL fields allowing None, valid URLs, or any string"""
        if v is None or (v.startswith("http") and "://" in v) or isinstance(v, str):
            return v
        raise ValidationError("URL field must be a URL or string")


class MediaOembed(TypesBaseModel):
    title: str
    author_name: str
    author_url: str
    author_id: str
    media_id: str
    provider_name: str
    provider_url: HttpUrl
    type: str
    width: Optional[int] = None
    height: Optional[int] = None
    html: str
    thumbnail_url: HttpUrl
    thumbnail_width: int
    thumbnail_height: int
    can_view: bool


class Collection(TypesBaseModel):
    id: str
    name: str
    type: str
    media_count: int


class Comment(TypesBaseModel):
    pk: str
    text: str
    user: UserShort
    created_at_utc: datetime
    content_type: str
    status: str
    replied_to_comment_id: Optional[str] = None
    has_liked: Optional[bool] = None
    like_count: Optional[int] = None


class Hashtag(TypesBaseModel):
    id: str
    name: str
    media_count: Optional[int] = None
    profile_pic_url: Optional[HttpUrl] = None


class StoryMention(TypesBaseModel):
    user: UserShort
    x: Optional[float] = None
    y: Optional[float] = None
    width: Optional[float] = None
    height: Optional[float] = None
    rotation: Optional[float] = None


class StoryMedia(TypesBaseModel):
    # Instagram does not return the feed_media object when requesting story,
    # so you will have to make an additional request to get media and this is overhead:
    # media: Media
    x: float = 0.5
    y: float = 0.4997396
    z: float = 0
    width: float = 0.8
    height: float = 0.60572916
    rotation: float = 0.0
    is_pinned: Optional[bool] = None
    is_hidden: Optional[bool] = None
    is_sticker: Optional[bool] = None
    is_fb_sticker: Optional[bool] = None
    media_pk: int
    user_id: Optional[int] = None
    product_type: Optional[str] = None
    media_code: Optional[str] = None


class StoryHashtag(TypesBaseModel):
    hashtag: Hashtag
    x: Optional[float] = None
    y: Optional[float] = None
    width: Optional[float] = None
    height: Optional[float] = None
    rotation: Optional[float] = None


class StoryLocation(TypesBaseModel):
    location: Location
    x: Optional[float] = None
    y: Optional[float] = None
    width: Optional[float] = None
    height: Optional[float] = None
    rotation: Optional[float] = None


class StoryStickerLink(TypesBaseModel):
    url: HttpUrl
    link_title: Optional[str] = None
    link_type: Optional[str] = None
    display_url: Optional[str] = None


class StorySticker(TypesBaseModel):
    id: Optional[str] = None
    type: Optional[str] = "gif"
    x: float
    y: float
    z: Optional[int] = 1000005
    width: float
    height: float
    rotation: Optional[float] = 0.0
    story_link: Optional[StoryStickerLink] = None
    extra: Optional[dict] = {}


class StoryPoll(TypesBaseModel):
    id: Optional[str] = None
    type: Optional[str] = "poll"
    x: float
    y: float
    z: Optional[int] = 0
    width: float
    height: float
    rotation: Optional[float] = 0.0
    is_multi_option: Optional[bool] = True
    is_shared_result: Optional[bool] = False
    viewer_can_vote: Optional[bool] = True
    finished: Optional[bool] = False
    color: Optional[str] = "black"
    poll_type: Optional[str] = ""
    question: str
    options: list
    extra: Optional[dict] = {}


class StoryBuild(TypesBaseModel):
    mentions: List[StoryMention]
    path: FilePath
    paths: List[FilePath] = []
    stickers: List[StorySticker] = []


class StoryLink(TypesBaseModel):
    webUri: HttpUrl
    x: float = 0.5126011
    y: float = 0.5168225
    z: float = 0.0
    width: float = 0.50998676
    height: float = 0.25875
    rotation: float = 0.0


class Story(TypesBaseModel):
    pk: str
    id: str
    code: str
    taken_at: datetime
    imported_taken_at: Optional[datetime] = None
    media_type: int
    product_type: Optional[str] = ""
    thumbnail_url: Optional[HttpUrl] = None
    user: UserShort
    video_url: Optional[HttpUrl] = None  # for Video and IGTV
    video_duration: Optional[float] = 0.0  # for Video and IGTV
    sponsor_tags: List[UserShort]
    is_paid_partnership: Optional[bool] = False
    mentions: List[StoryMention]
    links: List[StoryLink]
    hashtags: List[StoryHashtag]
    locations: List[StoryLocation]
    stickers: List[StorySticker]
    medias: List[StoryMedia] = []
    polls: List[StoryPoll] = []


class Guide(TypesBaseModel):
    id: Optional[str] = None
    title: Optional[str] = None
    description: str
    cover_media: Media
    feedback_item: Optional[dict] = None


class DirectMedia(TypesBaseModel):
    id: str
    media_type: int
    user: Optional[UserShort] = None
    thumbnail_url: Optional[HttpUrl] = None
    video_url: Optional[HttpUrl] = None
    audio_url: Optional[HttpUrl] = None


class MessageReaction(TypesBaseModel):
    """Individual emoji reaction on a direct message"""

    timestamp: datetime
    client_context: Optional[str] = None
    sender_id: int
    emoji: str
    super_react_type: str = "none"


class MessageReactions(TypesBaseModel):
    """Reactions structure for direct messages"""

    likes: List[dict] = []  # Structure unknown from current examples
    likes_count: Optional[int] = 0
    emojis: List[MessageReaction] = []


class LinkContext(TypesBaseModel):
    """Link context metadata for direct message links"""

    link_url: str
    link_title: Optional[str] = ""
    link_summary: Optional[str] = ""
    link_image_url: Optional[str] = ""


class MessageLink(TypesBaseModel):
    """Link structure for direct messages"""

    text: str
    link_context: LinkContext
    client_context: Optional[str] = None
    mutation_token: Optional[str] = None


class DisappearingMessagesSeenState(TypesBaseModel):
    """Disappearing messages seen state information"""

    item_id: str
    timestamp: datetime
    created_at: datetime


class LastSeenInfo(TypesBaseModel):
    """Last seen information for a user in a direct thread"""

    item_id: str
    timestamp: datetime
    created_at: datetime
    shh_seen_state: dict = {}
    disappearing_messages_seen_state: Optional[DisappearingMessagesSeenState] = None


class FallbackUrl(TypesBaseModel):
    """Fallback URL structure for media candidates"""

    url: str


class DirectMessageImageCandidate(TypesBaseModel):
    """Image candidate for ephemeral visual media in direct messages"""

    width: int
    height: int
    url: str
    scans_profile: Optional[str] = None
    fallback: Optional[FallbackUrl] = None
    url_expiration_timestamp_us: Optional[datetime] = None


class DirectMessageImageVersions(TypesBaseModel):
    """Image versions for ephemeral visual media in direct messages"""

    candidates: List[DirectMessageImageCandidate] = []


class VideoVersion(TypesBaseModel):
    """Individual video version with specific resolution and quality"""

    id: Optional[str] = ""
    type: Optional[int] = None
    width: int
    height: int
    url: str
    fallback: Optional[FallbackUrl] = None
    url_expiration_timestamp_us: Optional[datetime] = None
    bandwidth: Optional[int] = 0


class FriendshipStatus(TypesBaseModel):
    """Friendship status information for visual media user"""

    blocking: bool = False
    is_messaging_only_blocking: bool = False
    is_messaging_pseudo_blocking: bool = False
    is_unavailable: bool = False


class VisualMediaUser(TypesBaseModel):
    """User information in visual media (enhanced UserShort)"""

    id: str
    strong_id__: Optional[str] = None
    pk: int
    pk_id: str
    full_name: str
    username: str
    account_type: Optional[int] = None
    short_name: Optional[str] = None
    profile_pic_url: str
    is_verified: bool = False
    interop_messaging_user_fbid: Optional[int] = None
    fbid_v2: Optional[int] = None
    has_ig_profile: bool = True
    interop_user_type: Optional[int] = 0
    is_using_unified_inbox_for_direct: bool = False
    is_private: bool = False
    is_creator_agent_enabled: bool = False
    is_creator_automated_response_enabled: bool = False
    friendship_status: Optional[FriendshipStatus] = None
    is_shared_account: bool = False
    is_shared_account_with_messaging_access: bool = False
    ai_agent_banner_type: Optional[str] = None
    is_eligible_for_ai_bot_group_chats: bool = False


class ExpiringMediaActionSummary(TypesBaseModel):
    """Summary of expiring media actions"""

    type: str
    timestamp: datetime
    count: int


class VisualMediaContent(TypesBaseModel):
    """Content structure for visual media (can be rich or minimal)"""

    media_type: int  # Always present: 1=image, 2=video
    id: Optional[str] = None
    media_id: Optional[int] = None
    image_versions2: Optional[DirectMessageImageVersions] = None
    video_versions: Optional[List[VideoVersion]] = None
    original_width: Optional[int] = None
    original_height: Optional[int] = None
    user: Optional[VisualMediaUser] = None
    organic_tracking_token: Optional[str] = None
    video_duration: Optional[int] = None
    video_dash_manifest: Optional[str] = None
    is_dash_eligible: Optional[int] = None
    create_mode_attribution: Optional[dict] = None
    creative_config: Optional[dict] = None
    expiring_media_action_summary: Optional[ExpiringMediaActionSummary] = None


class VisualMedia(TypesBaseModel):
    """Complete visual media structure for direct messages"""

    media: VisualMediaContent
    seen_user_ids: List[str] = []
    seen_count: int = 0
    view_mode: str  # 'replayable', 'permanent', etc.
    replay_expiring_at_us: Optional[int] = None
    reply_type: Optional[str] = None
    url_expire_at_secs: Optional[int] = None
    story_app_attribution: Optional[dict] = None
    playback_duration_secs: Optional[int] = None
    tap_models: List[dict] = []
    expiring_media_action_summary: Optional[ExpiringMediaActionSummary] = None


class ReplyMessage(TypesBaseModel):
    id: str
    user_id: Optional[str] = None
    timestamp: datetime
    item_type: Optional[str] = None
    is_sent_by_viewer: Optional[bool] = None
    is_shh_mode: Optional[bool] = None
    text: Optional[str] = None
    link: Optional[dict] = None
    animated_media: Optional[dict] = None
    media: Optional[DirectMedia] = None
    visual_media: Optional[VisualMedia] = None
    media_share: Optional[Media] = None
    reel_share: Optional[dict] = None
    story_share: Optional[dict] = None
    felix_share: Optional[dict] = None
    xma_share: Optional[MediaXma] = None
    clip: Optional[Media] = None
    placeholder: Optional[dict] = None


class DirectMessage(TypesBaseModel):
    id: str  # e.g. 28597946203914980615241927545176064
    user_id: Optional[str] = None
    thread_id: Optional[int] = None  # e.g. 340282366841710300949128531777654287254
    timestamp: datetime
    item_type: Optional[str] = None
    is_sent_by_viewer: Optional[bool] = None
    is_shh_mode: Optional[bool] = None
    reactions: Optional[MessageReactions] = None
    text: Optional[str] = None
    reply: Optional[ReplyMessage] = None
    link: Optional[MessageLink] = None
    animated_media: Optional[dict] = None
    media: Optional[DirectMedia] = None
    visual_media: Optional[VisualMedia] = None
    media_share: Optional[Media] = None
    reel_share: Optional[dict] = None
    story_share: Optional[dict] = None
    felix_share: Optional[dict] = None
    xma_share: Optional[MediaXma] = None
    clip: Optional[Media] = None
    placeholder: Optional[dict] = None
    client_context: Optional[str] = None


class DirectResponse(TypesBaseModel):
    unseen_count: Optional[int] = None
    unseen_count_ts: Optional[int] = None
    status: Optional[str] = None


class DirectShortThread(TypesBaseModel):
    id: str
    users: List[UserShort]
    named: bool
    thread_title: str
    pending: bool
    thread_type: str
    viewer_id: str
    is_group: bool


class DirectThread(TypesBaseModel):
    pk: str  # thread_v2_id, e.g. 17898572618026348
    id: str  # thread_id, e.g. 340282366841510300949128268610842297468
    messages: List[DirectMessage]
    users: List[UserShort]
    inviter: Optional[UserShort] = None
    left_users: List[UserShort] = []
    admin_user_ids: list
    last_activity_at: datetime
    muted: bool
    is_pin: Optional[bool] = None
    named: bool
    canonical: bool
    pending: bool
    archived: bool
    thread_type: str
    thread_title: str
    folder: int
    vc_muted: bool
    is_group: bool
    mentions_muted: bool
    approval_required_for_new_members: bool
    input_mode: int
    business_thread_folder: int
    read_state: int
    is_close_friend_thread: bool
    assigned_admin_id: int
    shh_mode_enabled: bool
    last_seen_at: Dict[str, LastSeenInfo] = {}

    def is_seen(self, user_id: str):
        """Have I seen this thread?
        :param user_id: You account user_id
        """
        user_id = str(user_id)
        if user_id not in self.last_seen_at:
            return False
        own_timestamp = self.last_seen_at[user_id].timestamp.timestamp()
        timestamps = [
            (v.timestamp.timestamp() - own_timestamp) > 0
            for k, v in self.last_seen_at.items()
            if k != user_id
        ]
        return not any(timestamps)


class Relationship(TypesBaseModel):
    user_id: str
    blocking: bool
    followed_by: bool
    following: bool
    incoming_request: bool
    is_bestie: bool
    is_blocking_reel: bool
    is_muting_reel: bool
    is_private: bool
    is_restricted: bool
    muting: bool
    outgoing_request: bool


class RelationshipShort(TypesBaseModel):
    user_id: str
    following: bool
    incoming_request: bool
    is_bestie: bool
    is_feed_favorite: bool
    is_private: bool
    is_restricted: bool
    outgoing_request: bool


class Highlight(TypesBaseModel):
    pk: str  # 17895485401104052
    id: str  # highlight:17895485401104052
    latest_reel_media: int
    cover_media: dict
    user: UserShort
    title: str
    created_at: datetime
    is_pinned_highlight: bool
    media_count: int
    media_ids: List[int] = []
    items: List[Story] = []


class Share(TypesBaseModel):
    pk: str
    type: str


class Track(TypesBaseModel):
    id: str
    title: str
    subtitle: str
    display_artist: str
    audio_cluster_id: int
    artist_id: Optional[int] = None
    cover_artwork_uri: Optional[HttpUrl] = None
    cover_artwork_thumbnail_uri: Optional[HttpUrl] = None
    progressive_download_url: Optional[HttpUrl] = None
    fast_start_progressive_download_url: Optional[HttpUrl] = None
    reactive_audio_download_url: Optional[HttpUrl] = None
    highlight_start_times_in_ms: List[int]
    is_explicit: bool
    dash_manifest: str
    uri: Optional[HttpUrl] = None
    has_lyrics: bool
    audio_asset_id: int
    duration_in_ms: int
    dark_message: Optional[str] = None
    allows_saving: bool
    territory_validity_periods: dict


class Note(TypesBaseModel):
    id: str
    text: str
    user_id: str
    user: UserShort
    audience: int
    created_at: datetime
    expires_at: datetime
    is_emoji_only: bool
    has_translation: bool
    note_style: int



================================================
FILE: instagrapi/utils.py
================================================
import datetime
import enum
import json
import random
import string
import time
import urllib.parse
from typing import Any, TypeVar, Union, overload

from .exceptions import ValidationError


class InstagramIdCodec:
    ENCODING_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"

    @staticmethod
    def encode(num, alphabet=ENCODING_CHARS):
        """Covert a numeric value to a shortcode."""
        num = int(num)
        if num == 0:
            return alphabet[0]
        arr = []
        base = len(alphabet)
        while num:
            rem = num % base
            num //= base
            arr.append(alphabet[rem])
        arr.reverse()
        return "".join(arr)

    @staticmethod
    def decode(shortcode, alphabet=ENCODING_CHARS):
        """Covert a shortcode to a numeric value."""
        base = len(alphabet)
        strlen = len(shortcode)
        num = 0
        idx = 0
        for char in shortcode:
            power = strlen - (idx + 1)
            num += alphabet.index(char) * (base**power)
            idx += 1
        return num


class InstagrapiJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, enum.Enum):
            return obj.value
        elif isinstance(obj, datetime.time):
            return obj.strftime("%H:%M")
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return int(obj.strftime("%s"))
        elif isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


def generate_signature(data):
    """Generate signature of POST data for Private API

    Returns
    -------
    str
        e.g. "signed_body=SIGNATURE.test"
    """
    return "signed_body=SIGNATURE.{data}".format(data=urllib.parse.quote_plus(data))


T = TypeVar('T')


# Overload for when no default is provided - could return Any or None
@overload
def json_value(data: dict, *args: Union[str, int]) -> Any:
    ...


# Overload for when default is provided - returns either found value or default type
@overload
def json_value(data: dict, *args: Union[str, int], default: T) -> Union[T, Any]:
    ...


def json_value(data: dict, *args: Union[str, int], default: Any = None) -> Any:
    """Navigate through nested dictionaries/lists using provided keys.

    Args:
        data: The dictionary to navigate
        *args: Keys/indices to navigate through (strings for dicts, ints for lists)
        default: Value to return if navigation fails

    Returns:
        The value found at the specified path, or default if not found
    """
    cur: Any = data
    for a in args:
        try:
            if isinstance(a, int):
                cur = cur[a]
            else:
                cur = cur.get(a)
            if cur is None:
                return default
        except (IndexError, KeyError, TypeError, AttributeError):
            return default
    return cur


def gen_token(size=10, symbols=False):
    """Gen CSRF or something else token"""
    chars = string.ascii_letters + string.digits
    if symbols:
        chars += string.punctuation
    return "".join(random.choice(chars) for _ in range(size))


def gen_password(size=10):
    """Gen password"""
    return gen_token(size)


def dumps(data):
    """Json dumps format as required Instagram"""
    return InstagrapiJSONEncoder(separators=(",", ":")).encode(data)


def generate_jazoest(symbols: str) -> str:
    amount = sum(ord(s) for s in symbols)
    return f"2{amount}"


def date_time_original(localtime):
    # return time.strftime("%Y:%m:%d+%H:%M:%S", localtime)
    return time.strftime("%Y%m%dT%H%M%S.000Z", localtime)


def random_delay(delay_range: list):
    """Trigger sleep of a random floating number in range min_sleep to max_sleep"""
    return time.sleep(random.uniform(delay_range[0], delay_range[1]))


def vassert(pred, message):
    if not pred:
        raise ValidationError(message)



================================================
FILE: instagrapi/zones.py
================================================
from datetime import timedelta, tzinfo


class CET(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=1)

    def dst(self, dt):
        return timedelta(hours=2)


class UTC(tzinfo):
    def utcoffset(self, dt):
        return timedelta(0)

    def dst(self, dt):
        return timedelta(0)



================================================
FILE: instagrapi/mixins/__init__.py
================================================
[Empty file]


================================================
FILE: instagrapi/mixins/account.py
================================================
import json
from json.decoder import JSONDecodeError
from pathlib import Path
from typing import Dict

import requests

from instagrapi.exceptions import ClientError, ClientLoginRequired
from instagrapi.extractors import extract_account, extract_user_short
from instagrapi.types import Account, UserShort
from instagrapi.utils import dumps, gen_token, generate_signature


class AccountMixin:
    """
    Helper class to manage your account
    """

    def reset_password(self, username: str) -> Dict:
        """
        Reset your password

        Returns
        -------
        Dict
            Jsonified response from Instagram
        """
        response = requests.post(
            "https://www.instagram.com/accounts/account_recovery_send_ajax/",
            data={"email_or_username": username, "recaptcha_challenge_field": ""},
            headers={
                "x-requested-with": "XMLHttpRequest",
                "x-csrftoken": gen_token(),
                "Connection": "Keep-Alive",
                "Accept": "*/*",
                "Accept-Encoding": "gzip,deflate",
                "Accept-Language": "en-US",
                "User-Agent": (
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) "
                    "AppleWebKit/605.1.15 (KHTML, like Gecko) "
                    "Version/11.1.2 Safari/605.1.15"
                ),
            },
            proxies=self.public.proxies,
            timeout=self.request_timeout,
        )
        try:
            return response.json()
        except JSONDecodeError as e:
            if "/login/" in response.url:
                raise ClientLoginRequired(e, response=response)
            raise ClientError(e, response=response)

    def account_info(self) -> Account:
        """
        Fetch your account info

        Returns
        -------
        Account
            An object of Account class
        """
        result = self.private_request("accounts/current_user/?edit=true")
        return extract_account(result["user"])

    def change_password(
        self,
        old_password: str,
        new_password: str,
    ) -> bool:
        """
        Change password

        Parameters
        ----------
        new_password: str
            New password
        old_password: str
            Old password

        Returns
        -------
        bool
            A boolean value
        """
        try:
            enc_old_password = self.password_encrypt(old_password)
            enc_new_password = self.password_encrypt(new_password)
            data = {
                "enc_old_password": enc_old_password,
                "enc_new_password1": enc_new_password,
                "enc_new_password2": enc_new_password,
            }
            self.with_action_data(
                {
                    "_uid": self.user_id,
                    "_uuid": self.uuid,
                    "_csrftoken": self.token,
                }
            )
            result = self.private_request("accounts/change_password/", data=data)
            return result
        except Exception as e:
            self.logger.exception(e)
            return False

    def remove_bio_links(self, link_ids: list[int]) -> dict:
        signed_body = {
            "signed_body": "SIGNATURE." + json.dumps(
                {
                    "_uid": self.user_id,
                    "_uuid": self.uuid,
                    "link_ids": link_ids
                }
            )
        }
        return self.private_request('accounts/remove_bio_links/', data=signed_body, with_signature=False)

    def set_external_url(self, external_url) -> dict:
        """
        Set new biography
        """
        data = dumps(
            {
                "updated_links": dumps(
                    [{"url": external_url, "title": "", "link_type": "external"}]
                ),
                "_uid": self.user_id,
                "_uuid": self.uuid,
            }
        )
        return self.private_request(
            "accounts/update_bio_links/",
            data=generate_signature(data),
            with_signature=False,
        )

    def account_set_private(self) -> bool:
        """
        Sets your account private

        Returns
        -------
        Account
            An object of Account class
        """
        assert self.user_id, "Login required"
        user_id = str(self.user_id)
        data = self.with_action_data({"_uid": user_id, "_uuid": self.uuid})
        result = self.private_request("accounts/set_private/", data)
        return result["status"] == "ok"

    def account_set_public(self) -> bool:
        """
        Sets your account public

        Returns
        -------
        Account
            An object of Account class
        """
        assert self.user_id, "Login required"
        user_id = str(self.user_id)
        data = self.with_action_data({"_uid": user_id, "_uuid": self.uuid})
        result = self.private_request("accounts/set_public/", data)
        return result["status"] == "ok"

    def account_security_info(self) -> dict:
        """
        Fetch your account security info

        Returns
        -------
        dict
            Contains useful information on security settings: {
            "is_phone_confirmed": true,
            "is_two_factor_enabled": false,
            "is_totp_two_factor_enabled": true,
            "is_trusted_notifications_enabled": true,
            "is_eligible_for_whatsapp_two_factor": true,
            "is_whatsapp_two_factor_enabled": false,
            "backup_codes": [...],
            "trusted_devices": [],
            "has_reachable_email": true,
            "eligible_for_trusted_notifications": true,
            "is_eligible_for_multiple_totp": false,
            "totp_seeds": [],
            "can_add_additional_totp_seed": false
            }
        """
        return self.private_request(
            "accounts/account_security_info/", self.with_default_data({})
        )

    def account_edit(self, **data: Dict) -> Account:
        """
        Edit your profile (authorized account)

        Parameters
        ----------
        data: Dict
            Fields you want to edit in your account as key and value pairs

        Returns
        -------
        Account
            An object of Account class
        """
        fields = (
            "external_url",
            "username",
            "full_name",
            "biography",
            "phone_number",
            "email",
        )
        # if "email" in data:
        #     # email is handled separately
        #     self.send_confirm_email(data.pop("email"))
        # if "phone_number" in data:
        #     # phone_number is handled separately
        #     self.send_confirm_phone_number(data.pop("phone_number"))
        data = {key: val for key, val in data.items() if key in fields}
        if "email" not in data or "phone_number" not in data:
            # Instagram Error: You need an email or confirmed phone number.
            user_data = self.account_info().dict()
            user_data = {field: user_data[field] for field in fields}
            data = dict(user_data, **data)
        full_name = data.pop("full_name", None)
        if full_name:
            # Instagram original field-name for full user name is "first_name"
            data["first_name"] = full_name
        # Biography with entities (markup)
        result = self.private_request(
            "accounts/edit_profile/", self.with_default_data(data)
        )
        biography = data.get("biography")
        if biography:
            self.account_set_biography(biography)
        return extract_account(result["user"])

    def account_set_biography(self, biography: str) -> bool:
        """
        Set biography with entities (markup)

        Parameters
        ----------
        biography: str
            Biography raw text

        Returns
        -------
        bool
            A boolean value
        """
        data = {"logged_in_uids": dumps([str(self.user_id)]), "raw_text": biography}
        result = self.private_request(
            "accounts/set_biography/", self.with_default_data(data)
        )
        return result["status"] == "ok"

    def account_change_picture(self, path: Path) -> UserShort:
        """
        Change photo for your profile (authorized account)

        Parameters
        ----------
        path: Path
            Path to the image you want to update as your profile picture

        Returns
        -------
        UserShort
            An object of UserShort class
        """
        upload_id, _, _ = self.photo_rupload(Path(path))
        result = self.private_request(
            "accounts/change_profile_picture/",
            self.with_default_data({"use_fbuploader": True, "upload_id": upload_id}),
        )
        return extract_user_short(result["user"])

    def news_inbox_v1(self, mark_as_seen: bool = False) -> dict:
        """
        Get old and new stories as is

        Parameters
        ----------
        mark_as_seen: bool
            Mark as seen or not

        Returns
        -------
        dict
        """
        return self.private_request(
            "news/inbox/", params={"mark_as_seen": mark_as_seen}
        )

    def send_confirm_email(self, email: str) -> dict:
        """
        Send confirmation code to new email address

        Parameters
        ----------
        email: str
            Email address

        Returns
        -------
        dict
        """
        return self.private_request(
            "accounts/send_confirm_email/",
            self.with_extra_data(
                {"send_source": "personal_information", "email": email}
            ),
        )

    def send_confirm_phone_number(self, phone_number: str) -> dict:
        """
        Send confirmation code to new phone number

        Parameters
        ----------
        phone_number: str
            Phone number

        Returns
        -------
        dict
        """
        return self.private_request(
            "accounts/initiate_phone_number_confirmation/",
            self.with_extra_data(
                {
                    "android_build_type": "release",
                    "send_source": "edit_profile",
                    "phone_number": phone_number,
                }
            ),
        )



================================================
FILE: instagrapi/mixins/album.py
================================================
import time
from pathlib import Path
from typing import Dict, List
from urllib.parse import urlparse

from instagrapi.exceptions import (
    AlbumConfigureError,
    AlbumNotDownload,
    AlbumUnknownFormat,
)
from instagrapi.extractors import extract_media_v1
from instagrapi.types import Location, Media, Usertag
from instagrapi.utils import date_time_original, dumps


class DownloadAlbumMixin:
    """
    Helper class to download album
    """

    def album_download(self, media_pk: int, folder: Path = "") -> List[Path]:
        """
        Download your album

        Parameters
        ----------
        media_pk: int
            PK for the album you want to download
        folder: Path, optional
            Directory in which you want to download the album, default is ""
            and will download the files to working directory.

        Returns
        -------
        List[Path]
            List of path for all the files downloaded
        """
        media = self.media_info(media_pk)
        assert media.media_type == 8, "Must been album"
        paths = []
        for resource in media.resources:
            filename = f"{media.user.username}_{resource.pk}"
            if resource.media_type == 1:
                paths.append(
                    self.photo_download_by_url(resource.thumbnail_url, filename, folder)
                )
            elif resource.media_type == 2:
                paths.append(
                    self.video_download_by_url(resource.video_url, filename, folder)
                )
            else:
                raise AlbumNotDownload(
                    'Media type "{resource.media_type}" unknown for album (resource={resource.pk})'
                )
        return paths

    def album_download_by_urls(self, urls: List[str], folder: Path = "") -> List[Path]:
        """
        Download your album using specified URLs

        Parameters
        ----------
        urls: List[str]
            List of URLs to download media from
        folder: Path, optional
            Directory in which you want to download the album, default is ""
            and will download the files to working directory.

        Returns
        -------
        List[Path]
            List of path for all the files downloaded
        """
        paths = []
        for url in urls:
            file_name = urlparse(url).path.rsplit("/", 1)[1]
            if file_name.lower().endswith((".jpg", ".jpeg")):
                paths.append(self.photo_download_by_url(url, file_name, folder))
            elif file_name.lower().endswith(".mp4"):
                paths.append(self.video_download_by_url(url, file_name, folder))
            else:
                raise AlbumUnknownFormat()
        return paths

    def album_download_origin(self, media_pk: int) -> List[bytes]:
        """
        Download your album

        Parameters
        ----------
        media_pk: int
            PK for the album you want to download
        Returns
        -------
        List[Path]
            List of path for all the files downloaded
        """
        media = self.media_info(media_pk)
        assert media.media_type == 8, "Must been album"
        files = []
        for resource in media.resources:
            if resource.media_type == 1:
                files.append(self.photo_download_by_url_origin(resource.thumbnail_url))
            elif resource.media_type == 2:
                files.append(self.video_download_by_url_origin(resource.video_url))
            else:
                raise AlbumNotDownload(
                    'Media type "{resource.media_type}" unknown for album (resource={resource.pk})'
                )
        return files


class UploadAlbumMixin:
    def album_upload(
        self,
        paths: List[Path],
        caption: str,
        usertags: List[Usertag] = [],
        location: Location = None,
        configure_timeout: int = 3,
        configure_handler=None,
        configure_exception=None,
        to_story=False,
        extra_data: Dict[str, str] = {},
    ) -> Media:
        """
        Upload album to feed

        Parameters
        ----------
        paths: List[Path]
            List of paths for media to upload
        caption: str
            Media caption
        usertags: List[Usertag], optional
            List of users to be tagged on this upload, default is empty list.
        location: Location, optional
            Location tag for this upload, default is none
        configure_timeout: int
            Timeout between attempt to configure media (set caption, etc), default is 3
        configure_handler
            Configure handler method, default is None
        configure_exception
            Configure exception class, default is None
        to_story: bool
            Currently not used, default is False
        extra_data: Dict[str, str], optional
            Dict of extra data, if you need to add your params, like {"share_to_facebook": 1}.

        Returns
        -------
        Media
            An object of Media class
        """
        children = []
        for path in paths:
            path = Path(path)
            if path.suffix.lower() in (".jpg", ".jpeg", ".webp"):
                upload_id, width, height = self.photo_rupload(path, to_album=True)
                children.append(
                    {
                        "upload_id": upload_id,
                        "edits": dumps(
                            {
                                "crop_original_size": [width, height],
                                "crop_center": [0.0, -0.0],
                                "crop_zoom": 1.0,
                            }
                        ),
                        "extra": dumps(
                            {"source_width": width, "source_height": height}
                        ),
                        "scene_capture_type": "",
                        "scene_type": None,
                    }
                )
            elif path.suffix.lower() == ".mp4":
                upload_id, width, height, duration, thumbnail = self.video_rupload(
                    path, to_album=True
                )
                children.append(
                    {
                        "upload_id": upload_id,
                        "clips": dumps([{"length": duration, "source_type": "4"}]),
                        "extra": dumps(
                            {"source_width": width, "source_height": height}
                        ),
                        "length": duration,
                        "poster_frame_index": "0",
                        "filter_type": "0",
                        "video_result": "",
                        "date_time_original": date_time_original(time.localtime()),
                        "audio_muted": "false",
                    }
                )
                self.photo_rupload(thumbnail, upload_id)
            else:
                raise AlbumUnknownFormat()

        for attempt in range(50):
            self.logger.debug(f"Attempt #{attempt} to configure Album: {paths}")
            time.sleep(configure_timeout)
            try:
                configured = (configure_handler or self.album_configure)(
                    children, caption, usertags, location, extra_data=extra_data
                )
            except Exception as e:
                if "Transcode not finished yet" in str(e):
                    """
                    Response 202 status:
                    {"message": "Transcode not finished yet.", "status": "fail"}
                    """
                    time.sleep(configure_timeout)
                    continue
                raise e
            else:
                if configured:
                    media = configured.get("media")
                    self.expose()
                    return extract_media_v1(media)
        raise (configure_exception or AlbumConfigureError)(
            response=self.last_response, **self.last_json
        )

    def album_configure(
        self,
        childs: List,
        caption: str,
        usertags: List[Usertag] = [],
        location: Location = None,
        extra_data: Dict[str, str] = {},
    ) -> Dict:
        """
        Post Configure Album

        Parameters
        ----------
        childs: List
            List of media/resources of an album
        caption: str
            Media caption
        usertags: List[Usertag], optional
            List of users to be tagged on this upload, default is empty list.
        location: Location, optional
            Location tag for this upload, default is None
        extra_data: Dict[str, str], optional
            Dict of extra data, if you need to add your params, like {"share_to_facebook": 1}.

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        upload_id = str(int(time.time() * 1000))
        if usertags:
            usertags = [
                {"user_id": tag.user.pk, "position": [tag.x, tag.y]} for tag in usertags
            ]
            childs[0]["usertags"] = dumps({"in": usertags})
        data = {
            "timezone_offset": str(self.timezone_offset),
            "source_type": "4",
            "creation_logger_session_id": self.client_session_id,
            "location": self.location_build(location),
            "caption": caption,
            "client_sidecar_id": upload_id,
            "upload_id": upload_id,
            # "location": self.build_location(name, lat, lng, address),
            "suggested_venue_position": -1,
            "device": self.device,
            "is_suggested_venue": False,
            "children_metadata": [
                {
                    "source_type": "4",
                    "timezone_offset": str(self.timezone_offset),
                    "device": dumps(self.device),
                    **child,
                }
                for child in childs
            ],
            **extra_data,
        }
        return self.private_request(
            "media/configure_sidecar/", self.with_default_data(data)
        )



================================================
FILE: instagrapi/mixins/auth.py
================================================
import base64
import hashlib
import hmac
import json
import random
import re
import time
import uuid
from pathlib import Path
from typing import Dict, Union
from uuid import uuid4

import requests
from pydantic import ValidationError

from instagrapi import config
from instagrapi.exceptions import (
    BadCredentials,
    ClientThrottledError,
    PleaseWaitFewMinutes,
    PrivateError,
    ReloginAttemptExceeded,
    TwoFactorRequired,
)
from instagrapi.utils import dumps, gen_token, generate_jazoest

# from instagrapi.zones import CET
TIMELINE_FEED_REASONS = (
    "cold_start_fetch",
    "warm_start_fetch",
    "pagination",
    "pull_to_refresh",
    "auto_refresh",
)
REELS_TRAY_REASONS = ("cold_start", "pull_to_refresh")
try:
    from typing import Literal

    TIMELINE_FEED_REASON = Literal[TIMELINE_FEED_REASONS]
    REELS_TRAY_REASON = Literal[REELS_TRAY_REASONS]
except ImportError:
    # python <= 3.8
    TIMELINE_FEED_REASON = str
    REELS_TRAY_REASON = str


class PreLoginFlowMixin:
    """
    Helpers for pre login flow
    """

    def pre_login_flow(self) -> bool:
        """
        Emulation mobile app behavior before login

        Returns
        -------
        bool
            A boolean value
        """
        # self.set_contact_point_prefill("prefill")
        # self.get_prefill_candidates(True)
        # self.set_contact_point_prefill("prefill")
        self.sync_launcher(True)
        # self.sync_device_features(True)
        return True

    def get_prefill_candidates(self, login: bool = False) -> Dict:
        """
        Get prefill candidates value from Instagram

        Parameters
        ----------
        login: bool, optional
            Whether to login or not

        Returns
        -------
        bool
            A boolean value
        """
        data = {
            "android_device_id": self.android_device_id,
            "client_contact_points": '[{"type":"omnistring","value":"%s","source":"last_login_attempt"}]'
            % self.username,
            "phone_id": self.phone_id,
            "usages": '["account_recovery_omnibox"]',
            "logged_in_user_ids": "[]",  # "[\"123456789\",\"987654321\"]",
            "device_id": self.uuid,
        }
        # if login is False:
        data["_csrftoken"] = self.token
        return self.private_request(
            "accounts/get_prefill_candidates/", data, login=login
        )

    def sync_device_features(self, login: bool = False) -> Dict:
        """
        Sync device features to your Instagram account

        Parameters
        ----------
        login: bool, optional
            Whether to login or not

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        data = {
            "id": self.uuid,
            "server_config_retrieval": "1",
            # "experiments": config.LOGIN_EXPERIMENTS,
        }
        if login is False:
            data["_uuid"] = self.uuid
            data["_uid"] = self.user_id
            data["_csrftoken"] = self.token
        # headers={"X-DEVICE-ID": self.uuid}
        return self.private_request("qe/sync/", data, login=login)

    def sync_launcher(self, login: bool = False) -> Dict:
        """
        Sync Launcher

        Parameters
        ----------
        login: bool, optional
            Whether to login or not

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        data = {
            "id": self.uuid,
            "server_config_retrieval": "1",
        }
        if login is False:
            data["_uid"] = self.user_id
            data["_uuid"] = self.uuid
            data["_csrftoken"] = self.token
        return self.private_request("launcher/sync/", data, login=login)

    def set_contact_point_prefill(self, usage: str = "prefill") -> Dict:
        """
        Sync Launcher

        Parameters
        ----------
        usage: str, optional
            Default "prefill"

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        data = {
            "phone_id": self.phone_id,
            "usage": usage,
            # "_csrftoken": self.token
        }
        return self.private_request("accounts/contact_point_prefill/", data, login=True)


class PostLoginFlowMixin:
    """
    Helpers for post login flow
    """

    def login_flow(self) -> bool:
        """
        Emulation mobile app behaivor after login

        Returns
        -------
        bool
            A boolean value
        """
        check_flow = []
        # chance = random.randint(1, 100) % 2 == 0
        # reason = "pull_to_refresh" if chance else "cold_start"
        check_flow.append(self.get_reels_tray_feed("cold_start"))
        check_flow.append(self.get_timeline_feed(["cold_start_fetch"]))
        return all(check_flow)

    def get_timeline_feed(
        self, reason: TIMELINE_FEED_REASON = "pull_to_refresh", max_id: str = None
    ) -> Dict:
        """
        Get your timeline feed

        Parameters
        ----------
        reason: str, optional
            Reason to refresh the feed (cold_start_fetch, paginating, pull_to_refresh); Default "pull_to_refresh"
        max_id: str, optional
            Cursor for the next feed chunk (next cursor can be found in response["next_max_id"])

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        headers = {
            "X-Ads-Opt-Out": "0",
            "X-DEVICE-ID": self.uuid,
            "X-CM-Bandwidth-KBPS": "-1.000",  # str(random.randint(2000, 5000)),
            "X-CM-Latency": str(random.randint(1, 5)),
        }
        data = {
            "has_camera_permission": "1",
            "feed_view_info": "[]",  # e.g. [{"media_id":"2634223601739446191_7450075998","version":24,
            # "media_pct":1.0,"time_info":{"10":63124,"25":63124,"50":63124,"75":63124},"latest_timestamp":1628253523186}]
            "phone_id": self.phone_id,
            "reason": reason,
            "battery_level": 100,  # Random battery level is not simulating real bahaviour
            "timezone_offset": str(self.timezone_offset),
            # "_csrftoken": self.token, No longer in data
            "device_id": self.uuid,
            "request_id": self.request_id,
            "_uuid": self.uuid,
            "is_charging": random.randint(0, 1),
            "is_dark_mode": 1,  # Random dark mode is not simulating real bahaviour
            "will_sound_on": random.randint(0, 1),
            "session_id": self.client_session_id,
            "bloks_versioning_id": self.bloks_versioning_id,
        }
        if reason in ["pull_to_refresh", "auto_refresh"]:
            data["is_pull_to_refresh"] = "1"
        else:
            data["is_pull_to_refresh"] = "0"

        if max_id:
            data["max_id"] = max_id
            data["reason"] = "pagination"
        # if "push_disabled" in options:
        #     data["push_disabled"] = "true"
        # if "recovered_from_crash" in options:
        #     data["recovered_from_crash"] = "1"
        return self.private_request(
            "feed/timeline/", json.dumps(data), with_signature=False, headers=headers
        )

    def get_reels_tray_feed(
        self, reason: REELS_TRAY_REASON = "pull_to_refresh"
    ) -> Dict:
        """
        Get your reels tray feed

        Parameters
        ----------
        reason: str, optional
            Reason to refresh reels tray fee (cold_start, pull_to_refresh); Default "pull_to_refresh"

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        data = {
            "supported_capabilities_new": config.SUPPORTED_CAPABILITIES,
            "reason": reason,
            "timezone_offset": str(self.timezone_offset),
            "tray_session_id": self.tray_session_id,
            "request_id": self.request_id,
            # "latest_preloaded_reel_ids": "[]",  # Long JSON array with reel data
            # Example: [{"reel_id":"6009504750","media_count":"15","timestamp":1628253494,"media_ids":"..."}]
            "page_size": 50,
            # "_csrftoken": self.token,
            "_uuid": self.uuid,
        }
        if reason == "cold_start":
            data["reel_tray_impressions"] = {}
        else:
            data["reel_tray_impressions"] = {self.user_id: str(time.time())}
        return self.private_request("feed/reels_tray/", data)


class LoginMixin(PreLoginFlowMixin, PostLoginFlowMixin):
    username = None
    password = None
    authorization_data = {}  # decoded authorization header
    last_login = None
    relogin_attempt = 0
    device_settings = {}
    client_session_id = ""
    tray_session_id = ""
    advertising_id = ""
    android_device_id = ""
    request_id = ""
    phone_id = ""
    app_id = "567067343352427"
    uuid = ""
    mid = ""
    country = "US"
    country_code = 1  # Phone code, default USA
    locale = "en_US"
    timezone_offset: int = -14400  # New York, GMT-4 in seconds
    # Example: CLN,49897488153,1666640702:01f7bdb93090f4f773516fc2cf1424178a58a2295b4c754090ba02cb0a834e2d1f731e20
    ig_u_rur = ""
    ig_www_claim = ""  # e.g. hmac.AR2uidim8es5kYgDiNxY0UG_ZhffFFSt8TGCV5eA1VYYsMNx

    def __init__(self):
        self.user_agent = None
        self.settings = None

    def init(self) -> bool:
        """
        Initialize Login helpers

        Returns
        -------
        bool
            A boolean value
        """
        if "cookies" in self.settings:
            self.private.cookies = requests.utils.cookiejar_from_dict(
                self.settings["cookies"]
            )
        self.authorization_data = self.settings.get("authorization_data", {})
        self.last_login = self.settings.get("last_login")
        self.set_timezone_offset(
            self.settings.get("timezone_offset", self.timezone_offset)
        )
        self.set_device(self.settings.get("device_settings"))
        # c7aeefd59aab78fc0a703ea060ffb631e005e2b3948efb9d73ee6a346c446bf3
        self.bloks_versioning_id = (
            "ce555e5500576acd8e84a66018f54a05720f2dce29f0bb5a1f97f0c10d6fac48"
        )  # this param is constant and will change by Instagram app version
        self.set_user_agent(self.settings.get("user_agent"))
        self.set_uuids(self.settings.get("uuids") or {})
        self.set_locale(self.settings.get("locale", self.locale))
        self.set_country(self.settings.get("country", self.country))
        self.set_country_code(self.settings.get("country_code", self.country_code))
        self.mid = self.settings.get("mid", self.cookie_dict.get("mid"))
        self.set_ig_u_rur(self.settings.get("ig_u_rur"))
        self.set_ig_www_claim(self.settings.get("ig_www_claim"))
        # init headers
        headers = self.base_headers
        headers.update({"Authorization": self.authorization})
        self.private.headers.update(headers)
        return True

    def login_by_sessionid(self, sessionid: str) -> bool:
        """
        Login using session id

        Parameters
        ----------
        sessionid: str
            Session ID

        Returns
        -------
        bool
            A boolean value
        """
        assert isinstance(sessionid, str) and len(sessionid) > 30, "Invalid sessionid"
        self.settings["cookies"] = {"sessionid": sessionid}
        self.init()
        user_id = re.search(r"^\d+", sessionid).group()
        self.authorization_data = {
            "ds_user_id": user_id,
            "sessionid": sessionid,
            "should_use_header_over_cookies": True,
        }
        try:
            user = self.user_info_v1(int(user_id))
        except (PrivateError, ValidationError):
            user = self.user_short_gql(int(user_id))
        self.username = user.username
        self.cookie_dict["ds_user_id"] = user.pk
        return True

    def login(
        self,
        username: Union[str, None] = None,
        password: Union[str, None] = None,
        relogin: bool = False,
        verification_code: str = "",
    ) -> bool:
        """
        Login

        Parameters
        ----------
        username: str
            Instagram Username
        password: str
            Instagram Password
        relogin: bool
            Whether or not to re login, default False
        verification_code: str
            2FA verification code

        Returns
        -------
        bool
            A boolean value
        """
        if username and password:
            self.username = username
            self.password = password
        if self.username is None or self.password is None:
            raise BadCredentials("Both username and password must be provided.")

        if relogin:
            self.authorization_data = {}
            self.private.headers.pop("Authorization", None)
            self.private.cookies.clear()
            if self.relogin_attempt > 1:
                raise ReloginAttemptExceeded()
            self.relogin_attempt += 1
        # if self.user_id and self.last_login:
        #     if time.time() - self.last_login < 60 * 60 * 24:
        #        return True  # already login
        if self.user_id and not relogin:
            return True  # already login
        try:
            self.pre_login_flow()
        except (PleaseWaitFewMinutes, ClientThrottledError):
            self.logger.warning("Ignore 429: Continue login")
            # The instagram application ignores this error
            # and continues to log in (repeat this behavior)
        enc_password = self.password_encrypt(self.password)
        data = {
            "jazoest": generate_jazoest(self.phone_id),
            "country_codes": '[{"country_code":"%d","source":["default"]}]' % int(
                self.country_code
            ),
            "phone_id": self.phone_id,
            "enc_password": enc_password,
            "username": username,
            "adid": self.advertising_id,
            "guid": self.uuid,
            "device_id": self.android_device_id,
            "google_tokens": "[]",
            "login_attempt_count": "0",
        }
        try:
            logged = self.private_request("accounts/login/", data, login=True)
            self.authorization_data = self.parse_authorization(
                self.last_response.headers.get("ig-set-authorization")
            )
        except TwoFactorRequired as e:
            if not verification_code.strip():
                raise TwoFactorRequired(
                    f"{e} (you did not provide verification_code for login method)"
                )
            two_factor_identifier = self.last_json.get("two_factor_info", {}).get(
                "two_factor_identifier"
            )
            data = {
                "verification_code": verification_code,
                "phone_id": self.phone_id,
                "_csrftoken": self.token,
                "two_factor_identifier": two_factor_identifier,
                "username": username,
                "trust_this_device": "0",
                "guid": self.uuid,
                "device_id": self.android_device_id,
                "waterfall_id": str(uuid4()),
                "verification_method": "3",
            }
            logged = self.private_request(
                "accounts/two_factor_login/", data, login=True
            )
            self.authorization_data = self.parse_authorization(
                self.last_response.headers.get("ig-set-authorization")
            )
        if logged:
            self.login_flow()
            self.last_login = time.time()
            return True
        return False

    def one_tap_app_login(self, user_id: str, nonce: str) -> bool:
        """One tap login emulation

        Parameters
        ----------
        user_id: str
            User ID
        nonce: str
            Login nonce (from Instagram, e.g. in /logout/)

        Returns
        -------
        bool
            A boolean value
        """
        user_id = int(user_id)
        data = {
            "phone_id": self.phone_id,
            "user_id": user_id,
            "adid": self.advertising_id,
            "guid": self.uuid,
            "device_id": self.uuid,
            "login_nonce": nonce,
            "_csrftoken": self.token,
        }
        return self.private_request("accounts/one_tap_app_login/", data)

    def relogin(self) -> bool:
        """
        Relogin helper

        Returns
        -------
        bool
            A boolean value
        """
        return self.login(self.username, self.password, relogin=True)

    @property
    def cookie_dict(self) -> dict:
        return self.private.cookies.get_dict()

    @property
    def sessionid(self) -> str:
        sessionid = self.cookie_dict.get("sessionid")
        if not sessionid and self.authorization_data:
            sessionid = self.authorization_data.get("sessionid")
        return sessionid

    @property
    def token(self) -> str:
        """CSRF token
        e.g. vUJGjpst6szjI38mZ6Pb1dROsWVerZelGSYGe0W1tuugpSUefVjRLj2Pom2SWNoA
        """
        if not getattr(self, "_token", None):
            self._token = self.cookie_dict.get("csrftoken", gen_token(64))
        return self._token

    @property
    def rank_token(self) -> str:
        return f"{self.user_id}_{self.uuid}"

    @property
    def user_id(self) -> int:
        user_id = self.cookie_dict.get("ds_user_id")
        if not user_id and self.authorization_data:
            user_id = self.authorization_data.get("ds_user_id")
        if user_id:
            return int(user_id)
        return None

    @property
    def device(self) -> dict:
        return {
            key: val
            for key, val in self.device_settings.items()
            if key in ["manufacturer", "model", "android_version", "android_release"]
        }

    def get_settings(self) -> Dict:
        """
        Get current session settings

        Returns
        -------
        Dict
            Current session settings as a Dict
        """
        return {
            "uuids": {
                "phone_id": self.phone_id,
                "uuid": self.uuid,
                "client_session_id": self.client_session_id,
                "advertising_id": self.advertising_id,
                "android_device_id": self.android_device_id,
                # "device_id": self.uuid,
                "request_id": self.request_id,
                "tray_session_id": self.tray_session_id,
            },
            "mid": self.mid,
            "ig_u_rur": self.ig_u_rur,
            "ig_www_claim": self.ig_www_claim,
            "authorization_data": self.authorization_data,
            "cookies": requests.utils.dict_from_cookiejar(self.private.cookies),
            "last_login": self.last_login,
            "device_settings": self.device_settings,
            "user_agent": self.user_agent,
            "country": self.country,
            "country_code": self.country_code,
            "locale": self.locale,
            "timezone_offset": self.timezone_offset,
        }

    def set_settings(self, settings: Dict) -> bool:
        """
        Set session settings

        Returns
        -------
        Bool
        """
        self.settings = settings
        self.init()
        return True

    def load_settings(self, path: Union[str, Path]) -> Dict:
        """
        Load session settings

        Parameters
        ----------
        path: Path
            Path to storage file

        Returns
        -------
        Dict
            Current session settings as a Dict
        """
        with open(path, "r") as fp:
            self.set_settings(json.load(fp))
            return self.settings

    def dump_settings(self, path: Union[str, Path]) -> bool:
        """
        Serialize and save session settings

        Parameters
        ----------
        path: Path
            Path to storage file

        Returns
        -------
        Bool
        """
        with open(path, "w") as fp:
            json.dump(self.get_settings(), fp, indent=4)
        return True

    def set_device(self, device: Dict = None, reset: bool = False) -> bool:
        """
        Helper to set a device for login

        Parameters
        ----------
        device: Dict, optional
            Dict of device settings, default is None

        Returns
        -------
        bool
            A boolean value
        """
        self.device_settings = device or {
            "app_version": "269.0.0.18.75",
            "android_version": 26,
            "android_release": "8.0.0",
            "dpi": "480dpi",
            "resolution": "1080x1920",
            "manufacturer": "OnePlus",
            "device": "devitron",
            "model": "6T Dev",
            "cpu": "qcom",
            "version_code": "314665256",
        }
        self.settings["device_settings"] = self.device_settings
        if reset:
            self.set_uuids({})
            # self.settings = self.get_settings()
        return True

    def set_user_agent(self, user_agent: str = "", reset: bool = False) -> bool:
        """
        Helper to set user agent

        Parameters
        ----------
        user_agent: str, optional
            User agent, default is ""

        Returns
        -------
        bool
            A boolean value
        """
        data = dict(self.device_settings, locale=self.locale)
        self.user_agent = user_agent or config.USER_AGENT_BASE.format(**data)
        # self.private.headers.update({"User-Agent": self.user_agent})  # changed in base_headers
        self.settings["user_agent"] = self.user_agent
        if reset:
            self.set_uuids({})
            # self.settings = self.get_settings()
        return True

    def set_uuids(self, uuids: Dict = None) -> bool:
        """
        Helper to set uuids

        Parameters
        ----------
        uuids: Dict, optional
            UUIDs, default is None

        Returns
        -------
        bool
            A boolean value
        """
        self.phone_id = uuids.get("phone_id", self.generate_uuid())
        self.uuid = uuids.get("uuid", self.generate_uuid())
        self.client_session_id = uuids.get("client_session_id", self.generate_uuid())
        self.advertising_id = uuids.get("advertising_id", self.generate_uuid())
        self.android_device_id = uuids.get(
            "android_device_id", self.generate_android_device_id()
        )
        self.request_id = uuids.get("request_id", self.generate_uuid())
        self.tray_session_id = uuids.get("tray_session_id", self.generate_uuid())
        # self.device_id = uuids.get("device_id", self.generate_uuid())
        self.settings["uuids"] = uuids
        return True

    def generate_uuid(self, prefix: str = "", suffix: str = "") -> str:
        """
        Helper to generate uuids

        Returns
        -------
        str
            A stringified UUID
        """
        return f"{prefix}{uuid.uuid4()}{suffix}"

    def generate_mutation_token(self) -> str:
        """
        Token used when DM sending and upload media

        Returns
        -------
        str
            A stringified int
        """
        return str(random.randint(6800011111111111111, 6800099999999999999))

    def generate_android_device_id(self) -> str:
        """
        Helper to generate Android Device ID

        Returns
        -------
        str
            A random android device id
        """
        return "android-%s" % hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]

    def expose(self) -> Dict:
        """
        Helper to expose

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        data = {"id": self.uuid, "experiment": "ig_android_profile_contextual_feed"}
        return self.private_request("qe/expose/", self.with_default_data(data))

    def with_extra_data(self, data: Dict) -> Dict:
        """
        Helper to get extra data

        Returns
        -------
        Dict
            A dictionary of default data
        """
        return self.with_default_data(
            {
                "phone_id": self.phone_id,
                "_uid": str(self.user_id),
                "guid": self.uuid,
                **data,
            }
        )

    def with_default_data(self, data: Dict) -> Dict:
        """
        Helper to get default data

        Returns
        -------
        Dict
            A dictionary of default data
        """
        return {
            "_uuid": self.uuid,
            # "_uid": str(self.user_id),
            # "_csrftoken": self.token,
            "device_id": self.android_device_id,
            **data,
        }

    def with_action_data(self, data: Dict) -> Dict:
        """
        Helper to get action data

        Returns
        -------
        Dict
            A dictionary of action data
        """
        return dict(self.with_default_data({"radio_type": "wifi-none"}), **data)

    def gen_user_breadcrumb(self, size: int) -> str:
        """
        Helper to generate user breadcrumbs

        Parameters
        ----------
        size: int
            Integer value

        Returns
        -------
        Str
            A string
        """
        key = "iN4$aGr0m"
        dt = int(time.time() * 1000)
        time_elapsed = random.randint(500, 1500) + size * random.randint(500, 1500)
        text_change_event_count = max(1, size / random.randint(3, 5))
        data = "{size!s} {elapsed!s} {count!s} {dt!s}".format(
            **{
                "size": size,
                "elapsed": time_elapsed,
                "count": text_change_event_count,
                "dt": dt,
            }
        )
        return "{!s}\n{!s}\n".format(
            base64.b64encode(
                hmac.new(
                    key.encode("ascii"), data.encode("ascii"), digestmod=hashlib.sha256
                ).digest()
            ),
            base64.b64encode(data.encode("ascii")),
        )

    def inject_sessionid_to_public(self) -> bool:
        """
        Inject sessionid from private session to public session

        Returns
        -------
        bool
            A boolean value
        """
        if self.sessionid:
            self.public.cookies.set("sessionid", self.sessionid)
            return True
        return False

    def logout(self) -> bool:
        result = self.private_request("accounts/logout/", {"one_tap_app_login": True})
        return result["status"] == "ok"

    def parse_authorization(self, authorization) -> dict:
        """Parse authorization header"""
        try:
            b64part = authorization.rsplit(":", 1)[-1]
            if not b64part:
                return {}
            return json.loads(base64.b64decode(b64part))
        except Exception as e:
            self.logger.exception(e)
        return {}

    @property
    def authorization(self) -> str:
        """Build authorization header
        Example: Bearer IGT:2:eaW9u.....aWQiOiI0NzM5=
        """
        if self.authorization_data:
            b64part = base64.b64encode(dumps(self.authorization_data).encode()).decode()
            return f"Bearer IGT:2:{b64part}"
        return ""

    def dump_instaman(self):
        # Example format: helen9151hernandez:AgcXb0GJhAP|Instagram 200.0.0.24.121 Android...
        # Long string with user credentials and device info
        uuids = ";".join(
            [
                self.android_device_id.replace("android-", ""),
                self.uuid,
                self.phone_id,
                self.client_session_id,
            ]
        )
        headers = {
            "X-MID": self.mid,
            "IG-U-DS-USER-ID": self.user_id,
            "IG-U-RUR": self.ig_u_rur,
            "Authorization": self.authorization,
            "X-IG-WWW-Claim": self.ig_www_claim or "0",
        }
        headers = ";".join([f"{key}={value}" for key, value in headers.items()])
        return f"{self.username}:{self.password}|{self.user_agent}|{uuids}|{headers};||"



================================================
FILE: instagrapi/mixins/bloks.py
================================================
from instagrapi.utils import dumps


class BloksMixin:
    bloks_versioning_id = ""

    def bloks_action(self, action: str, data: dict) -> bool:
        """Performing actions for bloks

        Parameters
        ----------
        action: str
            Action, example "com.instagram.challenge.navigation.take_challenge"
        data: dict
            Additional data

        Returns
        -------
        bool
        """
        result = self.private_request(
            f"bloks/apps/{action}/", self.with_default_data(data)
        )
        return result["status"] == "ok"

    def bloks_change_password(self, password: str, challenge_context: dict) -> bool:
        """
        Change password for challenge

        Parameters
        ----------
        passwrd: str
            New password

        Returns
        -------
        bool
        """
        assert (
            self.bloks_versioning_id
        ), "Client.bloks_versioning_id is empty (hash is expected)"
        enc_password = self.password_encrypt(password)
        data = {
            "bk_client_context": dumps(
                {"bloks_version": self.bloks_versioning_id, "styles_id": "instagram"}
            ),
            "challenge_context": challenge_context,
            "bloks_versioning_id": self.bloks_versioning_id,
            "enc_new_password1": enc_password,
            "enc_new_password2": enc_password,
        }
        return self.bloks_action(
            "com.instagram.challenge.navigation.take_challenge", data
        )



================================================
FILE: instagrapi/mixins/captcha.py
================================================
# instagrapi/mixins/captcha.py
from typing import Callable, Dict, Optional

# Corrected relative import path as per task instructions
from ..exceptions import CaptchaChallengeRequired, ClientError


class CaptchaHandlerMixin:
    def __init__(self, *args, **kwargs):
        self._captcha_handler_instance: Optional[Callable[[Dict], str]] = None
        # Ensure compatibility with other mixins/classes by calling super()
        # This is important if CaptchaHandlerMixin is used in a multiple inheritance scenario.
        if hasattr(super(), "__init__"):
            super().__init__(*args, **kwargs)

    def set_captcha_handler(self, handler: Optional[Callable[[Dict], str]]) -> None:
        """
        Set a custom handler function for solving captcha challenges.

        Parameters
        ----------
        handler: Callable[[Dict], str], optional
            A function that takes a dictionary of challenge details
            (e.g., site_key, page_url, raw_challenge_json) and returns
            the solved captcha token as a string.
            If None, clears the existing handler.
        """
        self._captcha_handler_instance = handler

    def captcha_resolve(self, **challenge_details: Dict) -> str:
        """
        Resolve a captcha challenge using the registered handler.

        Parameters
        ----------
        **challenge_details: Dict
            A dictionary containing details of the captcha challenge,
            such as site_key, challenge_type, raw_challenge_json, page_url.

        Returns
        -------
        str
            The solved captcha token (e.g., g-recaptcha-response).

        Raises
        ------
        CaptchaChallengeRequired
            If no handler is configured, or if the handler fails to return a token,
            or if the handler itself raises an unhandled exception.
        ClientError
            For unexpected errors during the process.
        """
        if not hasattr(self, "_captcha_handler_instance"):
            # This can happen if __init__ of this mixin was not called,
            # e.g. due to incorrect super() chain.
            raise ClientError(
                "CaptchaHandlerMixin not properly initialized. _captcha_handler_instance is missing."
            )

        if self._captcha_handler_instance:
            try:
                # Ensure all keys expected by typical handlers are present, even if None
                details_to_pass = {
                    "site_key": challenge_details.get("site_key"),
                    "page_url": challenge_details.get(
                        "page_url"
                    ),  # Important for some solvers
                    "challenge_type": challenge_details.get("challenge_type"),
                    "raw_challenge_json": challenge_details.get("raw_challenge_json"),
                }
                token = self._captcha_handler_instance(details_to_pass)
                if isinstance(token, str) and token:
                    return token
                else:
                    # Handler was called but didn't return a valid token
                    raise CaptchaChallengeRequired(
                        message="Captcha handler ran but did not return a valid token string.",
                        challenge_details=challenge_details,
                    )
            except CaptchaChallengeRequired:  # Allow handler to raise this specifically
                raise
            except Exception as e:
                # Handler raised an unexpected exception
                raise CaptchaChallengeRequired(
                    message=f"Captcha handler raised an unexpected exception: {str(e)}",
                    challenge_details=challenge_details,
                ) from e
        else:
            # No handler is configured
            raise CaptchaChallengeRequired(
                message="No captcha handler is configured. Use client.set_captcha_handler() to set one.",
                challenge_details=challenge_details,
            )



================================================
FILE: instagrapi/mixins/challenge.py
================================================
import hashlib
import json
import random
import time
from enum import Enum
from typing import Dict

import requests

from instagrapi.exceptions import (
    ChallengeError,
    ChallengeRedirection,
    ChallengeRequired,
    ChallengeSelfieCaptcha,
    ChallengeUnknownStep,
    LegacyForceSetNewPasswordForm,
    RecaptchaChallengeForm,
    SelectContactPointRecoveryForm,
    SubmitPhoneNumberForm,
)

WAIT_SECONDS = 5


class ChallengeChoice(Enum):
    SMS = 0
    EMAIL = 1


def extract_messages(challenge):
    messages = []
    for item in challenge["extraData"].get("content"):
        message = item.get("title", item.get("text"))
        if message:
            dot = "" if message.endswith(".") else "."
            messages.append(f"{message}{dot}")
    return messages


class ChallengeResolveMixin:
    """
    Helpers for resolving login challenge
    """

    def challenge_resolve(self, last_json: Dict) -> bool:
        """
        Start challenge resolve

        Returns
        -------
        bool
            A boolean value
        """
        # START GET REQUEST to challenge_url
        challenge_url = last_json["challenge"]["api_path"]
        try:
            user_id, nonce_code = challenge_url.split("/")[2:4]
            challenge_context = last_json.get("challenge", {}).get("challenge_context")
            if not challenge_context:
                challenge_context = json.dumps(
                    {
                        "step_name": "",
                        "nonce_code": nonce_code,
                        "user_id": int(user_id),
                        "is_stateless": False,
                    }
                )
            params = {
                "guid": self.uuid,
                "device_id": self.android_device_id,
                "challenge_context": challenge_context,
            }
        except ValueError:
            # not enough values to unpack (expected 2, got 1)
            params = {}
        try:
            self._send_private_request(challenge_url[1:], params=params)
        except ChallengeRequired:
            assert self.last_json["message"] == "challenge_required", self.last_json
            return self.challenge_resolve_contact_form(challenge_url)
        return self.challenge_resolve_simple(challenge_url)

    def challenge_resolve_contact_form(self, challenge_url: str) -> bool:
        """
        Start challenge resolve

        Помогите нам удостовериться, что вы владеете этим аккаунтом
        > CODE
        Верна ли информация вашего профиля?
        Мы заметили подозрительные действия в вашем аккаунте.
        В целях безопасности сообщите, верна ли информация вашего профиля.
        > I AGREE

        Help us make sure you own this account
        > CODE
        Is your profile information correct?
        We have noticed suspicious activity on your account.
        For security reasons, please let us know if your profile information is correct.
        > I AGREE

        Parameters
        ----------
        challenge_url: str
            Challenge URL

        Returns
        -------
        bool
            A boolean value
        """
        result = self.last_json
        challenge_url = "https://i.instagram.com%s" % challenge_url
        enc_password = "#PWD_INSTAGRAM_BROWSER:0:%s:" % str(int(time.time()))
        instagram_ajax = hashlib.sha256(enc_password.encode()).hexdigest()[:12]
        session = requests.Session()
        session.verify = False  # fix SSLError/HTTPSConnectionPool
        session.proxies = self.private.proxies
        session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; MI 5s Build/OPR1.170623.032; wv) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.149 "
                "Mobile Safari/537.36 %s" % self.user_agent,
                "upgrade-insecure-requests": "1",
                "sec-fetch-dest": "document",
                "accept": (
                    "text/html,application/xhtml+xml,application/xml;q=0.9,"
                    "image/webp,image/apng,*/*;q=0.8,"
                    "application/signed-exchange;v=b3;q=0.9"
                ),
                "x-requested-with": "com.instagram.android",
                "sec-fetch-site": "none",
                "sec-fetch-mode": "navigate",
                "sec-fetch-user": "?1",
                "accept-encoding": "gzip, deflate",
                "accept-language": "en-US,en;q=0.9,en-US;q=0.8,en;q=0.7",
                "pragma": "no-cache",
                "cache-control": "no-cache",
            }
        )
        for key, value in self.private.cookies.items():
            if key in ["mid", "csrftoken"]:
                session.cookies.set(key, value)
        time.sleep(WAIT_SECONDS)
        result = session.get(challenge_url)  # render html form
        session.headers.update(
            {
                "x-ig-www-claim": "0",
                "x-instagram-ajax": instagram_ajax,
                "content-type": "application/x-www-form-urlencoded",
                "accept": "*/*",
                "sec-fetch-dest": "empty",
                "x-requested-with": "XMLHttpRequest",
                "x-csrftoken": session.cookies.get_dict().get("csrftoken"),
                "x-ig-app-id": self.private.headers.get("X-IG-App-ID"),
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "referer": challenge_url,
            }
        )
        time.sleep(WAIT_SECONDS)
        choice = ChallengeChoice.EMAIL
        result = session.post(challenge_url, {"choice": choice})
        result = result.json()
        for retry in range(8):
            time.sleep(WAIT_SECONDS)
            try:
                # FORM TO ENTER CODE
                result = self.handle_challenge_result(result)
                break
            except SelectContactPointRecoveryForm as e:
                if choice == ChallengeChoice.SMS:  # last iteration
                    raise e
                choice = ChallengeChoice.SMS
                result = session.post(challenge_url, {"choice": choice})
                result = result.json()
                continue  # next choice attempt
            except SubmitPhoneNumberForm as e:
                result = session.post(
                    challenge_url,
                    {
                        "phone_number": e.challenge["fields"]["phone_number"],
                        "challenge_context": e.challenge["challenge_context"],
                    },
                )
                result = result.json()
                break
            except ChallengeRedirection:
                return True  # instagram redirect
        assert result.get("challengeType") in (
            "VerifyEmailCodeForm",
            "VerifySMSCodeForm",
            "VerifySMSCodeFormForSMSCaptcha",
        ), result
        for retry_code in range(5):
            for attempt in range(1, 11):
                code = self.challenge_code_handler(self.username, choice)
                if code:
                    break
                time.sleep(WAIT_SECONDS * attempt)
            # SEND CODE
            time.sleep(WAIT_SECONDS)
            result = session.post(challenge_url, {"security_code": code}).json()
            result = result.get("challenge", result)
            if (
                "Please check the code we sent you and try again"
                not in (result.get("errors") or [""])[0]
            ):
                break
        # FORM TO APPROVE CONTACT DATA
        challenge_type = result.get("challengeType")
        if challenge_type == "LegacyForceSetNewPasswordForm":
            self.challenge_resolve_new_password_form(result)
        assert result.get("challengeType") == "ReviewContactPointChangeForm", result
        details = []
        for data in result["extraData"]["content"]:
            for entry in data.get("labeled_list_entries", []):
                val = entry["list_item_text"]
                if "@" not in val:
                    val = val.replace(" ", "").replace("-", "")
                details.append(val)
        # CHECK ACCOUNT DATA
        for detail in [self.username, self.email, self.phone_number]:
            assert (
                not detail or detail in details
            ), 'ChallengeResolve: Data invalid: "%s" not in %s' % (detail, details)
        time.sleep(WAIT_SECONDS)
        result = session.post(
            "https://i.instagram.com%s" % result.get("navigation").get("forward"),
            {
                "choice": 0,  # I AGREE
                "enc_new_password1": enc_password,
                "new_password1": "",
                "enc_new_password2": enc_password,
                "new_password2": "",
            },
        ).json()
        assert result.get("type") == "CHALLENGE_REDIRECTION", result
        assert result.get("status") == "ok", result
        return True

    def challenge_resolve_new_password_form(self, result):
        msg = " ".join(
            [
                "Log into your Instagram account from smartphone and change password!",
                *extract_messages(result),
            ]
        )
        raise LegacyForceSetNewPasswordForm(msg)

    def handle_challenge_result(self, challenge: Dict):
        """
        Handle challenge result

        Parameters
        ----------
        challenge: Dict
            Dict

        Returns
        -------
        bool
            A boolean value
        """
        messages = []
        if "challenge" in challenge:
            """
            Иногда в JSON есть вложенность,
            вместо {challege_object}
            приходит {"challenge": {challenge_object}}
            Sometimes there is nesting in JSON,
            instead of {challege_object}
            comes {"challenge": {challenge_object}}
            """
            challenge = challenge["challenge"]
        challenge_type = challenge.get("challengeType")
        if challenge_type == "SelectContactPointRecoveryForm":
            """
            Помогите нам удостовериться, что вы владеете этим аккаунтом
            Чтобы защитить свой аккаунт, запросите помощь со входом.
            {'message': '',
            'challenge': {'challengeType': 'SelectContactPointRecoveryForm',
            'errors': ['Select a valid choice. 1 is not one of the available choices.'],
            'experiments': {},
            'extraData': {'__typename': 'GraphChallengePage',
            'content': [{'__typename': 'GraphChallengePageHeader',
            'description': None,
            'title': 'Help Us Confirm You Own This Account'},
            {'__typename': 'GraphChallengePageText',
            'alignment': 'center',
            'html': None,
            'text': 'To secure your account, you need to request help logging in.'},
            {'__typename': 'GraphChallengePageForm',
            'call_to_action': 'Get Help Logging In',
            'display': 'inline',
            'fields': None,
            'href': 'https://help.instagram.com/358911864194456'}]},
            'fields': {'choice': 'None'},
            'navigation': {'forward': '/challenge/8530598273/PlWAX2OMVk/',
            'replay': '/challenge/replay/8530598273/PlWAX2OMVk/',
            'dismiss': 'instagram://checkpoint/dismiss'},
            'privacyPolicyUrl': '/about/legal/privacy/',
            'type': 'CHALLENGE'},
            'status': 'fail'}
            """
            if "extraData" in challenge:
                messages += extract_messages(challenge)
            if "errors" in challenge:
                for error in challenge["errors"]:
                    messages.append(error)
            raise SelectContactPointRecoveryForm(
                " ".join(messages), challenge=challenge
            )
        elif challenge_type == "RecaptchaChallengeForm":
            """
            Example:
            {'message': '',
            'challenge': {
            'challengeType': 'RecaptchaChallengeForm',
            'errors': ['Неправильная Captcha. Попробуйте еще раз.'],
            'experiments': {},
            'extraData': None,
            'fields': {'g-recaptcha-response': 'None',
            'disable_num_days_remaining': -60,
            'sitekey': '6LebnxwUAAAAAGm3yH06pfqQtcMH0AYDwlsXnh-u'},
            'navigation': {'forward': '/challenge/32708972491/CE6QdsYZyB/',
            'replay': '/challenge/replay/32708972491/CE6QdsYZyB/',
            'dismiss': 'instagram://checkpoint/dismiss'},
            'privacyPolicyUrl': '/about/legal/privacy/',
            'type': 'CHALLENGE'},
            'status': 'fail'}
            """
            raise RecaptchaChallengeForm(". ".join(challenge.get("errors", [])))
        elif challenge_type in ("VerifyEmailCodeForm", "VerifySMSCodeForm"):
            # Success. Next step
            return challenge
        elif challenge_type == "SubmitPhoneNumberForm":
            raise SubmitPhoneNumberForm(challenge=challenge)
        elif challenge_type:
            # Unknown challenge_type
            messages.append(challenge_type)
            if "errors" in challenge:
                messages.append("\n".join(challenge["errors"]))
            messages.append("(Please manual login)")
            raise ChallengeError(" ".join(messages))
        elif challenge.get("type") == "CHALLENGE_REDIRECTION":
            """
            Example:
            {'location': 'instagram://checkpoint/dismiss',
            'status': 'ok',
            'type': 'CHALLENGE_REDIRECTION'}
            """
            raise ChallengeRedirection()
        return challenge

    def challenge_resolve_simple(self, challenge_url: str) -> bool:
        """
        Old type (through private api) challenge resolver
        Помогите нам удостовериться, что вы владеете этим аккаунтом

        Parameters
        ----------
        challenge_url : str
            Challenge URL

        Returns
        -------
        bool
            A boolean value
        """
        step_name = self.last_json.get("step_name", "")
        if step_name == "delta_login_review" or step_name == "scraping_warning":
            # IT WAS ME (by GEO)
            self._send_private_request(challenge_url, {"choice": "0"})
            return True
        elif step_name == "add_birthday":
            random_year = random.randint(1970, 2004)
            random_month = random.randint(1, 12)
            random_day = random.randint(1, 28)
            self._send_private_request(
                challenge_url,
                {
                    "birthday_year": str(random_year),
                    "birthday_month": str(random_month),
                    "birthday_day": str(random_day),
                },
            )
            return True
        elif step_name in ("verify_email", "verify_email_code", "select_verify_method"):
            if step_name == "select_verify_method":
                """
                {'step_name': 'select_verify_method',
                'step_data': {'choice': '0',
                'fb_access_token': 'None',
                'big_blue_token': 'None',
                'google_oauth_token': 'true',
                'vetted_device': 'None',
                'phone_number': '+7 *** ***-**-09',
                'email': 'x****g@y*****.com'},     <------------- choice
                'nonce_code': 'DrW8V4m5Ec',
                'user_id': 12060121299,
                'status': 'ok'}
                """
                steps = self.last_json["step_data"].keys()
                challenge_url = challenge_url[1:]
                if "email" in steps:
                    self._send_private_request(
                        challenge_url, {"choice": ChallengeChoice.EMAIL}
                    )
                elif "phone_number" in steps:
                    self._send_private_request(
                        challenge_url, {"choice": ChallengeChoice.SMS}
                    )
                else:
                    raise ChallengeError(
                        f'ChallengeResolve: Choice "email" or "phone_number" '
                        f"(sms) not available to this account {self.last_json}"
                    )
            wait_seconds = 5
            for attempt in range(24):
                code = self.challenge_code_handler(self.username, ChallengeChoice.EMAIL)
                if code:
                    break
                time.sleep(wait_seconds)
            print(
                f'Code entered "{code}" for {self.username} ({attempt} attempts by {wait_seconds} seconds)'
            )
            self._send_private_request(challenge_url, {"security_code": code})
            # assert 'logged_in_user' in client.last_json
            assert self.last_json.get("action", "") == "close"
            assert self.last_json.get("status", "") == "ok"
            return True
        elif step_name == "":
            assert self.last_json.get("action", "") == "close"
            assert self.last_json.get("status", "") == "ok"
            return True
        elif step_name == "change_password":
            # Example: {'step_name': 'change_password',
            #  'step_data': {'new_password1': 'None', 'new_password2': 'None'},
            #  'flow_render_type': 3,
            #  'bloks_action': 'com.instagram.challenge.navigation.take_challenge',
            #  'cni': 18226879502000588,
            #  'challenge_context': '{"step_name": "change_password",
            #      "cni": 18226879502000588, "is_stateless": false,
            #      "challenge_type_enum": "PASSWORD_RESET"}',
            #  'challenge_type_enum_str': 'PASSWORD_RESET',
            #  'status': 'ok'}
            wait_seconds = 5
            for attempt in range(24):
                pwd = self.change_password_handler(self.username)
                if pwd:
                    break
                time.sleep(wait_seconds)
            print(
                f'Password entered "{pwd}" for {self.username} ({attempt} attempts by {wait_seconds} seconds)'
            )
            return self.bloks_change_password(pwd, self.last_json["challenge_context"])
        elif step_name == "selfie_captcha":
            raise ChallengeSelfieCaptcha(self.last_json)
        elif step_name == "select_contact_point_recovery":
            """
            {
                'step_name': 'select_contact_point_recovery',
                'step_data': {'choice': '0',
                    'phone_number': '+62 ***-****-**11',
                    'email': 'g*******b@w**.de',
                    'hl_co_enabled': False,
                    'sigp_to_hl': False
                },
                'flow_render_type': 3,
                'bloks_action': 'com.instagram.challenge.navigation.take_challenge',
                'cni': 178623487724,
                'challenge_context': '{"step_name": "select_contact_point_recovery",
                "cni": 178623487724,
                "is_stateless": false,
                "challenge_type_enum": "HACKED_LOCK",
                "present_as_modal": false}',
                'challenge_type_enum_str': 'HACKED_LOCK',
                'status': 'ok'
            }
            """
            steps = self.last_json["step_data"].keys()
            challenge_url = challenge_url[1:]
            if "email" in steps:
                self._send_private_request(
                    challenge_url, {"choice": ChallengeChoice.EMAIL}
                )
            elif "phone_number" in steps:
                self._send_private_request(
                    challenge_url, {"choice": ChallengeChoice.SMS}
                )
            else:
                raise ChallengeError(
                    f'ChallengeResolve: Choice "email" or "phone_number" (sms) '
                    f"not available to this account {self.last_json}"
                )
            wait_seconds = 5
            for attempt in range(24):
                code = self.challenge_code_handler(self.username, ChallengeChoice.EMAIL)
                if code:
                    break
                time.sleep(wait_seconds)
            print(
                f'Code entered "{code}" for {self.username} ({attempt} attempts by {wait_seconds} seconds)'
            )
            self._send_private_request(challenge_url, {"security_code": code})

            if self.last_json.get("action", "") == "close":
                assert self.last_json.get("status", "") == "ok"
                return True

            # last form to verify account details
            assert (
                self.last_json["step_name"] == "review_contact_point_change"
            ), f"Unexpected step_name {self.last_json['step_name']}"

            # details = self.last_json["step_data"]

            # TODO: add validation of account details
            # assert self.username == details['username'], \
            #     f"Data invalid: {self.username} does not match {details['username']}"
            # assert self.email == details['email'], \
            #     f"Data invalid: {self.email} does not match {details['email']}"
            # assert self.phone_number == details['phone_number'], \
            #     f"Data invalid: {self.phone_number} does not match {details['phone_number']}"

            # "choice": 0 ==> details look good
            self._send_private_request(challenge_url, {"choice": 0})

            # TODO: assert that the user is now logged in.
            # # assert 'logged_in_user' in client.last_json
            # assert self.last_json.get("action", "") == "close"
            # assert self.last_json.get("status", "") == "ok"
            return True
        else:
            raise ChallengeUnknownStep(
                f'ChallengeResolve: Unknown step_name "{step_name}" for '
                f'"{self.username}" in challenge resolver: {self.last_json}'
            )
        return True



================================================
FILE: instagrapi/mixins/clip.py
================================================
import json
import random
import tempfile
import time
from pathlib import Path
from typing import Dict, List
from uuid import uuid4

from instagrapi import config
from instagrapi.exceptions import ClientError, ClipConfigureError, ClipNotUpload
from instagrapi.extractors import extract_media_v1
from instagrapi.types import Location, Media, Track, Usertag
from instagrapi.utils import date_time_original

try:
    from PIL import Image
except ImportError:
    raise Exception("You don't have PIL installed. Please install PIL or Pillow>=8.1.1")


class DownloadClipMixin:
    """
    Helpers to download CLIP videos
    """

    def clip_download(self, media_pk: int, folder: Path = "") -> str:
        """
        Download CLIP video

        Parameters
        ----------
        media_pk: int
            PK for the album you want to download
        folder: Path, optional
            Directory in which you want to download the album,
            default is "" and will download the files to working
            directory.

        Returns
        -------
        str
        """
        return self.video_download(media_pk, folder)

    def clip_download_by_url(
        self, url: str, filename: str = "", folder: Path = ""
    ) -> str:
        """
        Download CLIP video using URL

        Parameters
        ----------
        url: str
            URL to download media from
        folder: Path, optional
            Directory in which you want to download the album,
            default is "" and will download the files to working
            directory.

        Returns
        -------
        str
        """
        return self.video_download_by_url(url, filename, folder)


class UploadClipMixin:
    """
    Helpers to upload CLIP videos
    """

    def clip_upload(
        self,
        path: Path,
        caption: str,
        thumbnail: Path = None,
        usertags: List[Usertag] = [],
        location: Location = None,
        configure_timeout: int = 10,
        feed_show: str = "1",
        extra_data: Dict[str, str] = {},
    ) -> Media:
        """
        Upload CLIP to Instagram

        Parameters
        ----------
        path: Path
            Path to CLIP file
        caption: str
            Media caption
        thumbnail: Path, optional
            Path to thumbnail for CLIP.
            Default value is None, and it generates a thumbnail
        usertags: List[Usertag], optional
            List of users to be tagged on this upload, default is empty list.
        location: Location, optional
            Location tag for this upload, default is none
        configure_timeout: int
            Timeout between attempt to configure media (set caption, etc), default is 10
        extra_data: Dict[str, str], optional
            Dict of extra data, if you need to add your params,
            like {"share_to_facebook": 1}.

        Returns
        -------
        Media
            An object of Media class
        """
        path = Path(path)
        if thumbnail is not None:
            thumbnail = Path(thumbnail)
        upload_id = str(int(time.time() * 1000))
        thumbnail, width, height, duration = analyze_video(path, thumbnail)
        waterfall_id = str(uuid4())
        # upload_name example: '1576102477530_0_7823256191'
        upload_name = "{upload_id}_0_{rand}".format(
            upload_id=upload_id, rand=random.randint(1000000000, 9999999999)
        )
        rupload_params = {
            "is_clips_video": "1",
            "retry_context": '{"num_reupload":0,"num_step_auto_retry":0,"num_step_manual_retry":0}',
            "media_type": "2",
            "xsharing_user_ids": json.dumps([self.user_id]),
            "upload_id": upload_id,
            "upload_media_duration_ms": str(int(duration * 1000)),
            "upload_media_width": str(width),
            "upload_media_height": str(height),
        }
        headers = {
            "Accept-Encoding": "gzip",
            "X-Instagram-Rupload-Params": json.dumps(rupload_params),
            "X_FB_VIDEO_WATERFALL_ID": waterfall_id,
            "X-Entity-Type": "video/mp4",
        }
        response = self.private.get(
            "https://{domain}/rupload_igvideo/{name}".format(
                domain=config.API_DOMAIN, name=upload_name
            ),
            headers=headers,
        )
        self.request_log(response)
        if response.status_code != 200:
            raise ClipNotUpload(response=self.last_response, **self.last_json)
        with open(path, "rb") as fp:
            clip_data = fp.read()
            clip_len = str(len(clip_data))
        headers = {
            "Offset": "0",
            "X-Entity-Name": upload_name,
            "X-Entity-Length": clip_len,
            "Content-Type": "application/octet-stream",
            "Content-Length": clip_len,
            **headers,
        }
        response = self.private.post(
            "https://{domain}/rupload_igvideo/{name}".format(
                domain=config.API_DOMAIN, name=upload_name
            ),
            data=clip_data,
            headers=headers,
        )
        self.request_log(response)
        if response.status_code != 200:
            raise ClipNotUpload(response=self.last_response, **self.last_json)
        # CONFIGURE
        # self.igtv_composer_session_id = self.generate_uuid()  #issue
        for attempt in range(50):
            self.logger.debug(f"Attempt #{attempt} to configure CLIP: {path}")
            time.sleep(configure_timeout)
            try:
                configured = self.clip_configure(
                    upload_id,
                    thumbnail,
                    width,
                    height,
                    duration,
                    caption,
                    usertags,
                    location,
                    feed_show,
                    extra_data=extra_data,
                )
            except ClientError as e:
                if "Transcode not finished yet" in str(e):
                    """
                    Response 202 status:
                    {"message": "Transcode not finished yet.", "status": "fail"}
                    """
                    time.sleep(configure_timeout)
                    continue
                raise e
            else:
                if configured:
                    media = self.last_json.get("media")
                    self.expose()
                    return extract_media_v1(media)
        raise ClipConfigureError(response=self.last_response, **self.last_json)

    def clip_upload_as_reel_with_music(
        self,
        path: Path,
        caption: str,
        track: Track,
        extra_data: Dict[str, str] = {},
    ) -> Media:

        """
        Upload CLIP as reel with music metadata.
        It also add the music under the video, therefore a mute video is required.

        If you just want to add music metadata to your reel,
        just copy the extra data you find here and add it
        to the extra_data parameter of the clip_upload function.

        Parameters
        ----------
        path: Path
            Path to CLIP file
        caption: str
            Media caption
        track: Track
            The music track to be added to the video reel
            use cl.search_music(title)[0].dict()

        extra_data: Dict[str, str], optional
            Dict of extra data, if you need to add your params, like {"share_to_facebook": 1}.

        Returns
        -------
        Media
            A Media response from the call
        """
        tmpaudio = Path(tempfile.mktemp(".m4a"))
        tmpaudio = self.track_download_by_url(track.uri, "track", tmpaudio.parent)
        try:
            highlight_start_time = track.highlight_start_times_in_ms[0]
        except IndexError:
            highlight_start_time = 0
        try:
            import moviepy.editor as mp
        except ImportError:
            try:
                import moviepy as mp
            except ImportError:
                raise Exception("Please install moviepy>=1.0.3 and retry")
        # get all media to create the reel
        video = mp.VideoFileClip(str(path))
        audio_clip = mp.AudioFileClip(str(tmpaudio))
        # set the start time of the audio and create the actual media
        start = highlight_start_time / 1000
        end = highlight_start_time / 1000 + video.duration
        audio_clip = audio_clip.subclip(start, end)
        video = video.set_audio(audio_clip)
        # save the media in tmp folder
        tmpvideo = Path(tempfile.mktemp(".mp4"))
        video.write_videofile(str(tmpvideo))
        # close the media
        try:
            video.close()
        except AttributeError:
            pass
        try:
            audio_clip.close()
        except AttributeError:
            pass
        # create the extra data to upload with it
        data = extra_data or {}
        data["clips_audio_metadata"] = (
            {
                "original": {"volume_level": 0.0},
                "song": {
                    "volume_level": 1.0,
                    "is_saved": "0",
                    "artist_name": track.display_artist,
                    "audio_asset_id": track.id,
                    "audio_cluster_id": track.audio_cluster_id,
                    "track_name": track.title,
                    "is_picked_precapture": "1",
                },
            },
        )
        data["music_params"] = {
            "audio_asset_id": track.id,
            "audio_cluster_id": track.audio_cluster_id,
            "audio_asset_start_time_in_ms": highlight_start_time,
            "derived_content_start_time_in_ms": 0,
            "overlap_duration_in_ms": int(video.duration * 1000),
            "product": "story_camera_clips_v2",
            "song_name": track.title,
            "artist_name": track.display_artist,
            "alacorn_session_id": "null",
        }
        clip_upload = self.clip_upload(tmpvideo, caption, extra_data=data)
        # remove the tmp files
        tmpvideo.unlink()
        tmpaudio.unlink()
        return clip_upload

    def clip_configure(
        self,
        upload_id: str,
        thumbnail: Path,
        width: int,
        height: int,
        duration: int,
        caption: str,
        usertags: List[Usertag] = [],
        location: Location = None,
        feed_show: str = "1",
        extra_data: Dict[str, str] = {},
    ) -> Dict:
        """
        Post Configure CLIP (send caption, thumbnail and more to Instagram)

        Parameters
        ----------
        upload_id: str
            Unique identifier for a IGTV video
        thumbnail: Path
            Path to thumbnail for IGTV
        width: int
            Width of the video in pixels
        height: int
            Height of the video in pixels
        duration: int
            Duration of the video in seconds
        caption: str
            Media caption
        usertags: List[Usertag], optional
            List of users to be tagged on this upload, default is empty list.
        location: Location, optional
            Location tag for this upload, default is None
        extra_data: Dict[str, str], optional
            Dict of extra data, if you need to add your params, like {"share_to_facebook": 1}.

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        self.photo_rupload(Path(thumbnail), upload_id)
        usertags = [
            {"user_id": tag.user.pk, "position": [tag.x, tag.y]} for tag in usertags
        ]
        data = {
            # "igtv_ads_toggled_on": "0",
            "filter_type": "0",
            "timezone_offset": str(self.timezone_offset),
            "media_folder": "ScreenRecorder",
            "location": self.location_build(location),
            "source_type": "4",
            # "title": title,
            "caption": caption,
            "usertags": json.dumps({"in": usertags}),
            "date_time_original": date_time_original(time.localtime()),
            "clips_share_preview_to_feed": feed_show,
            "upload_id": upload_id,
            # "igtv_composer_session_id": self.igtv_composer_session_id,
            "device": self.device,
            "length": duration,
            "clips": [{"length": duration, "source_type": "4"}],
            "extra": {"source_width": width, "source_height": height},
            "audio_muted": False,
            "poster_frame_index": 70,
            **extra_data,
        }
        return self.private_request(
            "media/configure_to_clips/?video=1",
            self.with_default_data(data),
            with_signature=True,
        )


def analyze_video(path: Path, thumbnail: Path = None) -> tuple:
    """
    Analyze and crop thumbnail if need

    Parameters
    ----------
    path: Path
        Path to the video
    thumbnail: Path
        Path to thumbnail for CLIP

    Returns
    -------
    Tuple
        A tuple with (thumbail path, width, height, duration)
    """
    try:
        import moviepy.editor as mp
    except ImportError:
        try:
            import moviepy as mp
        except ImportError:
            raise Exception("Please install moviepy>=1.0.3 and retry")

    print(f'Analyzing CLIP file "{path}"')
    video = mp.VideoFileClip(str(path))
    width, height = video.size
    if not thumbnail:
        thumbnail = f"{path}.jpg"
        print(f'Generating thumbnail "{thumbnail}"...')
        video.save_frame(thumbnail, t=(video.duration / 2))
        crop_thumbnail(thumbnail)
    return thumbnail, width, height, video.duration


def crop_thumbnail(path: Path) -> bool:
    """
    Analyze and crop thumbnail if need

    Parameters
    ----------
    path: Path
        Path to the video

    Returns
    -------
    bool
        A boolean value
    """
    im = Image.open(str(path))
    width, height = im.size
    offset = (height / 1.78) / 2
    center = width / 2
    # Crop the center of the image
    im = im.crop((center - offset, 0, center + offset, height))
    with open(path, "w") as fp:
        im.save(fp)
        im.close()
    return True



================================================
FILE: instagrapi/mixins/collection.py
================================================
from typing import List, Tuple

from instagrapi.exceptions import CollectionNotFound
from instagrapi.extractors import extract_collection, extract_media_v1
from instagrapi.types import Collection, Media


class CollectionMixin:
    """
    Helpers for collection
    """

    def collections(self) -> List[Collection]:
        """
        Get collections

        Returns
        -------
        List[Collection]
            A list of objects of Collection
        """
        next_max_id = ""
        total_items = []
        while True:
            try:
                result = self.private_request(
                    "collections/list/",
                    params={
                        "collection_types": '["ALL_MEDIA_AUTO_COLLECTION","PRODUCT_AUTO_COLLECTION","MEDIA"]',
                        "max_id": next_max_id,
                    },
                )
            except Exception as e:
                self.logger.exception(e)
                return total_items
            for item in result["items"]:
                total_items.append(extract_collection(item))
            if not result.get("more_available"):
                return total_items
            next_max_id = result.get("next_max_id", "")
        return total_items

    def collection_pk_by_name(self, name: str) -> int:
        """
        Get collection_pk by name

        Parameters
        ----------
        name: str
            Name of the collection

        Returns
        -------
        List[Collection]
            A list of objects of Collection
        """
        for item in self.collections():
            if item.name == name:
                return item.id
        raise CollectionNotFound(name=name)

    def collection_medias_by_name(self, name: str) -> List[Collection]:
        """
        Get medias by collection name

        Parameters
        ----------
        name: str
            Name of the collection

        Returns
        -------
        List[Collection]
            A list of collections
        """

        return self.collection_medias(self.collection_pk_by_name(name))

    def liked_medias(self, amount: int = 21, last_media_pk: int = 0) -> List[Media]:
        """
        Get media you have liked

        Parameters
        ----------
        amount: int, optional
            Maximum number of media to return, default is 21
        last_media_pk: int, optional
            Last PK user has seen, function will return medias after this pk. Default is 0
        Returns
        -------
        List[Media]
            A list of objects of Media
        """
        return self.collection_medias("liked", amount, last_media_pk)

    def collection_medias_v1_chunk(
        self, collection_pk: str, max_id: str = ""
    ) -> Tuple[List[Media], str]:
        """
        Get media in a collection by collection_pk

        Parameters
        ----------
        collection_pk: str
            Unique identifier of a Collection
        max_id: str, optional
            Cursor

        Returns
        -------
        Tuple[List[Media], str]
            A list of objects of Media and cursor
        """
        if isinstance(collection_pk, int) or collection_pk.isdigit():
            private_request_endpoint = f"feed/collection/{collection_pk}/"
        elif collection_pk.lower() == "liked":
            private_request_endpoint = "feed/liked/"
        else:
            private_request_endpoint = "feed/saved/posts/"

        params = {"include_igtv_preview": "false"}
        if max_id:
            params["max_id"] = max_id
        result = self.private_request(private_request_endpoint, params=params)
        items = [extract_media_v1(m.get("media", m)) for m in result["items"]]
        return items, result.get("next_max_id", "")

    def collection_medias_v1(
        self, collection_pk: str, amount: int = 21, last_media_pk: int = 0
    ) -> List[Media]:
        """
        Get media in a collection by collection_pk

        Parameters
        ----------
        collection_pk: str
            Unique identifier of a Collection
        amount: int, optional
            Maximum number of media to return, default is 21
        last_media_pk: int, optional
            Last PK user has seen, function will return medias after this pk. Default is 0

        Returns
        -------
        List[Media]
            A list of objects of Media
        """
        last_media_pk = last_media_pk and int(last_media_pk)
        total_items = []
        next_max_id = ""
        amount = int(amount)
        found_last_media_pk = False
        while True:
            items, next_max_id = self.collection_medias_v1_chunk(
                collection_pk, max_id=next_max_id
            )
            for item in items:
                if last_media_pk and last_media_pk == item.pk:
                    found_last_media_pk = True
                    break
                total_items.append(item)
            if (amount and len(total_items) >= amount) or found_last_media_pk:
                break
            if not items or not next_max_id:
                break
        return total_items[:amount] if amount else total_items

    def collection_medias(
        self, collection_pk: str, amount: int = 21, last_media_pk: int = 0
    ) -> List[Media]:
        """
        Get media in a collection by collection_pk

        Parameters
        ----------
        collection_pk: str
            Unique identifier of a Collection
        amount: int, optional
            Maximum number of media to return, default is 21
        last_media_pk: int, optional
            Last PK user has seen, function will return medias after this pk. Default is 0

        Returns
        -------
        List[Media]
            A list of objects of Media
        """
        return self.collection_medias_v1(
            collection_pk, amount=amount, last_media_pk=last_media_pk
        )

    def media_save(
        self, media_id: str, collection_pk: int = None, revert: bool = False
    ) -> bool:
        """
        Save a media to collection

        Parameters
        ----------
        media_id: str
            Unique identifier of a Media
        collection_pk: int
            Unique identifier of a Collection
        revert: bool, optional
            If True then save to collection, otherwise unsave

        Returns
        -------
        bool
            A boolean value
        """
        assert self.user_id, "Login required"
        media_id = self.media_pk(media_id)
        data = {
            "module_name": "feed_timeline",
            "radio_type": "wifi-none",
        }
        if collection_pk:
            data["added_collection_ids"] = f"[{int(collection_pk)}]"
        name = "unsave" if revert else "save"
        result = self.private_request(
            f"media/{media_id}/{name}/", self.with_action_data(data)
        )
        return result["status"] == "ok"

    def media_unsave(self, media_id: str, collection_pk: int = None) -> bool:
        """
        Unsave a media

        Parameters
        ----------
        media_id: str
            Unique identifier of a Media
        collection_pk: int
            Unique identifier of a Collection

        Returns
        -------
        bool
            A boolean value
        """
        return self.media_save(media_id, collection_pk, revert=True)



================================================
FILE: instagrapi/mixins/comment.py
================================================
import random
from typing import List, Optional, Tuple

from instagrapi.exceptions import ClientError, ClientNotFoundError, MediaNotFound
from instagrapi.extractors import extract_comment
from instagrapi.types import Comment


class CommentMixin:
    """
    Helpers for managing comments on a Media
    """

    def media_comments(self, media_id: str, amount: int = 20) -> List[Comment]:
        """
        Get comments on a media

        Parameters
        ----------
        media_id: str
            Unique identifier of a Media
        amount: int, optional
            Maximum number of comments to return, default is 0 - Inf

        Returns
        -------
        List[Comment]
            A list of objects of Comment
        """

        # TODO: to public or private
        def get_comments():
            if result.get("comments"):
                for comment in result.get("comments"):
                    comments.append(extract_comment(comment))

        media_id = self.media_id(media_id)
        params = None
        comments = []
        result = self.private_request(f"media/{media_id}/comments/", params)
        get_comments()
        while (result.get("has_more_comments") and result.get("next_max_id")) or (
            result.get("has_more_headload_comments") and result.get("next_min_id")
        ):
            try:
                if result.get("has_more_comments"):
                    params = {"max_id": result.get("next_max_id")}
                else:
                    params = {"min_id": result.get("next_min_id")}
                if not (
                    result.get("next_max_id")
                    or result.get("next_min_id")
                    or result.get("comments")
                ):
                    break
                result = self.private_request(f"media/{media_id}/comments/", params)
                get_comments()
            except ClientNotFoundError as e:
                raise MediaNotFound(e, media_id=media_id, **self.last_json)
            except ClientError as e:
                if "Media not found" in str(e):
                    raise MediaNotFound(e, media_id=media_id, **self.last_json)
                raise e
            if amount and len(comments) >= amount:
                break
        if amount:
            comments = comments[:amount]
        return comments

    def media_comments_chunk(
        self, media_id: str, max_amount: int, min_id: str = None
    ) -> Tuple[List[Comment], str]:
        """
        Get chunk of comments on a media and end_cursor

        Parameters
        ----------
        media_id: str
            Unique identifier of a Media
        max_amount: int
            Limit number of comments to fetch, default is 100
        min_id: str, optional
            End Cursor of previous chunk that had more comments, default value is None

        Returns
        -------
        Tuple[List[Comment], str]
            A list of objects of Comment and an end_cursor
        """

        # TODO: to public or private
        def get_comments():
            if result.get("comments"):
                for comment in result.get("comments"):
                    comments.append(extract_comment(comment))

        media_id = self.media_id(media_id)
        params = {"min_id": min_id} if min_id else None
        comments = []
        result = self.private_request(f"media/{media_id}/comments/", params)
        get_comments()
        while result.get("has_more_headload_comments") and result.get("next_min_id"):
            try:
                params = {"min_id": result.get("next_min_id")}
                if not (result.get("next_min_id") or result.get("comments")):
                    break
                result = self.private_request(f"media/{media_id}/comments/", params)
                get_comments()
            except ClientNotFoundError as e:
                raise MediaNotFound(e, media_id=media_id, **self.last_json)
            except ClientError as e:
                if "Media not found" in str(e):
                    raise MediaNotFound(e, media_id=media_id, **self.last_json)
                raise e
            if len(comments) >= max_amount:
                break
        return (comments, result.get("next_min_id"))

    def media_comment(
        self, media_id: str, text: str, replied_to_comment_id: Optional[int] = None
    ) -> Comment:
        """
        Post a comment on a media

        Parameters
        ----------
        media_id: str
            Unique identifier of a Media
        text: str
            String to be posted on the media

        Returns
        -------
        Comment
            An object of Comment type
        """
        assert self.user_id, "Login required"
        media_id = self.media_id(media_id)
        data = {
            "delivery_class": "organic",
            "feed_position": "0",
            "container_module": "self_comments_v2_feed_contextual_self_profile",  # "comments_v2",
            "user_breadcrumb": self.gen_user_breadcrumb(len(text)),
            "idempotence_token": self.generate_uuid(),
            "comment_text": text,
        }
        if replied_to_comment_id:
            data["replied_to_comment_id"] = int(replied_to_comment_id)
        result = self.private_request(
            f"media/{media_id}/comment/",
            self.with_action_data(data),
        )
        return extract_comment(result["comment"])

    def media_check_offensive_comment(self, media_id: str, text: str) -> bool:
        """
        Checks if a comment text is offensive

        Parameters
        ----------
        media_id: str
            Unique identifier of a Media
        text: str
            String to be posted on the media

        Returns
        -------
        bool
            If comment is offensive
        """
        assert self.user_id, "Login required"
        media_id = self.media_id(media_id)
        data = {
            # _uid, comment_session_id are not in this body?
            "media_id": media_id,
            "comment_text": text,
        }
        result = self.private_request(
            "media/comment/check_offensive_comment/",
            self.with_action_data(data),
        )
        return result["is_offensive"]

    def comment_like(self, comment_pk: int, revert: bool = False) -> bool:
        """
        Like a comment on a media

        Parameters
        ----------
        comment_pk: int
            Unique identifier of a Comment
        revert: bool, optional
            If liked, whether or not to unlike. Default is False

        Returns
        -------
        bool
            A boolean value
        """
        assert self.user_id, "Login required"
        comment_pk = int(comment_pk)
        data = {
            "is_carousel_bumped_post": "false",
            "container_module": "feed_contextual_self_profile",
            "feed_position": str(random.randint(0, 6)),
        }
        name = "unlike" if revert else "like"
        result = self.private_request(
            f"media/{comment_pk}/comment_{name}/", self.with_action_data(data)
        )
        return result["status"] == "ok"

    def comment_unlike(self, comment_pk: int) -> bool:
        """
        Unlike a comment on a media

        Parameters
        ----------
        comment_pk: int
            Unique identifier of a Comment

        Returns
        -------
        bool
            A boolean value
        """
        return self.comment_like(comment_pk, revert=True)

    def comment_pin(self, media_id: str, comment_pk: int, revert: bool = False):
        """
        Pin a comment on a media

        Parameters
        ----------
        media_id: str
            Unique identifier of a Media
        comment_pk: int
           Unique identifier of a Comment
        revert: bool, optional
            Unpin when True
        Returns
        -------
        bool
           A boolean value
        """
        data = self.with_action_data({"_uid": self.user_id, "_uuid": self.uuid})
        name = "unpin" if revert else "pin"

        result = self.private_request(
            f"media/{media_id}/{name}_comment/{comment_pk}", data
        )
        return result["status"] == "ok"

    def comment_unpin(self, media_id: str, comment_pk: int):
        """
        Unpin a comment on a media

        Parameters
        ----------
        media_id: str
            Unique identifier of a Media
        comment_pk: int
           Unique identifier of a Comment

        Returns
        -------
        bool
           A boolean value
        """
        return self.comment_pin(media_id, comment_pk, True)

    def comment_bulk_delete(self, media_id: str, comment_pks: List[int]) -> bool:
        """
        Delete a comment on a media

        Parameters
        ----------
        media_id: str
            Unique identifier of a Media
        comment_pks: List[int]
            List of unique identifier of a Comment

        Returns
        -------
        bool
            A boolean value
        """
        media_id = self.media_id(media_id)
        data = {
            "comment_ids_to_delete": ",".join([str(pk) for pk in comment_pks]),
            "container_module": "self_comments_v2_newsfeed_you",
        }
        result = self.private_request(
            f"media/{media_id}/comment/bulk_delete/", self.with_action_data(data)
        )
        return result["status"] == "ok"



================================================
FILE: instagrapi/mixins/direct.py
================================================
import random
import re
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from instagrapi.exceptions import ClientNotFoundError, DirectThreadNotFound
from instagrapi.extractors import (
    extract_direct_media,
    extract_direct_message,
    extract_direct_short_thread,
    extract_direct_thread,
    extract_user_short,
)
from instagrapi.types import (
    DirectMessage,
    DirectShortThread,
    DirectThread,
    Media,
    UserShort,
)
from instagrapi.utils import dumps

SELECTED_FILTERS = ("flagged", "unread")
SEARCH_MODES = ("raven", "universal")
SEND_ATTRIBUTES = ("message_button", "inbox_search")
SEND_ATTRIBUTES_MEDIA = (
    "feed_timeline",
    "feed_contextual_chain",
    "feed_short_url",
    "feed_contextual_self_profile",
    "feed_contextual_profile",
)
BOXES = ("general", "primary")

try:
    from typing import Literal

    SELECTED_FILTER = Literal[SELECTED_FILTERS]
    SEARCH_MODE = Literal[SEARCH_MODES]
    SEND_ATTRIBUTE = Literal[SEND_ATTRIBUTES]
    SEND_ATTRIBUTE_MEDIA = Literal[SEND_ATTRIBUTES_MEDIA]
    BOX = Literal[BOXES]
except ImportError:
    # python <= 3.8
    SELECTED_FILTER = str
    SEARCH_MODE = str
    SEND_ATTRIBUTE = str
    BOX = str


class DirectMixin:
    """
    Helpers for managing Direct Messaging
    """

    def direct_threads(
        self,
        amount: int = 20,
        selected_filter: SELECTED_FILTER = "",
        box: BOX = "",
        thread_message_limit: Optional[int] = None,
    ) -> List[DirectThread]:
        """
        Get direct message threads

        Parameters
        ----------
        amount: int, optional
            Maximum number of media to return, default is 20
        selected_filter: str, optional
            Filter to apply to threads (flagged or unread)
        box: str, optional
            Box to gather threads from (primary or general) (business accounts only)
        thread_message_limit: int, optional
            Thread message limit, deafult is 10

        Returns
        -------
        List[DirectThread]
            A list of objects of DirectThread
        """

        cursor = None
        threads = []
        # self.private_request("direct_v2/get_presence/")
        while True:
            threads_chunk, cursor = self.direct_threads_chunk(
                selected_filter, box, thread_message_limit, cursor
            )
            for thread in threads_chunk:
                threads.append(thread)

            if not cursor or (amount and len(threads) >= amount):
                break
        if amount:
            threads = threads[:amount]
        return threads

    def direct_threads_chunk(
        self,
        selected_filter: SELECTED_FILTER = "",
        box: BOX = "",
        thread_message_limit: Optional[int] = None,
        cursor: str = None,
    ) -> Tuple[List[DirectThread], str]:
        """
        Get direct a chunk of threads by cursor value

        Parameters
        ----------
        selected_filter: str, optional
            Filter to apply to threads (flagged or unread)
        thread_message_limit: int, optional
            Thread message limit, deafult is 10
        box: str, optional
            Box to gather threads from (primary or general) (business accounts only)
        cursor: str, optional
            Cursor from the previous chunk request

        Returns
        -------
        Tuple[List[DirectThread], str]
            A tuple of list of objects of DirectThread and str (cursor)
        """
        assert self.user_id, "Login required"
        params = {
            "visual_message_return_type": "unseen",
            "thread_message_limit": "10",
            "persistentBadging": "true",
            "limit": "20",
            "is_prefetching": "false",
        }
        if selected_filter:
            assert (
                selected_filter in SELECTED_FILTERS
            ), f'Unsupported selected_filter="{selected_filter}" {SELECTED_FILTERS}'
            params.update({"selected_filter": selected_filter})
        if box:
            assert box in BOXES, f'Unsupported box="{box}" {BOXES}'
            params.update({"folder": "1" if box == "general" else "0"})
        if thread_message_limit:
            params.update({"thread_message_limit": thread_message_limit})
        if cursor:
            params.update(
                {"cursor": cursor, "direction": "older", "fetch_reason": "page_scroll"}
            )

        threads = []
        result = self.private_request("direct_v2/inbox/", params=params)
        inbox = result.get("inbox", {})
        for thread in inbox.get("threads", []):
            threads.append(extract_direct_thread(thread))
        cursor = inbox.get("oldest_cursor")
        return threads, cursor

    def direct_pending_inbox(self, amount: int = 20) -> List[DirectThread]:
        """
        Get direct threads of Pending inbox

        Parameters
        ----------
        amount: int, optional
            Maximum number of threads to return, default is 20

        Returns
        -------
        List[DirectThread]
            A list of objects of DirectThread
        """

        cursor = None
        threads = []
        while True:
            new_threads, cursor = self.direct_pending_chunk(cursor)
            for thread in new_threads:
                threads.append(thread)

            if not cursor or (amount and len(threads) >= amount):
                break
        if amount:
            threads = threads[:amount]
        return threads

    def direct_pending_chunk(
        self, cursor: str = None
    ) -> Tuple[List[DirectThread], str]:
        """
        Get direct threads of Pending inbox. Chunk

        Parameters
        ----------
        cursor: str, optional
            Cursor from the previous chunk request

        Returns
        -------
        Tuple[List[DirectThread], str]
            A tuple of list of objects of DirectThread and str (cursor)
        """
        assert self.user_id, "Login required"
        params = {
            "visual_message_return_type": "unseen",
            "persistentBadging": "true",
            "is_prefetching": "false",
            "request_session_id": self.request_id,
        }
        if cursor:
            params.update({"cursor": cursor})

        threads = []
        result = self.private_request("direct_v2/pending_inbox/", params=params)
        inbox = result.get("inbox", {})
        for thread in inbox.get("threads", []):
            threads.append(extract_direct_thread(thread))
        cursor = inbox.get("oldest_cursor")
        return threads, cursor

    def direct_pending_approve(self, thread_id: int) -> bool:
        """
        Approve pending direct thread

        Parameters
        ----------
        thread_id: int
            ID of thread to approve

        Returns
        -------
        bool
            A boolean value
        """
        assert self.user_id, "Login required"

        result = self.private_request(
            f"direct_v2/threads/{thread_id}/approve/",
            data={"filter": "DEFAULT", "_uuid": self.uuid},
            with_signature=False,
        )
        return result.get("status", "") == "ok"

    def direct_spam_inbox(self, amount: int = 20) -> List[DirectThread]:
        """
        Get direct threads of Spam inbox (hidden requests)

        Parameters
        ----------
        amount: int, optional
            Maximum number of threads to return, default is 20

        Returns
        -------
        List[DirectThread]
            A list of objects of DirectThread
        """
        cursor = None
        threads = []
        while True:
            new_threads, cursor = self.direct_spam_chunk(cursor)
            for thread in new_threads:
                threads.append(thread)

            if not cursor or (amount and len(threads) >= amount):
                break
        if amount:
            threads = threads[:amount]
        return threads

    def direct_spam_chunk(self, cursor: str = None) -> Tuple[List[DirectThread], str]:
        """
        Get direct threads of Spam inbox (hidden requests). Chunk

        Parameters
        ----------
        cursor: str, optional
            Cursor from the previous chunk request

        Returns
        -------
        Tuple[List[DirectThread], str]
            A tuple of list of objects of DirectThread and str (cursor)
        """
        assert self.user_id, "Login required"
        params = {
            "visual_message_return_type": "unseen",
            "persistentBadging": "true",
            "is_prefetching": "false",
        }
        if cursor:
            params.update({"cursor": cursor})

        threads = []
        result = self.private_request("direct_v2/spam_inbox/", params=params)
        inbox = result.get("inbox", {})
        for thread in inbox.get("threads", []):
            threads.append(extract_direct_thread(thread))
        cursor = inbox.get("oldest_cursor")
        return threads, cursor

    def direct_thread(self, thread_id: int, amount: int = 20) -> DirectThread:
        """
        Get all the information about a Direct Message thread

        Parameters
        ----------
        thread_id: int
            Unique identifier of a Direct Message thread

        amount: int, optional
            Maximum number of media to return, default is 20

        Returns
        -------
        DirectThread
            An object of DirectThread
        """
        assert self.user_id, "Login required"
        params = {
            "visual_message_return_type": "unseen",
            "direction": "older",
            "seq_id": "40065",  # 59663
            "limit": "20",
        }
        cursor = None
        items = []
        while True:
            if cursor:
                params["cursor"] = cursor
            try:
                result = self.private_request(
                    f"direct_v2/threads/{thread_id}/", params=params
                )
            except ClientNotFoundError as e:
                raise DirectThreadNotFound(e, thread_id=thread_id, **self.last_json)
            thread = result["thread"]
            for item in thread["items"]:
                items.append(item)
            cursor = thread.get("oldest_cursor")
            if not cursor or (amount and len(items) >= amount):
                break
        if amount:
            items = items[:amount]
        thread["items"] = items
        return extract_direct_thread(thread)

    def direct_messages(self, thread_id: int, amount: int = 20) -> List[DirectMessage]:
        """
        Get all the messages from a thread

        Parameters
        ----------
        thread_id: int
            Unique identifier of a Direct Message thread

        amount: int, optional
            Maximum number of media to return, default is 20

        Returns
        -------
        List[DirectMessage]
            A list of objects of DirectMessage
        """
        assert self.user_id, "Login required"
        return self.direct_thread(thread_id, amount).messages

    def direct_answer(self, thread_id: int, text: str) -> DirectMessage:
        """
        Post a message on a Direct Message thread

        Parameters
        ----------
        thread_id: int
            Unique identifier of a Direct Message thread

        text: str
            String to be posted on the thread

        Returns
        -------
        DirectMessage
            An object of DirectMessage
        """
        assert self.user_id, "Login required"
        return self.direct_send(text, [], [int(thread_id)])

    def direct_send(
        self,
        text: str,
        user_ids: List[int] = [],
        thread_ids: List[int] = [],
        send_attribute: SEND_ATTRIBUTE = "message_button",
        reply_to_message: Optional[DirectMessage] = None,
    ) -> DirectMessage:
        """
        Send a direct message to list of users or threads

        Parameters
        ----------
        text: str
            String to be posted on the thread

        user_ids: List[int]
            List of unique identifier of Users id

        thread_ids: List[int]
            List of unique identifier of Direct Message thread id

        send_attribute: str, optional
            Sending option. Default is "message_button"

        Returns
        -------
        DirectMessage
            An object of DirectMessage
        """
        assert self.user_id, "Login required"
        assert (user_ids or thread_ids) and not (
            user_ids and thread_ids
        ), "Specify user_ids or thread_ids, but not both"
        assert (
            send_attribute in SEND_ATTRIBUTES
        ), f'Unsupported send_attribute="{send_attribute}" {SEND_ATTRIBUTES}'
        method = "text"
        token = self.generate_mutation_token()

        kwargs = {
            "action": "send_item",
            "is_x_transport_forward": "false",
            "send_silently": "false",
            "is_shh_mode": "0",
            "send_attribution": send_attribute,
            "client_context": token,
            "device_id": self.android_device_id,
            "mutation_token": token,
            "_uuid": self.uuid,
            "btt_dual_send": "false",
            "nav_chain": (
                "1qT:feed_timeline:1,1qT:feed_timeline:2,1qT:feed_timeline:3,"
                "7Az:direct_inbox:4,7Az:direct_inbox:5,5rG:direct_thread:7"
            ),
            "is_ae_dual_send": "false",
            "offline_threading_id": token,
        }
        if "http" in text:
            method = "link"
            kwargs["link_text"] = text
            kwargs["link_urls"] = dumps(re.findall(r"(https?://[^\s]+)", text))
        else:
            kwargs["text"] = text
        if thread_ids:
            kwargs["thread_ids"] = dumps([int(tid) for tid in thread_ids])
        if user_ids:
            kwargs["recipient_users"] = dumps([[int(uid) for uid in user_ids]])
        if reply_to_message:
            kwargs["replied_to_action_source"] = "swipe"
            kwargs["replied_to_item_id"] = reply_to_message.id
            kwargs["replied_to_client_context"] = reply_to_message.client_context
        result = self.private_request(
            f"direct_v2/threads/broadcast/{method}/",
            data=self.with_default_data(kwargs),
            with_signature=False,
        )
        return extract_direct_message(result["payload"])

    def direct_send_photo(
        self, path: Path, user_ids: List[int] = [], thread_ids: List[int] = []
    ) -> DirectMessage:
        """
        Send a direct photo to list of users or threads

        Parameters
        ----------
        path: Path
            Path to photo that will be posted on the thread
        user_ids: List[int]
            List of unique identifier of Users id
        thread_ids: List[int]
            List of unique identifier of Direct Message thread id

        Returns
        -------
        DirectMessage
            An object of DirectMessage
        """
        return self.direct_send_file(path, user_ids, thread_ids, content_type="photo")

    def direct_send_video(
        self, path: Path, user_ids: List[int] = [], thread_ids: List[int] = []
    ) -> DirectMessage:
        """
        Send a direct video to list of users or threads

        Parameters
        ----------
        path: Path
            Path to video that will be posted on the thread
        user_ids: List[int]
            List of unique identifier of Users id
        thread_ids: List[int]
            List of unique identifier of Direct Message thread id

        Returns
        -------
        DirectMessage
            An object of DirectMessage
        """
        return self.direct_send_file(path, user_ids, thread_ids, content_type="video")

    def direct_send_file(
        self,
        path: Path,
        user_ids: List[int] = [],
        thread_ids: List[int] = [],
        content_type: str = "photo",
    ) -> DirectMessage:
        """
        Send a direct file to list of users or threads

        Parameters
        ----------
        path: Path
            Path to file that will be posted on the thread
        user_ids: List[int]
            List of unique identifier of Users id
        thread_ids: List[int]
            List of unique identifier of Direct Message thread id

        Returns
        -------
        DirectMessage
            An object of DirectMessage
        """
        assert self.user_id, "Login required"
        assert (user_ids or thread_ids) and not (
            user_ids and thread_ids
        ), "Specify user_ids or thread_ids, but not both"
        method = f"configure_{content_type}"
        token = self.generate_mutation_token()
        nav_chains = [
            (
                "6xQ:direct_media_picker_photos_fragment:1,5rG:direct_thread:2,"
                "5ME:direct_quick_camera_fragment:3,5ME:direct_quick_camera_fragment:4,"
                "4ju:reel_composer_preview:5,5rG:direct_thread:6,5rG:direct_thread:7,"
                "6xQ:direct_media_picker_photos_fragment:8,5rG:direct_thread:9"
            ),
            (
                "1qT:feed_timeline:1,7Az:direct_inbox:2,7Az:direct_inbox:3,"
                "5rG:direct_thread:4,6xQ:direct_media_picker_photos_fragment:5,"
                "5rG:direct_thread:6,5rG:direct_thread:7,"
                "6xQ:direct_media_picker_photos_fragment:8,5rG:direct_thread:9"
            ),
        ]
        kwargs = {}
        data = {
            "action": "send_item",
            "is_shh_mode": "0",
            "send_attribution": "direct_thread",
            "client_context": token,
            "mutation_token": token,
            "nav_chain": random.choices(nav_chains),
            "offline_threading_id": token,
        }
        if content_type == "video":
            data["video_result"] = ""
            kwargs["to_direct"] = True
        if content_type == "photo":
            data["send_attribution"] = "inbox"
            data["allow_full_aspect_ratio"] = "true"
        if user_ids:
            data["recipient_users"] = dumps([[int(uid) for uid in user_ids]])
        if thread_ids:
            data["thread_ids"] = dumps([int(tid) for tid in thread_ids])
        path = Path(path)
        upload_id = str(int(time.time() * 1000))
        upload_id, width, height = getattr(self, f"{content_type}_rupload")(
            path, upload_id, **kwargs
        )[:3]
        data["upload_id"] = upload_id
        # data['content_type'] = content_type
        result = self.private_request(
            f"direct_v2/threads/broadcast/{method}/",
            data=self.with_default_data(data),
            with_signature=False,
        )
        return extract_direct_message(result["payload"])

    def direct_users_presence(self, user_ids: List[int]) -> Dict:
        """
        Get a presence of User

        Parameters
        ----------
        user_ids: List[int]
            List of unique identifier of Users ID

        Returns
        -------
        Dict
            Dict with User's presences
        """
        assert self.user_id, "Login Required"
        data = {
            "_uuid": self.uuid,
            "subscriptions_off": "false",
            "request_data": dumps([int(uid) for uid in user_ids]),
        }
        result = self.private_request(
            "direct_v2/fetch_and_subscribe_presence/",
            data=self.with_default_data(data),
            with_signature=False,
        )
        assert (
            result.get("status") == "ok"
        ), f"Failed to retrieve presence of user_id={user_ids}"
        return result

    def direct_active_presence(self) -> Dict:
        """
        Getting active presences in Direct

        Returns
        -------
        Dict
            Dict with active presences
        """
        params = {"recent_thread_limit": 0, "suggested_followers_limit": 100}
        result = self.private_request(
            "direct_v2/get_presence_active_now/", params=params
        )
        assert result.get("status") == "ok", "Failed to retrieve active presences"

        return result.get("user_presence", {})

    def direct_message_seen(self, thread_id: int, message_id: int) -> bool:
        """
        Mark direct message as seen

        Parameters
        ----------
        thread_id: int
            ID of the thread with message
        message_id: int
            ID of the message to mark as seen

        Returns
        -------
        bool
            A boolean value
        """
        token = self.generate_mutation_token()
        data = {
            "thread_id": str(thread_id),
            "action": "mark_seen",
            "client_context": token,
            "_uuid": self.uuid,
            "offline_threading_id": token,
        }
        result = self.private_request(
            f"direct_v2/threads/{thread_id}/items/{message_id}/seen/",
            data=data,
            with_signature=False,
        )
        return result.get("status", "") == "ok"

    def direct_send_seen(self, thread_id: int) -> bool:
        """
        Mark direct thread as seen

        Parameters
        ----------
        thread_id: int
            ID of thread to mark as read

        Returns
        -------
        bool
            A boolean value
        """
        thread = self.direct_thread(thread_id=thread_id)
        return self.direct_message_seen(thread_id, thread.messages[0].id)

    def direct_search(
        self, query: str, mode: SEARCH_MODE = "universal"
    ) -> List[UserShort]:
        """
        Search threads by query

        Parameters
        ----------
        query: str
            Text query, e.g. username
        mode: str, optional
            Mode for searching, by deafult "universal"

        Returns
        -------
        List[UserShort]
            List of short version of Users
        """
        assert mode in SEARCH_MODES, f'Unsupported mode="{mode}" {SEARCH_MODES}'

        params = {
            "max_ig_bus_results": "10",
            "mode": mode,
            "show_threads": "true",
            "query": str(query),
            "max_ig_results": "10",
            "max_fb_results": "0",
        }
        result = self.private_request(
            "direct_v2/ranked_recipients/",
            params=params,
        )
        return [
            extract_user_short(item.get("user", {}))
            for item in result.get("ranked_recipients", [])
            if "user" in item
            and item.get("user", {}).get("username", "")
            != ""  # Check to exclude suggestions from FB
        ]

    def direct_message_search(
        self, query: str
    ) -> List[Tuple[DirectMessage, DirectShortThread]]:
        """
        Search query mentions in direct messages

        Parameters
        ----------
        query: str
            Text query

        Returns
        -------
        List[Tuple[DirectMessage, DirectThread]]
            List of Tuples with DirectMessage (matched query) and its DirectThread
        """
        params = {
            "offsets": '{"message_content":"0","reshared_content":""}',
            "query": query,
            "result_types": '["message_content","reshared_content"]',
        }
        result = self.private_request(
            "direct_v2/search_secondary/",
            params=params,
        )
        assert result.get("status", "") == "ok"
        search_results = result.get("message_search_results", {})

        data = []
        for item in search_results.get("message_search_result_items", []):
            message = item.get("matched_message_info", {})
            thread = item.get("thread", {})
            data.append(
                (
                    extract_direct_message(message.get("item_info", {})),
                    extract_direct_short_thread(thread),
                )
            )
        return data

    def direct_thread_by_participants(self, user_ids: List[int]) -> Dict:
        """
        Get direct thread by participants

        Parameters
        ----------
        user_ids: List[int]
            List of unique identifier of Users id

        Returns
        -------
        Dict
            Some information about thread.
            List of UserShort under "users" key
        """
        recipient_users = dumps([int(uid) for uid in user_ids])
        result = self.private_request(
            "direct_v2/threads/get_by_participants/",
            params={"recipient_users": recipient_users, "seq_id": 2580572, "limit": 20},
        )
        users = []
        for user in result.get("users", []):
            # User dict object also contains fields like follower_count,
            #     following_count, mutual_followers_count, media_count
            users.append(
                UserShort(
                    pk=user["pk"],
                    username=user["username"],
                    full_name=user["full_name"],
                    profile_pic_url=user["profile_pic_url"],
                    is_private=user["is_private"],
                )
            )
        result["users"] = users
        return result

    def direct_thread_hide(self, thread_id: int, move_to_spam: bool = False) -> bool:
        """
        Hide (delete) a thread
        When you click delete, Instagram hides a thread

        Parameters
        ----------
        thread_id: int
            ID of thread to hide
        move_to_spam: bool, optional
            True - move to the hidden requests (spam) folder, False - just hide (default - False)

        Returns
        -------
        bool
            A boolean value
        """
        assert self.user_id, "Login required"

        result = self.private_request(
            f"direct_v2/threads/{thread_id}/hide/",
            data={
                "should_move_future_requests_to_spam": move_to_spam,
                "_uuid": self.uuid,
            },
            with_signature=False,
        )
        return result.get("status", "") == "ok"

    def direct_media_share(
        self,
        media_id: str,
        user_ids: List[int],
        send_attribute: SEND_ATTRIBUTES_MEDIA = "feed_timeline",
        media_type: str = "photo",
    ) -> DirectMessage:
        """
        Share a media to list of users

        Parameters
        ----------
        media_id: str
            Unique Media ID
        user_ids: List[int]
            List of unique identifier of Users id
        send_attribute: str, optional
            Sending option. Default is "feed_timeline"
        media_type: str, optional
            Type of the shared media. Default is "photo", also can be "video"

        Returns
        -------
        DirectMessage
            An object of DirectMessage
        """
        assert self.user_id, "Login required"
        token = self.generate_mutation_token()
        media_id = self.media_id(media_id)
        recipient_users = dumps([[int(uid) for uid in user_ids]])
        kwargs = {
            "recipient_users": recipient_users,
            "action": "send_item",
            "is_shh_mode": "0",
            "send_attribution": send_attribute,
            "client_context": token,
            "media_id": media_id,
            "device_id": self.android_device_id,
            "mutation_token": token,
            "_uuid": self.uuid,
            "btt_dual_send": "false",
            "nav_chain": (
                "1qT:feed_timeline:1,1qT:feed_timeline:2,1qT:feed_timeline:3,"
                "7Az:direct_inbox:4,7Az:direct_inbox:5,5rG:direct_thread:7"
            ),
            "is_ae_dual_send": "false",
            "offline_threading_id": token,
        }
        if send_attribute in ["feed_contextual_chain", "feed_short_url"]:
            kwargs["inventory_source"] = "recommended_explore_grid_cover_model"
        if send_attribute == "feed_timeline":
            kwargs["inventory_source"] = "media_or_ad"

        result = self.private_request(
            "direct_v2/threads/broadcast/media_share/",
            params={"media_type": media_type},
            data=self.with_default_data(kwargs),
            with_signature=False,
        )
        assert result.get("status", "") == "ok"

        return extract_direct_message(result["payload"])

    def direct_story_share(
        self, story_id: str, user_ids: List[int] = [], thread_ids: List[int] = []
    ) -> DirectMessage:
        """
        Share a story to list of users

        Parameters
        ----------
        story_id: str
            Unique Story ID
        user_ids: List[int]
            List of unique identifier of Users id
        thread_ids: List[int]
            List of unique identifier of Users id

        Returns
        -------
        DirectMessage
            An object of DirectMessage
        """
        assert self.user_id, "Login required"
        assert (user_ids or thread_ids) and not (
            user_ids and thread_ids
        ), "Specify user_ids or thread_ids, but not both"
        story_id = self.media_id(story_id)
        story_pk = self.media_pk(story_id)
        token = self.generate_mutation_token()
        data = {
            "action": "send_item",
            "is_shh_mode": "0",
            "send_attribution": "reel_feed_timeline",
            "client_context": token,
            "mutation_token": token,
            "nav_chain": (
                "1qT:feed_timeline:1,ReelViewerFragment:reel_feed_timeline:4,"
                "DirectShareSheetFragment:direct_reshare_sheet:5"
            ),
            "reel_id": story_pk,
            "containermodule": "reel_feed_timeline",
            "story_media_id": story_id,
            "offline_threading_id": token,
        }
        if user_ids:
            data["recipient_users"] = dumps([[int(uid) for uid in user_ids]])
        if thread_ids:
            data["thread_ids"] = dumps([int(tid) for tid in thread_ids])
        result = self.private_request(
            "direct_v2/threads/broadcast/story_share/",
            # params={'story_type': 'video'},
            data=self.with_default_data(data),
            with_signature=False,
        )
        return extract_direct_message(result["payload"])

    def direct_thread_mark_unread(self, thread_id: int) -> bool:
        """
        Mark a thread as unread

        Parameters
        ----------
        thread_id: int
            Id of thread

        Returns
        -------
        bool
            A boolean value
        """
        data = self.with_default_data({})
        data.pop("_uid", None)
        data.pop("device_id", None)
        result = self.private_request(
            f"direct_v2/threads/{thread_id}/mark_unread/", data=data
        )
        return result["status"] == "ok"

    def direct_message_delete(self, thread_id: int, message_id: int) -> bool:
        """
        Delete a message from thread

        Parameters
        ----------
        thread_id: int
            Id of thread
        message_id: int
            Id of message

        Returns
        -------
        bool
            A boolean value
        """
        data = self.with_default_data({})
        data.pop("_uid", None)
        data.pop("device_id", None)
        result = self.private_request(
            f"direct_v2/threads/{thread_id}/items/{message_id}/delete/", data=data
        )
        return result["status"] == "ok"

    def direct_thread_mute(self, thread_id: int, revert: bool = False) -> bool:
        """
        Mute the thread

        Parameters
        ----------
        thread_id: int
            Id of thread
        revert: bool, optional
            If muted, whether or not to unmute. Default is False

        Returns
        -------
        bool
            A boolean value
        """
        name = "unmute" if revert else "mute"
        result = self.private_request(
            f"direct_v2/threads/{thread_id}/{name}/", data={"_uuid": self.uuid}
        )
        return result["status"] == "ok"

    def direct_thread_unmute(self, thread_id: int) -> bool:
        """
        Unmute the thread

        Parameters
        ----------
        thread_id: int
            Id of thread

        Returns
        -------
        bool
            A boolean value
        """
        return self.direct_thread_mute(thread_id, revert=True)

    def direct_thread_mute_video_call(
        self, thread_id: int, revert: bool = False
    ) -> bool:
        """
        Mute video call for the thread

        Parameters
        ----------
        thread_id: int
            Id of thread
        revert: bool, optional
            If muted, whether or not to unmute. Default is False

        Returns
        -------
        bool
            A boolean value
        """
        name = "unmute_video_call" if revert else "mute_video_call"
        result = self.private_request(
            f"direct_v2/threads/{thread_id}/{name}/", data={"_uuid": self.uuid}
        )
        return result["status"] == "ok"

    def direct_thread_unmute_video_call(self, thread_id: int) -> bool:
        """
        Unmute video call for the thread

        Parameters
        ----------
        thread_id: int
            Id of thread

        Returns
        -------
        bool
            A boolean value
        """
        return self.direct_thread_mute_video_call(thread_id, revert=True)

    def direct_profile_share(
        self, user_id: str, user_ids: List[int] = [], thread_ids: List[int] = []
    ) -> DirectMessage:
        """
        Share a profile to list of users

        Parameters
        ----------
        user_id: str
            Unique User ID (profile)
        user_ids: List[int]
            List of unique identifier of Users id (recipients)
        thread_ids: List[int]
            List of unique identifier of Users id

        Returns
        -------
        DirectMessage
            An object of DirectMessage
        """
        assert self.user_id, "Login required"
        assert (user_ids or thread_ids) and not (
            user_ids and thread_ids
        ), "Specify user_ids or thread_ids, but not both"
        token = self.generate_mutation_token()
        kwargs = {
            "profile_user_id": user_id,
            "action": "send_item",
            "is_shh_mode": "0",
            "send_attribution": "profile",
            "client_context": token,
            "device_id": self.android_device_id,
            "mutation_token": token,
            "_uuid": self.uuid,
            "btt_dual_send": "false",
            "nav_chain": (
                "1qT:feed_timeline:1,1qT:feed_timeline:2,1qT:feed_timeline:3,"
                "7Az:direct_inbox:4,7Az:direct_inbox:5,5rG:direct_thread:7"
            ),
            "is_ae_dual_send": "false",
            "offline_threading_id": token,
        }
        if user_ids:
            kwargs["recipient_users"] = dumps([[int(uid) for uid in user_ids]])
        if thread_ids:
            kwargs["thread_ids"] = dumps([int(tid) for tid in thread_ids])
        result = self.private_request(
            "direct_v2/threads/broadcast/profile/",
            data=self.with_default_data(kwargs),
            with_signature=False,
        )
        assert result.get("status", "") == "ok"

        return extract_direct_message(result["payload"])

    def direct_media(self, thread_id: int, amount: int = 20) -> List[Media]:
        """
        Get all the media from a thread

        Parameters
        ----------
        thread_id: int
            Unique identifier of a Direct Message thread

        amount: int, optional
            Maximum number of media to return, default is 20

        Returns
        -------
        List[Media]
            A list of objects of Media
        """
        assert self.user_id, "Login required"
        params = {"limit": 20, "media_type": "photos_and_videos"}
        max_timestamp = None
        items = []
        while True:
            if max_timestamp:
                params["max_timestamp"] = max_timestamp
            try:
                result = self.private_request(
                    f"direct_v2/threads/{thread_id}/media/", params=params
                )
            except ClientNotFoundError as e:
                raise DirectThreadNotFound(e, thread_id=thread_id, **self.last_json)
            for item in result["items"]:
                media = item.get("media")
                items.append(extract_direct_media(media))
                max_timestamp = item.get("timestamp")
            more_available = result.get("more_available")
            if not more_available or (amount and len(items) >= amount):
                break
        if amount:
            items = items[:amount]
        return items



================================================
FILE: instagrapi/mixins/explore.py
================================================
class ExploreMixin:
    """
    Helpers for the explore page
    """

    def explore_page(self):
        """
        Get explore page

        Returns
        -------
        dict
        """
        return self.private_request("discover/topical_explore/")

    def report_explore_media(self, media_pk: int):
        """
        Report media in explore page. This is equivalent to the "not interested" button

        Parameters
        ----------
        media_pk: int
            Media PK
        Returns
        -------
        bool
            True if success
        """
        params = {
            "m_pk": media_pk,
        }
        result = self.private_request("discover/explore_report/", params=params)
        return result["explore_report_status"] == "OK"

    def explore_page_media_info(self, media_pk: int):
        """
        Returns media information for a media item on the explore page

        This is the API call that happens when you're on the explore page
        and you click into a media item. It returns information about that media item
        like comments, likes, etc.
        """
        return self.private_request(
            "/v1/discover/media_metadata/", params={"media_id": media_pk}
        )["media_or_ad"]



================================================
FILE: instagrapi/mixins/fbsearch.py
================================================
from typing import Dict, List, Tuple, Union

from instagrapi.extractors import (
    extract_hashtag_v1,
    extract_location,
    extract_track,
    extract_user_short,
)
from instagrapi.types import Hashtag, Location, Track, UserShort


class FbSearchMixin:
    def fbsearch_places(
        self, query: str, lat: float = 40.74, lng: float = -73.94
    ) -> List[Location]:
        params = {
            "search_surface": "places_search_page",
            "timezone_offset": self.timezone_offset,
            "lat": lat,
            "lng": lng,
            "count": 30,
            "query": query,
        }
        result = self.private_request("fbsearch/places/", params=params)
        locations = []
        for item in result["items"]:
            locations.append(extract_location(item["location"]))
        return locations

    def fbsearch_topsearch_flat(self, query: str) -> List[dict]:
        params = {
            "search_surface": "top_search_page",
            "context": "blended",
            "timezone_offset": self.timezone_offset,
            "count": 30,
            "query": query,
        }
        result = self.private_request("fbsearch/topsearch_flat/", params=params)
        return result["list"]

    def search_users(self, query: str) -> List[UserShort]:
        params = {
            "search_surface": "user_search_page",
            "timezone_offset": self.timezone_offset,
            "count": 30,
            "q": query,
        }
        result = self.private_request("users/search/", params=params)
        return [extract_user_short(item) for item in result["users"]]

    def search_music(self, query: str) -> List[Track]:
        params = {
            "query": query,
            "browse_session_id": self.generate_uuid(),
        }
        result = self.private_request("music/audio_global_search/", params=params)
        return [extract_track(item["track"]) for item in result["items"]]

    def search_hashtags(self, query: str) -> List[Hashtag]:
        params = {
            "search_surface": "hashtag_search_page",
            "timezone_offset": self.timezone_offset,
            "count": 30,
            "q": query,
        }
        result = self.private_request("tags/search/", params=params)
        return [extract_hashtag_v1(ht) for ht in result["results"]]

    def fbsearch_suggested_profiles(self, user_id: str) -> List[UserShort]:
        params = {
            "target_user_id": user_id,
            "include_friendship_status": "true",
        }
        result = self.private_request("fbsearch/accounts_recs/", params=params)
        return result["users"]

    def fbsearch_recent(self) -> List[Tuple[int, Union[UserShort, Hashtag, Dict]]]:
        """
        Retrieves recently searched results

        Returns
        -------
        List[Tuple[int, Union[UserShort, Hashtag, Dict]]]
            Returns list of Tuples where first value is timestamp of searh, second is retrived result
        """
        result = self.private_request("fbsearch/recent_searches/")
        assert result.get("status", "") == "ok", "Failed to retrieve recent searches"

        data = []
        for item in result.get("recent", []):
            if "user" in item.keys():
                data.append(
                    (item.get("client_time", None), extract_user_short(item["user"]))
                )
            if "hashtag" in item.keys():
                hashtag = item.get("hashtag")
                hashtag["media_count"] = hashtag.pop("formatted_media_count")
                data.append((item.get("client_time", None), Hashtag(**hashtag)))
            if "keyword" in item.keys():
                data.append((item.get("client_time", None), item["keyword"]))
        return data



================================================
FILE: instagrapi/mixins/fundraiser.py
================================================
class FundraiserMixin:
    """
    Helpers for the fundraisers.
    """

    def standalone_fundraiser_info_v1(self, user_id: str):
        """
        Get fundraiser info.

        Parameters
        ----------
        user_id: str
            User id of an instagram account

        Returns
        -------
        dict
        """
        user_id = str(user_id)
        return self.private_request(f"fundraiser/{user_id}/standalone_fundraiser_info/")



================================================
FILE: instagrapi/mixins/hashtag.py
================================================
import base64
import json
from typing import List, Tuple

from instagrapi.exceptions import (
    ClientError,
    ClientLoginRequired,
    ClientUnauthorizedError,
    HashtagNotFound,
    WrongCursorError,
)
from instagrapi.extractors import (
    extract_hashtag_gql,
    extract_hashtag_v1,
    extract_media_v1,
)
from instagrapi.types import Hashtag, Media
from instagrapi.utils import dumps


class HashtagMixin:
    """
    Helpers for managing Hashtag
    """

    def hashtag_info_a1(self, name: str, max_id: str = None) -> Hashtag:
        """
        Get information about a hashtag by Public Web API

        Parameters
        ----------
        name: str
            Name of the hashtag

        max_id: str
            Max ID, default value is None

        Returns
        -------
        Hashtag
            An object of Hashtag
        """
        params = {"max_id": max_id} if max_id else None
        try:
            data = self.public_a1_request(f"/explore/tags/{name}/", params=params)
        except ClientUnauthorizedError:
            self.inject_sessionid_to_public()
            data = self.public_a1_request(f"/explore/tags/{name}/", params=params)
        if not data.get("hashtag"):
            raise HashtagNotFound(name=name, **data)
        return extract_hashtag_gql(data["hashtag"])

    def hashtag_info_gql(
        self, name: str, amount: int = 12, end_cursor: str = None
    ) -> Hashtag:
        """
        Get information about a hashtag by Public Graphql API

        Parameters
        ----------
        name: str
            Name of the hashtag

        amount: int, optional
            Maximum number of media to return, default is 12

        end_cursor: str, optional
            End Cursor, default value is None

        Returns
        -------
        Hashtag
            An object of Hashtag
        """
        variables = {"tag_name": name, "show_ranked": False, "first": int(amount)}
        if end_cursor:
            variables["after"] = end_cursor
        data = self.public_graphql_request(
            variables, query_hash="f92f56d47dc7a55b606908374b43a314"
        )
        if not data.get("hashtag"):
            raise HashtagNotFound(name=name, **data)
        return extract_hashtag_gql(data["hashtag"])

    def hashtag_info_v1(self, name: str) -> Hashtag:
        """
        Get information about a hashtag by Private Mobile API

        Parameters
        ----------
        name: str
            Name of the hashtag

        Returns
        -------
        Hashtag
            An object of Hashtag
        """
        result = self.private_request(f"tags/{name}/info/")
        return extract_hashtag_v1(result)

    def hashtag_info(self, name: str) -> Hashtag:
        """
        Get information about a hashtag

        Parameters
        ----------
        name: str
            Name of the hashtag

        Returns
        -------
        Hashtag
            An object of Hashtag
        """
        try:
            hashtag = self.hashtag_info_a1(name)
        except Exception:
            # Users do not understand the output of such information and create bug reports
            # such this - https://github.com/subzeroid/instagrapi/issues/364
            # if not isinstance(e, ClientError):
            #     self.logger.exception(e)
            hashtag = self.hashtag_info_v1(name)
        return hashtag

    def hashtag_related_hashtags(self, name: str) -> List[Hashtag]:
        """
        Get related hashtags from a hashtag

        Parameters
        ----------
        name: str
            Name of the hashtag

        Returns
        -------
        List[Hashtag]
            List of objects of Hashtag
        """
        data = self.public_a1_request(f"/explore/tags/{name}/")
        if not data.get("hashtag"):
            raise HashtagNotFound(name=name, **data)
        return [
            extract_hashtag_gql(item["node"])
            for item in data["hashtag"]["edge_hashtag_to_related_tags"]["edges"]
        ]

    def hashtag_medias_a1_chunk(
        self, name: str, max_amount: int = 27, tab_key: str = "", end_cursor: str = None
    ) -> Tuple[List[Media], str]:
        """
        Get chunk of medias and end_cursor by Public Web API

        Parameters
        ----------
        name: str
            Name of the hashtag
        max_amount: int, optional
            Maximum number of media to return, default is 27
        tab_key: str, optional
            Tab Key, default value is ""
        end_cursor: str, optional
            End Cursor, default value is None

        Returns
        -------
        Tuple[List[Media], str]
            List of objects of Media and end_cursor
        """
        assert tab_key in (
            "recent",
            "top",
        ), 'You must specify one of the options for "tab_key" ("recent" or "top")'
        url = f"/explore/tags/{name}/"
        medias = []
        while True:
            params = {"max_id": end_cursor} if end_cursor else {}
            try:
                data = self.public_a1_request(url, params=params)
            except (ClientUnauthorizedError, ClientLoginRequired):
                self.inject_sessionid_to_public()
                data = self.public_a1_request(url, params=params)

            result = data["data"][tab_key]
            for section in result["sections"]:
                layout_content = section.get("layout_content") or {}
                nodes = layout_content.get("medias") or []
                for node in nodes:
                    if max_amount and len(medias) >= max_amount:
                        break
                    media = extract_media_v1(node["media"])
                    # media_pk = node["media"]["id"]
                    # if media_pk in unique_set:
                    #     continue
                    # unique_set.add(media_pk)
                    # check contains hashtag in caption
                    # if f"#{name}" not in media.caption_text:
                    #     continue
                    medias.append(media)
            if not result["more_available"]:
                break
            if max_amount and len(medias) >= max_amount:
                break
            end_cursor = result["next_max_id"]
        return medias, end_cursor

    def hashtag_medias_a1(
        self, name: str, amount: int = 27, tab_key: str = ""
    ) -> List[Media]:
        """
        Get medias for a hashtag by Public Web API

        Parameters
        ----------
        name: str
            Name of the hashtag
        amount: int, optional
            Maximum number of media to return, default is 27
        tab_key: str, optional
            Tab Key, default value is ""

        Returns
        -------
        List[Media]
            List of objects of Media
        """
        medias, _ = self.hashtag_medias_a1_chunk(name, amount, tab_key)
        if amount:
            medias = medias[:amount]
        return medias

    def hashtag_medias_v1_chunk(
        self, name: str, max_amount: int = 27, tab_key: str = "", max_id: str = None
    ) -> Tuple[List[Media], str]:
        """
        Get chunk of medias for a hashtag and max_id (cursor) by Private Mobile API

        Parameters
        ----------
        name: str
            Name of the hashtag
        max_amount: int, optional
            Maximum number of media to return, default is 27
        tab_key: str, optional
            Tab Key, default value is ""
        max_id: str
            Max ID, default value is None

        Returns
        -------
        Tuple[List[Media], str]
            List of objects of Media and max_id
        """
        assert tab_key in (
            "top",
            "recent",
            "clips",
        ), 'You must specify one of the options for "tab_key" ("top", "recent", "clips")'
        media_recency_filter = {
            "top": "default",
            "recent": "top_recent_posts",
        }
        data = {
            "media_recency_filter": media_recency_filter.get(tab_key, tab_key),
            # "page": 1,
            "_uuid": self.uuid,
            "include_persistent": "false",
            "rank_token": self.rank_token,
        }
        if max_id:
            try:
                [page_id, nm_ids] = json.loads(base64.b64decode(max_id))
            except Exception:
                raise WrongCursorError()
            data["max_id"] = page_id
            data["next_media_ids"] = dumps(nm_ids)
        medias = []
        result = self.private_request(
            f"tags/{name}/sections/",
            # params={"max_id": max_id} if max_id else {},
            data=data,
            with_signature=False,
        )
        next_max_id = None
        if result.get("next_max_id"):
            np = result.get("next_max_id")
            ids = result.get("next_media_ids")
            next_max_id = base64.b64encode(json.dumps([np, ids]).encode()).decode()
        for section in result["sections"]:
            layout_content = section.get("layout_content") or {}
            nodes = layout_content.get("medias") or []
            for node in nodes:
                if max_amount and len(medias) >= max_amount:
                    break
                media = extract_media_v1(node["media"])
                # check contains hashtag in caption
                # if f"#{name}" not in media.caption_text:
                #     continue
                medias.append(media)
        # max_id = result["next_max_id"]
        if not result["more_available"]:
            next_max_id = None  # stop
        return medias, next_max_id

    def hashtag_medias_v1(
        self, name: str, amount: int = 27, tab_key: str = ""
    ) -> List[Media]:
        """
        Get medias for a hashtag by Private Mobile API

        Parameters
        ----------
        name: str
            Name of the hashtag
        amount: int, optional
            Maximum number of media to return, default is 27
        tab_key: str, optional
            Tab Key, default value is ""

        Returns
        -------
        List[Media]
            List of objects of Media
        """
        medias = []
        max_id = None
        while True:
            items, max_id = self.hashtag_medias_v1_chunk(name, amount, tab_key, max_id)
            medias.extend(items)
            if amount and len(medias) >= amount:
                break
            if not max_id:
                break
        if amount:
            medias = medias[:amount]
        return medias

    def hashtag_medias_top_a1(self, name: str, amount: int = 9) -> List[Media]:
        """
        Get top medias for a hashtag by Public Web API

        Parameters
        ----------
        name: str
            Name of the hashtag
        amount: int, optional
            Maximum number of media to return, default is 9

        Returns
        -------
        List[Media]
            List of objects of Media
        """
        return self.hashtag_medias_a1(name, amount, tab_key="top")

    def hashtag_medias_top_v1(self, name: str, amount: int = 9) -> List[Media]:
        """
        Get top medias for a hashtag by Private Mobile API

        Parameters
        ----------
        name: str
            Name of the hashtag
        amount: int, optional
            Maximum number of media to return, default is 9

        Returns
        -------
        List[Media]
            List of objects of Media
        """
        return self.hashtag_medias_v1(name, amount, tab_key="top")

    def hashtag_medias_top(self, name: str, amount: int = 9) -> List[Media]:
        """
        Get top medias for a hashtag

        Parameters
        ----------
        name: str
            Name of the hashtag
        amount: int, optional
            Maximum number of media to return, default is 9

        Returns
        -------
        List[Media]
            List of objects of Media
        """
        try:
            medias = self.hashtag_medias_top_a1(name, amount)
        except ClientError:
            medias = self.hashtag_medias_top_v1(name, amount)
        return medias

    def hashtag_medias_recent_a1(self, name: str, amount: int = 71) -> List[Media]:
        """
        Get recent medias for a hashtag by Public Web API

        Parameters
        ----------
        name: str
            Name of the hashtag
        amount: int, optional
            Maximum number of media to return, default is 71

        Returns
        -------
        List[Media]
            List of objects of Media
        """
        return self.hashtag_medias_a1(name, amount, tab_key="recent")

    def hashtag_medias_recent_v1(self, name: str, amount: int = 27) -> List[Media]:
        """
        Get recent medias for a hashtag by Private Mobile API

        Parameters
        ----------
        name: str
            Name of the hashtag
        amount: int, optional
            Maximum number of media to return, default is 71

        Returns
        -------
        List[Media]
            List of objects of Media
        """
        return self.hashtag_medias_v1(name, amount, tab_key="recent")

    def hashtag_medias_recent(self, name: str, amount: int = 27) -> List[Media]:
        """
        Get recent medias for a hashtag

        Parameters
        ----------
        name: str
            Name of the hashtag
        amount: int, optional
            Maximum number of media to return, default is 71

        Returns
        -------
        List[Media]
            List of objects of Media
        """
        try:
            medias = self.hashtag_medias_recent_a1(name, amount)
        except ClientError:
            medias = self.hashtag_medias_recent_v1(name, amount)
        return medias

    def hashtag_medias_reels_v1(self, name: str, amount: int = 27) -> List[Media]:
        """
        Get reels medias for a hashtag by Private Mobile API

        Parameters
        ----------
        name: str
            Name of the hashtag
        amount: int, optional
            Maximum number of media to return, default is 71

        Returns
        -------
        List[Media]
            List of objects of Media
        """
        return self.hashtag_medias_v1(name, amount, tab_key="clips")

    def hashtag_follow(self, hashtag: str, unfollow: bool = False) -> bool:
        """
        Follow to hashtag
        Parameters
        ----------
        hashtag: str
            Unique identifier of a Hashtag
        unfollow: bool, optional
            Unfollow when True
        Returns
        -------
        bool
            A boolean value
        """
        assert self.user_id, "Login required"
        name = "unfollow" if unfollow else "follow"
        data = self.with_action_data({"user_id": self.user_id})
        result = self.private_request(
            f"web/tags/{name}/{hashtag}/", domain="www.instagram.com", data=data
        )
        return result["status"] == "ok"

    def hashtag_unfollow(self, hashtag: str) -> bool:
        """
        Unfollow to hashtag
        Parameters
        ----------
        hashtag: str
            Unique identifier of a Hashtag
        Returns
        -------
        bool
            A boolean value
        """
        return self.hashtag_follow(hashtag, unfollow=True)



================================================
FILE: instagrapi/mixins/highlight.py
================================================
import json
import random
import time
from pathlib import Path
from typing import Dict, List
from urllib.parse import urlparse

from instagrapi import config
from instagrapi.exceptions import HighlightNotFound
from instagrapi.extractors import extract_highlight_v1
from instagrapi.types import Highlight
from instagrapi.utils import dumps, vassert


class HighlightMixin:
    def highlight_pk_from_url(self, url: str) -> str:
        """
        Get Highlight PK from URL

        Parameters
        ----------
        url: str
            URL of highlight

        Returns
        -------
        str
            Highlight PK

        Examples
        --------
        https://www.instagram.com/stories/highlights/17895485201104054/ -> 17895485201104054
        """
        vassert("/highlights/" in url, "URL must contain '/highlights/'")
        path = urlparse(url).path
        parts = [p for p in path.split("/") if p and p.isdigit()]
        return str(parts[0])

    def user_highlights_v1(self, user_id: str, amount: int = 0) -> List[Highlight]:
        """
        Get a user's highlight

        Parameters
        ----------
        user_id: str
        amount: int, optional
            Maximum number of highlight to return, default is 0 (all highlights)

        Returns
        -------
        List[Highlight]
            A list of objects of Highlight
        """
        amount = int(amount)
        user_id = int(user_id)
        params = {
            "supported_capabilities_new": json.dumps(config.SUPPORTED_CAPABILITIES),
            "phone_id": self.phone_id,
            "battery_level": random.randint(25, 100),
            "panavision_mode": "",
            "is_charging": random.randint(0, 1),
            "is_dark_mode": random.randint(0, 1),
            "will_sound_on": random.randint(0, 1),
        }
        result = self.private_request(
            f"highlights/{user_id}/highlights_tray/", params=params
        )
        return [extract_highlight_v1(highlight) for highlight in result.get("tray", [])]

    def user_highlights(self, user_id: str, amount: int = 0) -> List[Highlight]:
        """
        Get a user's highlights

        Parameters
        ----------
        user_id: str
        amount: int, optional
            Maximum number of highlight to return, default is 0 (all highlights)

        Returns
        -------
        List[Highlight]
            A list of objects of Highlight
        """
        return self.user_highlights_v1(user_id, amount)

    def highlight_info_v1(self, highlight_pk: str) -> Highlight:
        """
        Get Highlight by pk or id (by Private Mobile API)

        Parameters
        ----------
        highlight_pk: str
            Unique identifier of Highlight

        Returns
        -------
        Highlight
            An object of Highlight type
        """
        highlight_id = f"highlight:{highlight_pk}"
        data = {
            "exclude_media_ids": "[]",
            "supported_capabilities_new": json.dumps(config.SUPPORTED_CAPABILITIES),
            "source": "profile",
            "_uid": str(self.user_id),
            "_uuid": self.uuid,
            "user_ids": [highlight_id],
        }
        result = self.private_request("feed/reels_media/", data)
        data = result["reels"]
        if highlight_id not in data:
            raise HighlightNotFound(highlight_pk=highlight_pk, **data)
        return extract_highlight_v1(data[highlight_id])

    def highlight_info(self, highlight_pk: str) -> Highlight:
        """
        Get Highlight by pk or id

        Parameters
        ----------
        highlight_pk: str
            Unique identifier of Highlight

        Returns
        -------
        Highlight
            An object of Highlight type
        """
        return self.highlight_info_v1(highlight_pk)

    def highlight_create(
        self,
        title: str,
        story_ids: List[str],
        cover_story_id: str = "",
        crop_rect: List[float] = [0.0, 0.21830457, 1.0, 0.78094524],
    ) -> Highlight:
        """
        Create highlight

        Parameters
        ----------
        title: str
            Title
        story_ids: List[str]
            List of story ids
        cover_story_id: str
            User story as cover, default is first of story_ids

        Returns
        -------
        Highlight
            An object of Highlight type
        """
        if not cover_story_id:
            cover_story_id = story_ids[0]
        data = {
            "supported_capabilities_new": json.dumps(config.SUPPORTED_CAPABILITIES),
            "source": "self_profile",
            "creation_id": str(int(time.time())),
            "_uid": str(self.user_id),
            "_uuid": self.uuid,
            "cover": dumps(
                {
                    "media_id": self.media_id(cover_story_id),
                    "crop_rect": dumps(crop_rect),
                }
            ),
            "title": title,
            "media_ids": dumps([self.media_id(sid) for sid in story_ids]),
        }
        result = self.private_request("highlights/create_reel/", data=data)
        return extract_highlight_v1(result["reel"])

    def highlight_edit(
        self,
        highlight_pk: str,
        title: str = "",
        cover: Dict = {},
        added_media_ids: List[str] = [],
        removed_media_ids: List[str] = [],
    ):
        data = {
            "supported_capabilities_new": json.dumps(config.SUPPORTED_CAPABILITIES),
            "source": "self_profile",
            "_uid": str(self.user_id),
            "_uuid": self.uuid,
            "added_media_ids": dumps(added_media_ids),
            "removed_media_ids": dumps(removed_media_ids),
        }
        if title:
            data["title"] = title
        if cover:
            data["cover"] = dumps(cover)
        result = self.private_request(
            f"highlights/highlight:{highlight_pk}/edit_reel/", data=data
        )
        return extract_highlight_v1(result["reel"])

    def highlight_change_title(self, highlight_pk: str, title: str) -> Highlight:
        """
        Change title for highlight

        Parameters
        ----------
        highlight_pk: str
            Unique identifier of Highlight
        title: str
            Title of Highlight

        Returns
        -------
        Highlight
        """
        return self.highlight_edit(highlight_pk, title=title)

    def highlight_change_cover(self, highlight_pk: str, cover_path: Path) -> Highlight:
        """
        Change cover for highlight

        Parameters
        ----------
        highlight_pk: str
            Unique identifier of Highlight
        cover_path: Path
            Path to photo

        Returns
        -------
        Highlight
        """
        upload_id, width, height = self.photo_rupload(Path(cover_path))
        cover = {"upload_id": str(upload_id), "crop_rect": "[0.0,0.0,1.0,1.0]"}
        return self.highlight_edit(highlight_pk, cover=cover)

    def highlight_add_stories(
        self, highlight_pk: str, added_media_ids: List[str]
    ) -> Highlight:
        """
        Add stories to highlight

        Parameters
        ----------
        highlight_pk: str
            Unique identifier of Highlight
        removed_media_ids: List[str]
            Remove stories from highlight

        Returns
        -------
        Highlight
        """
        return self.highlight_edit(highlight_pk, added_media_ids=added_media_ids)

    def highlight_remove_stories(
        self, highlight_pk: str, removed_media_ids: List[str]
    ) -> Highlight:
        """
        Remove stories from highlight

        Parameters
        ----------
        highlight_pk: str
            Unique identifier of Highlight
        removed_media_ids: List[str]
            Remove stories from highlight

        Returns
        -------
        Highlight
        """
        return self.highlight_edit(highlight_pk, removed_media_ids=removed_media_ids)

    def highlight_delete(self, highlight_pk: str) -> bool:
        """
        Delete highlight

        Parameters
        ----------
        highlight_pk: str
            Unique identifier of Highlight

        Returns
        -------
        bool
        """
        data = {"_uid": str(self.user_id), "_uuid": self.uuid}
        result = self.private_request(
            f"highlights/highlight:{highlight_pk}/delete_reel/", data=data
        )
        return result.get("status") == "ok"



================================================
FILE: instagrapi/mixins/igtv.py
================================================
import contextlib
import json
import random
import time
from pathlib import Path
from typing import Dict, List
from uuid import uuid4

from instagrapi import config
from instagrapi.exceptions import ClientError, IGTVConfigureError, IGTVNotUpload
from instagrapi.extractors import extract_media_v1
from instagrapi.types import Location, Media, Usertag
from instagrapi.utils import date_time_original

try:
    from PIL import Image
except ImportError:
    raise Exception("You don't have PIL installed. Please install PIL or Pillow>=8.1.1")


class DownloadIGTVMixin:
    """
    Helpers to download IGTV videos
    """

    def igtv_download(self, media_pk: int, folder: Path = "") -> str:
        """
        Download IGTV video

        Parameters
        ----------
        media_pk: int
            PK for the album you want to download
        folder: Path, optional
            Directory in which you want to download the album, default is "" and will download the files to working
                directory.

        Returns
        -------
        str
        """
        return self.video_download(media_pk, folder)

    def igtv_download_by_url(
        self, url: str, filename: str = "", folder: Path = ""
    ) -> str:
        """
        Download IGTV video using URL

        Parameters
        ----------
        url: str
            URL to download media from
        folder: Path, optional
            Directory in which you want to download the album, default is "" and will download the files to working
                directory.

        Returns
        -------
        str
        """
        return self.video_download_by_url(url, filename, folder)


class UploadIGTVMixin:
    """
    Helpers to upload IGTV videos
    """

    def igtv_upload(
        self,
        path: Path,
        title: str,
        caption: str,
        thumbnail: Path = None,
        usertags: List[Usertag] = [],
        location: Location = None,
        configure_timeout: int = 10,
        extra_data: Dict[str, str] = {},
    ) -> Media:
        """
        Upload IGTV to Instagram

        Parameters
        ----------
        path: Path
            Path to IGTV file
        title: str
            Title of the video
        caption: str
            Media caption
        thumbnail: Path, optional
            Path to thumbnail for IGTV. Default value is None, and it generates a thumbnail
        usertags: List[Usertag], optional
            List of users to be tagged on this upload, default is empty list.
        location: Location, optional
            Location tag for this upload, default is none
        configure_timeout: int
            Timeout between attempt to configure media (set caption, etc), default is 10
        extra_data: Dict[str, str], optional
            Dict of extra data, if you need to add your params, like {"share_to_facebook": 1}.

        Returns
        -------
        Media
            An object of Media class
        """
        path = Path(path)
        if thumbnail is not None:
            thumbnail = Path(thumbnail)
        upload_id = str(int(time.time() * 1000))
        thumbnail, width, height, duration = analyze_video(path, thumbnail)
        waterfall_id = str(uuid4())
        # upload_name example: '1576102477530_0_7823256191'
        upload_name = "{upload_id}_0_{rand}".format(
            upload_id=upload_id, rand=random.randint(1000000000, 9999999999)
        )
        # by segments bb2c1d0c127384453a2122e79e4c9a85-0-6498763
        # upload_name = "{hash}-0-{rand}".format(
        #     hash="bb2c1d0c127384453a2122e79e4c9a85", rand=random.randint(1111111, 9999999)
        # )
        rupload_params = {
            "is_igtv_video": "1",
            "retry_context": '{"num_step_auto_retry":0,"num_reupload":0,"num_step_manual_retry":0}',
            "media_type": "2",
            "xsharing_user_ids": json.dumps([self.user_id]),
            "upload_id": upload_id,
            "upload_media_duration_ms": str(int(duration * 1000)),
            "upload_media_width": str(width),
            "upload_media_height": str(height),
        }
        headers = {
            "Accept-Encoding": "gzip",
            "X-Instagram-Rupload-Params": json.dumps(rupload_params),
            "X_FB_VIDEO_WATERFALL_ID": waterfall_id,
            "X-Entity-Type": "video/mp4",
        }
        response = self.private.get(
            "https://{domain}/rupload_igvideo/{name}".format(
                domain=config.API_DOMAIN, name=upload_name
            ),
            headers=headers,
        )
        self.request_log(response)
        if response.status_code != 200:
            raise IGTVNotUpload(response=self.last_response, **self.last_json)
        with open(path, "rb") as fp:
            igtv_data = fp.read()
            igtv_len = str(len(igtv_data))
        headers = {
            "Offset": "0",
            "X-Entity-Name": upload_name,
            "X-Entity-Length": igtv_len,
            "Content-Type": "application/octet-stream",
            "Content-Length": igtv_len,
            **headers,
        }
        response = self.private.post(
            "https://{domain}/rupload_igvideo/{name}".format(
                domain=config.API_DOMAIN, name=upload_name
            ),
            data=igtv_data,
            headers=headers,
        )
        self.request_log(response)
        if response.status_code != 200:
            raise IGTVNotUpload(response=self.last_response, **self.last_json)
        # CONFIGURE
        self.igtv_composer_session_id = self.generate_uuid()
        for attempt in range(50):
            self.logger.debug(f"Attempt #{attempt} to configure IGTV: {path}")
            time.sleep(configure_timeout)
            try:
                configured = self.igtv_configure(
                    upload_id,
                    thumbnail,
                    width,
                    height,
                    duration,
                    title,
                    caption,
                    usertags,
                    location,
                    extra_data=extra_data,
                )
            except ClientError as e:
                if "Transcode not finished yet" in str(e):
                    """
                    Response 202 status:
                    {"message": "Transcode not finished yet.", "status": "fail"}
                    """
                    time.sleep(configure_timeout)
                    continue
                raise e
            else:
                if configured:
                    media = self.last_json.get("media")
                    self.expose()
                    return extract_media_v1(media)
        raise IGTVConfigureError(response=self.last_response, **self.last_json)

    def igtv_configure(
        self,
        upload_id: str,
        thumbnail: Path,
        width: int,
        height: int,
        duration: int,
        title: str,
        caption: str,
        usertags: List[Usertag] = [],
        location: Location = None,
        extra_data: Dict[str, str] = {},
    ) -> Dict:
        """
        Post Configure IGTV (send caption, thumbnail and more to Instagram)

        Parameters
        ----------
        upload_id: str
            Unique identifier for a IGTV video
        thumbnail: Path
            Path to thumbnail for IGTV
        width: int
            Width of the video in pixels
        height: int
            Height of the video in pixels
        duration: int
            Duration of the video in seconds
        title: str
            Title of the video
        caption: str
            Media caption
        usertags: List[Usertag], optional
            List of users to be tagged on this upload, default is empty list.
        location: Location, optional
            Location tag for this upload, default is None
        extra_data: Dict[str, str], optional
            Dict of extra data, if you need to add your params, like {"share_to_facebook": 1}.

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        self.photo_rupload(Path(thumbnail), upload_id)
        usertags = [
            {"user_id": tag.user.pk, "position": [tag.x, tag.y]} for tag in usertags
        ]
        data = {
            "igtv_ads_toggled_on": "0",
            "filter_type": "0",
            "timezone_offset": str(self.timezone_offset),
            "media_folder": "ScreenRecorder",
            "location": self.location_build(location),
            "source_type": "4",
            "title": title,
            "caption": caption,
            "usertags": json.dumps({"in": usertags}),
            "date_time_original": date_time_original(time.localtime()),
            "igtv_share_preview_to_feed": "1",
            "upload_id": upload_id,
            "igtv_composer_session_id": self.igtv_composer_session_id,
            "device": self.device,
            "length": duration,
            "clips": [{"length": duration, "source_type": "4"}],
            "extra": {"source_width": width, "source_height": height},
            "audio_muted": False,
            "poster_frame_index": 70,
            **extra_data,
        }
        return self.private_request(
            "media/configure_to_igtv/?video=1",
            self.with_default_data(data),
            with_signature=True,
        )


def analyze_video(path: Path, thumbnail: Path = None) -> tuple:
    """
    Analyze and crop thumbnail if need

    Parameters
    ----------
    path: Path
        Path to the video
    thumbnail: Path
        Path to thumbnail for IGTV

    Returns
    -------
    Tuple
        A tuple with (thumbail path, width, height, duration)
    """
    try:
        import moviepy.editor as mp
    except ImportError:
        try:
            import moviepy as mp
        except ImportError:
            raise Exception("Please install moviepy>=1.0.3 and retry")

    print(f'Analyzing IGTV file "{path}"')
    with contextlib.ExitStack() as stack:
        video = mp.VideoFileClip(str(path))
        width, height = video.size
        if not thumbnail:
            thumbnail = f"{path}.jpg"
            print(f'Generating thumbnail "{thumbnail}"...')
            video.save_frame(thumbnail, t=(video.duration / 2))
            crop_thumbnail(thumbnail)
        stack.enter_context(contextlib.closing(video))
    return thumbnail, width, height, video.duration


def crop_thumbnail(path: Path) -> bool:
    """
    Analyze and crop thumbnail if need

    Parameters
    ----------
    path: Path
        Path to the video

    Returns
    -------
    bool
        A boolean value
    """
    im = Image.open(str(path))
    width, height = im.size
    offset = (height / 1.78) / 2
    center = width / 2
    # Crop the center of the image
    im = im.crop((center - offset, 0, center + offset, height))
    with open(path, "w") as fp:
        im.save(fp)
        im.close()
    return True



================================================
FILE: instagrapi/mixins/insights.py
================================================
import time
from typing import Dict, List

from instagrapi.exceptions import ClientError, MediaError, UserError
from instagrapi.utils import json_value

POST_TYPES = ("ALL", "CAROUSEL_V2", "IMAGE", "SHOPPING", "VIDEO")
TIME_FRAMES = (
    "ONE_WEEK",
    "ONE_MONTH",
    "THREE_MONTHS",
    "SIX_MONTHS",
    "ONE_YEAR",
    "TWO_YEARS",
)
DATA_ORDERS = (
    "REACH_COUNT",
    "LIKE_COUNT",
    "FOLLOW",
    "SHARE_COUNT",
    "BIO_LINK_CLICK",
    "COMMENT_COUNT",
    "IMPRESSION_COUNT",
    "PROFILE_VIEW",
    "VIDEO_VIEW_COUNT",
    "SAVE_COUNT",
)

try:
    from typing import Literal

    POST_TYPE = Literal[POST_TYPES]
    TIME_FRAME = Literal[TIME_FRAMES]
    DATA_ORDERING = Literal[DATA_ORDERS]
except ImportError:
    # python <= 3.8
    POST_TYPE = TIME_FRAME = DATA_ORDERING = str


class InsightsMixin:
    """
    Helper class to get insights
    """

    def insights_media_feed_all(
        self,
        post_type: POST_TYPE = "ALL",
        time_frame: TIME_FRAME = "TWO_YEARS",
        data_ordering: DATA_ORDERING = "REACH_COUNT",
        count: int = 0,
        sleep: int = 2,
    ) -> List[Dict]:
        """
        Get insights for all medias from feed with page iteration with cursor and sleep timeout

        Parameters
        ----------
        post_type: str, optional
            Types of posts, default is "ALL"
        time_frame: str, optional
            Time frame to pull media insights, default is "TWO_YEARS"
        data_ordering: str, optional
            Ordering strategy for the data, default is "REACH_COUNT"
        count: int, optional
            Max media count for retrieving, default is 0
        sleep: int, optional
            Timeout between pages iterations, default is 2

        Returns
        -------
        List[Dict]
            List of dictionaries of response from the call
        """
        assert (
            post_type in POST_TYPES
        ), f'Unsupported post_type="{post_type}" {POST_TYPES}'
        assert (
            time_frame in TIME_FRAMES
        ), f'Unsupported time_frame="{time_frame}" {TIME_FRAMES}'
        assert (
            data_ordering in DATA_ORDERS
        ), f'Unsupported data_ordering="{data_ordering}" {DATA_ORDERS}'
        assert self.user_id, "Login required"
        medias = []
        cursor = None
        data = {
            "surface": "post_grid",
            "doc_id": 2345520318892697,
            "locale": "en_US",
            "vc_policy": "insights_policy",
            "strip_nulls": False,
            "strip_defaults": False,
        }
        query_params = {
            "IgInsightsGridMediaImage_SIZE": 480,
            "count": 200,  # TODO Try to detect max allowed value
            # "cursor": "0",
            "dataOrdering": data_ordering,
            "postType": post_type,
            "timeframe": time_frame,
            "search_base": "USER",
            "is_user": "true",
            "queryParams": {"access_token": "", "id": self.user_id},
        }
        while True:
            if cursor:
                query_params["cursor"] = cursor
            result = self.private_request(
                "ads/graphql/",
                self.with_query_params(data, query_params),
            )
            if not json_value(
                result,
                "data",
                "shadow_instagram_user",
                "business_manager",
                default=None,
            ):
                raise UserError("Account is not business account", **self.last_json)
            stats = json_value(
                result,
                "data",
                "shadow_instagram_user",
                "business_manager",
                "top_posts_unit",
                "top_posts",
            )
            cursor = stats["page_info"]["end_cursor"]
            medias.extend(stats["edges"])
            if not stats["page_info"]["has_next_page"]:
                break
            if count and len(medias) >= count:
                break
            time.sleep(sleep)
        if count:
            medias = medias[:count]
        return medias

    """
    Helpers for getting insights for media
    """

    def insights_account(self) -> Dict:
        """
        Get insights for account

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        assert self.user_id, "Login required"
        data = {
            "surface": "account",
            "doc_id": 2449243051851783,
            "locale": "en_US",
            "vc_policy": "insights_policy",
            "strip_nulls": False,
            "strip_defaults": False,
        }
        query_params = {
            "IgInsightsGridMediaImage_SIZE": 360,
            "activityTab": True,
            "audienceTab": True,
            "contentTab": True,
            "query_params": {"access_token": "", "id": self.user_id},
        }

        result = self.private_request(
            "ads/graphql/",
            self.with_query_params(data, query_params),
        )
        res = json_value(result, "data", "shadow_instagram_user", "business_manager")
        if not res:
            raise UserError("Account is not business account", **self.last_json)
        return res

    def insights_media(self, media_pk: int) -> Dict:
        """
        Get insights data for media

        Parameters
        ----------
        media_pk: int
            PK for the album you want to download

        Returns
        -------
        Dict
            A dictionary with insights data
        """
        assert self.user_id, "Login required"
        media_pk = self.media_pk(media_pk)
        data = {
            "surface": "post",
            "doc_id": 3221905377882880,
            "locale": "en_US",
            "vc_policy": "insights_policy",
            "strip_nulls": False,
            "strip_defaults": False,
        }
        query_params = {
            "query_params": {"access_token": "", "id": media_pk},
        }
        try:
            result = self.private_request(
                "ads/graphql/",
                self.with_query_params(data, query_params),
            )
            return result["data"]["instagram_post_by_igid"]
        except ClientError as e:
            raise MediaError(e.message, media_pk=media_pk, **self.last_json)



================================================
FILE: instagrapi/mixins/location.py
================================================
import base64
import json
from typing import List, Tuple

from instagrapi.exceptions import (
    ClientNotFoundError,
    LocationNotFound,
    WrongCursorError,
)
from instagrapi.extractors import extract_guide_v1, extract_location, extract_media_v1
from instagrapi.types import Guide, Location, Media

tab_keys_a1 = ("edge_location_to_top_posts", "edge_location_to_media")
tab_keys_v1 = ("ranked", "recent")


class LocationMixin:
    """
    Helper class to get location
    """

    def location_search(self, lat: float, lng: float) -> List[Location]:
        """
        Get locations using lat and long

        Parameters
        ----------
        lat: float
            Latitude you want to search for
        lng: float
            Longitude you want to search for

        Returns
        -------
        List[Location]
            List of objects of Location
        """
        params = {
            "latitude": lat,
            "longitude": lng,
            # rankToken=c544eea5-726b-4091-a916-a71a35a76474 - self.uuid?
            # fb_access_token=EAABwzLixnjYBABK2YBFkT...pKrjju4cijEGYtcbIyCSJ0j4ZD
        }
        result = self.private_request("location_search/", params=params)
        locations = []
        for venue in result["venues"]:
            if "lat" not in venue:
                venue["lat"] = lat
                venue["lng"] = lng
            locations.append(extract_location(venue))
        return locations

    def location_complete(self, location: Location) -> Location:
        """
        Smart complete of location

        Parameters
        ----------
        location: Location
            An object of location

        Returns
        -------
        Location
            An object of Location
        """
        assert location and isinstance(
            location, Location
        ), f'Location is wrong "{location}" ({type(location)})'
        if location.pk and not location.lat:
            # search lat and lng
            info = self.location_info(location.pk)
            location.lat = info.lat
            location.lng = info.lng
        if not location.external_id and location.lat:
            # search extrernal_id and external_id_source
            try:
                venue = self.location_search(location.lat, location.lng)[0]
                location.external_id = venue.external_id
                location.external_id_source = venue.external_id_source
            except IndexError:
                pass
        if not location.pk and location.external_id:
            info = self.location_info(location.external_id)
            if info.name == location.name or (
                info.lat == location.lat and info.lng == location.lng
            ):
                location.pk = location.external_id
        return location

    def location_build(self, location: Location) -> str:
        """
        Build correct location data

        Parameters
        ----------
        location: Location
            An object of location

        Returns
        -------
        str
        """
        if not location:
            return "{}"
        if not location.external_id and location.lat:
            try:
                location = self.location_search(location.lat, location.lng)[0]
            except IndexError:
                pass
        data = {
            "name": location.name,
            "address": location.address,
            "lat": location.lat,
            "lng": location.lng,
            "external_source": location.external_id_source,
            "facebook_places_id": location.external_id,
        }
        return json.dumps(data, separators=(",", ":"))

    def location_info_a1(self, location_pk: int) -> Location:
        """
        Get a location using location pk

        Parameters
        ----------
        location_pk: int
            Unique identifier for a location

        Returns
        -------
        Location
            An object of Location
        """
        try:
            data = self.public_a1_request(f"/explore/locations/{location_pk}/") or {}
            if not data.get("location"):
                raise LocationNotFound(location_pk=location_pk, **data)
            return extract_location(data["location"])
        except ClientNotFoundError:
            raise LocationNotFound(location_pk=location_pk)

    def location_info_v1(self, location_pk: int) -> Location:
        """
        Get a location using location pk

        Parameters
        ----------
        location_pk: int
            Unique identifier for a location

        Returns
        -------
        Location
            An object of Location
        """
        result = self.private_request(f"locations/{location_pk}/location_info/")
        if not result.get("name"):
            # Sorry, this page isn't available.
            raise LocationNotFound(location_pk=location_pk, **result)
        return extract_location(result)

    def location_info(self, location_pk: int) -> Location:
        """
        Get a location using location pk

        Parameters
        ----------
        location_pk: int
            Unique identifier for a location

        Returns
        -------
        Location
            An object of Location
        """
        return self.location_info_v1(location_pk)

    def location_medias_a1_chunk(
        self,
        location_pk: int,
        max_amount: int = 24,
        sleep: float = 0.5,
        tab_key: str = "",
        max_id: str = None,
    ) -> Tuple[List[Media], str]:
        """
        Get chunk of medias and end_cursor by Public Web API

        Parameters
        ----------
        location_pk: int
            Unique identifier for a location
        max_amount: int, optional
            Maximum number of media to return, default is 24
        sleep: float, optional
            Timeout between requests, default is 0.5
        tab_key: str, optional
            Tab Key, default value is ""
        end_cursor: str, optional
            End Cursor, default value is None

        Returns
        -------
        Tuple[List[Media], str]
            List of objects of Media and end_cursor
        """
        assert (
            tab_key in tab_keys_a1
        ), f'You must specify one of the options for "tab_key" {tab_keys_a1}'
        unique_set = set()
        medias = []
        end_cursor = None
        result = self.public_a1_request(
            f"/explore/locations/{location_pk}/",
            params={"max_id": end_cursor} if end_cursor else {},
        )
        data = result["location"]
        page_info = data["edge_location_to_media"]["page_info"]
        end_cursor = page_info["end_cursor"]
        edges = data[tab_key]["edges"]
        for edge in edges:
            node = edge["node"]
            # check uniq
            media_pk = node["id"]
            if media_pk in unique_set:
                continue
            unique_set.add(media_pk)
            # Enrich media: Full user, usertags and video_url
            medias.append(self.media_info_gql(media_pk))
        return medias, end_cursor

    def location_medias_a1(
        self, location_pk: int, amount: int = 24, sleep: float = 0.5, tab_key: str = ""
    ) -> List[Media]:
        """
        Get medias for a location

        Parameters
        ----------
        location_pk: int
            Unique identifier for a location
        amount: int, optional
            Maximum number of media to return, default is 24
        sleep: float, optional
            Timeout between requests, default is 0.5
        tab_key: str, optional
            Tab Key, default value is ""

        Returns
        -------
        List[Media]
            List of objects of Media
        """
        assert (
            tab_key in tab_keys_a1
        ), f'You must specify one of the options for "tab_key" {tab_keys_a1}'
        medias, _ = self.location_medias_a1_chunk(location_pk, amount, sleep, tab_key)
        if amount:
            medias = medias[:amount]
        return medias

    def location_medias_v1_chunk(
        self,
        location_pk: int,
        max_amount: int = 63,
        tab_key: str = "",
        max_id: str = None,
    ) -> Tuple[List[Media], str]:
        """
        Get chunk of medias for a location and max_id (cursor) by Private Mobile API

        Parameters
        ----------
        location_pk: int
            Unique identifier for a location
        max_amount: int, optional
            Maximum number of media to return, default is 27
        tab_key: str, optional
            Tab Key, default value is ""
        max_id: str
            Max ID, default value is None

        Returns
        -------
        Tuple[List[Media], str]
            List of objects of Media and max_id
        """
        assert (
            tab_key in tab_keys_v1
        ), f'You must specify one of the options for "tab_key" {tab_keys_v1}'
        data = {
            "_uuid": self.uuid,
            "session_id": self.client_session_id,
            "tab": tab_key,
        }
        if max_id:
            try:
                [m_id, page_id, nm_ids] = json.loads(base64.b64decode(max_id))
            except Exception:
                raise WrongCursorError()
            data["max_id"] = m_id
            data["page"] = page_id
            data["next_media_ids"] = nm_ids
        medias = []
        result = self.private_request(
            f"locations/{location_pk}/sections/",
            data=data,
        )
        next_max_id = None
        if result.get("next_page"):
            np = result.get("next_page")
            ids = result.get("next_media_ids")
            next_m_id = result.get("next_max_id")
            next_max_id = base64.b64encode(
                json.dumps([next_m_id, np, ids]).encode()
            ).decode()
        for section in result.get("sections") or []:
            layout_content = section.get("layout_content") or {}
            nodes = layout_content.get("medias") or []
            for node in nodes:
                media = extract_media_v1(node["media"])
                medias.append(media)
        return medias, next_max_id

    def location_medias_v1(
        self, location_pk: int, amount: int = 63, tab_key: str = ""
    ) -> List[Media]:
        """
        Get medias for a location by Private Mobile API

        Parameters
        ----------
        location_pk: int
            Unique identifier for a location
        amount: int, optional
            Maximum number of media to return, default is 63
        tab_key: str, optional
            Tab Key, default value is ""

        Returns
        -------
        List[Media]
            List of objects of Media
        """
        assert (
            tab_key in tab_keys_v1
        ), f'You must specify one of the options for "tab_key" {tab_keys_a1}'
        medias, _ = self.location_medias_v1_chunk(location_pk, amount, tab_key)
        if amount:
            medias = medias[:amount]
        return medias

    def location_medias_top_a1(
        self, location_pk: int, amount: int = 9, sleep: float = 0.5
    ) -> List[Media]:
        """
        Get top medias for a location

        Parameters
        ----------
        location_pk: int
            Unique identifier for a location
        amount: int, optional
            Maximum number of media to return, default is 9
        sleep: float, optional
            Timeout between requests, default is 0.5

        Returns
        -------
        List[Media]
            List of objects of Media
        """
        return self.location_medias_a1(
            location_pk, amount, sleep=sleep, tab_key="edge_location_to_top_posts"
        )

    def location_medias_top_v1(self, location_pk: int, amount: int = 21) -> List[Media]:
        """
        Get top medias for a location

        Parameters
        ----------
        location_pk: int
            Unique identifier for a location
        amount: int, optional
            Maximum number of media to return, default is 21

        Returns
        -------
        List[Media]
            List of objects of Media
        """
        return self.location_medias_v1(location_pk, amount, tab_key="ranked")

    def location_medias_top(
        self, location_pk: int, amount: int = 27
    ) -> List[Media]:
        """
        Get top medias for a location

        Parameters
        ----------
        location_pk: int
            Unique identifier for a location
        amount: int, optional
            Maximum number of media to return, default is 27

        Returns
        -------
        List[Media]
            List of objects of Media
        """
        return self.location_medias_top_v1(location_pk, amount)

    def location_medias_recent_a1(
        self, location_pk: int, amount: int = 24, sleep: float = 0.5
    ) -> List[Media]:
        """
        Get recent medias for a location

        Parameters
        ----------
        location_pk: int
            Unique identifier for a location
        amount: int, optional
            Maximum number of media to return, default is 24
        sleep: float, optional
            Timeout between requests, default is 0.5

        Returns
        -------
        List[Media]
            List of objects of Media
        """
        return self.location_medias_a1(
            location_pk, amount, sleep=sleep, tab_key="edge_location_to_media"
        )

    def location_medias_recent_v1(
        self, location_pk: int, amount: int = 63
    ) -> List[Media]:
        """
        Get recent medias for a location

        Parameters
        ----------
        location_pk: int
            Unique identifier for a location
        amount: int, optional
            Maximum number of media to return, default is 63

        Returns
        -------
        List[Media]
            List of objects of Media
        """
        return self.location_medias_v1(location_pk, amount, tab_key="recent")

    def location_medias_recent(
        self, location_pk: int, amount: int = 63
    ) -> List[Media]:
        """
        Get recent medias for a location

        Parameters
        ----------
        location_pk: int
            Unique identifier for a location
        amount: int, optional
            Maximum number of media to return, default is 63

        Returns
        -------
        List[Media]
            List of objects of Media
        """
        return self.location_medias_recent_v1(location_pk, amount)

    def location_guides_v1(self, location_pk: int) -> List[Guide]:
        """
        Get guides by location_pk

        Parameters
        ----------
        location_pk: int

        Returns
        -------
        List[Guide]
            List of objects of Guide
        """
        location_pk = int(location_pk)
        result = self.private_request(f"guides/location/{location_pk}/")
        return [extract_guide_v1(item) for item in (result.get("guides") or [])]



================================================
FILE: instagrapi/mixins/media.py
================================================
import json
import random
import time
from copy import deepcopy
from datetime import datetime
from typing import Dict, List, Tuple
from urllib.parse import urlparse

from instagrapi.exceptions import (
    ClientError,
    ClientLoginRequired,
    ClientNotFoundError,
    MediaNotFound,
    PrivateError,
)
from instagrapi.extractors import (
    extract_location,
    extract_media_gql,
    extract_media_oembed,
    extract_media_v1,
    extract_user_short,
)
from instagrapi.types import Location, Media, UserShort, Usertag
from instagrapi.utils import InstagramIdCodec, json_value


class MediaMixin:
    """
    Helpers for media
    """

    _medias_cache = {}  # pk -> object

    def media_id(self, media_pk: str) -> str:
        """
        Get full media id

        Parameters
        ----------
        media_pk: str
            Unique Media ID

        Returns
        -------
        str
            Full media id

        Example
        -------
        2277033926878261772 -> 2277033926878261772_1903424587
        """
        media_id = str(media_pk)
        if "_" not in media_id:
            assert media_id.isdigit(), (
                "media_id must been contain digits, now %s" % media_id
            )
            user = self.media_user(media_id)
            media_id = "%s_%s" % (media_id, user.pk)
        return media_id

    @staticmethod
    def media_pk(media_id: str) -> str:
        """
        Get short media id

        Parameters
        ----------
        media_id: str
            Unique Media ID

        Returns
        -------
        str
            media id

        Example
        -------
        2277033926878261772_1903424587 -> 2277033926878261772
        """
        media_pk = str(media_id)
        if "_" in media_pk:
            media_pk, _ = media_id.split("_")
        return str(media_pk)

    def media_code_from_pk(self, media_pk: str) -> str:
        """
        Get Code from Media PK

        Parameters
        ----------
        media_pk: str
            Media PK

        Returns
        -------
        str
            Code (aka shortcode)

        Examples
        --------
        2110901750722920960 -> B1LbfVPlwIA
        2278584739065882267 -> B-fKL9qpeab
        """
        return InstagramIdCodec.encode(media_pk)

    def media_pk_from_code(self, code: str) -> str:
        """
        Get Media PK from Code

        Parameters
        ----------
        code: str
            Code

        Returns
        -------
        int
            Full media id

        Examples
        --------
        B1LbfVPlwIA -> 2110901750722920960
        B-fKL9qpeab -> 2278584739065882267
        CCQQsCXjOaBfS3I2PpqsNkxElV9DXj61vzo5xs0 -> 2346448800803776129
        """
        return str(InstagramIdCodec.decode(code[:11]))

    def media_pk_from_url(self, url: str) -> str:
        """
        Get Media PK from URL

        Parameters
        ----------
        url: str
            URL of the media

        Returns
        -------
        int
            Media PK

        Examples
        --------
        https://instagram.com/p/B1LbfVPlwIA/ -> 2110901750722920960
        https://www.instagram.com/p/B-fKL9qpeab/?igshid=1xm76zkq7o1im -> 2278584739065882267
        """
        path = urlparse(url).path
        parts = [p for p in path.split("/") if p]
        return self.media_pk_from_code(parts.pop())

    def media_info_a1(self, media_pk: str, max_id: str = None) -> Media:
        """
        Get Media from PK by Public Web API

        Parameters
        ----------
        media_pk: str
            Unique identifier of the media
        max_id: str, optional
            Max ID, default value is None

        Returns
        -------
        Media
            An object of Media type
        """
        media_pk = self.media_pk(media_pk)
        shortcode = self.media_code_from_pk(media_pk)
        """Use Client.media_info
        """
        params = {"max_id": max_id} if max_id else None
        data = self.public_a1_request(
            "/p/{shortcode!s}/".format(**{"shortcode": shortcode}), params=params
        )
        if not data.get("shortcode_media"):
            raise MediaNotFound(media_pk=media_pk, **data)
        return extract_media_gql(data["shortcode_media"])

    def media_info_gql(self, media_pk: str) -> Media:
        """
        Get Media from PK by Public Graphql API

        Parameters
        ----------
        media_pk: str
            Unique identifier of the media

        Returns
        -------
        Media
            An object of Media type
        """
        media_pk = self.media_pk(media_pk)
        shortcode = self.media_code_from_pk(media_pk)
        """Use Client.media_info
        """
        variables = {
            "shortcode": shortcode,
            "child_comment_count": 3,
            "fetch_comment_count": 40,
            "parent_comment_count": 24,
            "has_threaded_comments": False,
        }
        data = self.public_graphql_request(
            variables, query_hash="477b65a610463740ccdb83135b2014db"
        )
        if not data.get("shortcode_media"):
            raise MediaNotFound(media_pk=media_pk, **data)
        if data["shortcode_media"]["location"] and self.authorization:
            data["shortcode_media"]["location"] = self.location_complete(
                extract_location(data["shortcode_media"]["location"])
            ).dict()
        return extract_media_gql(data["shortcode_media"])

    def media_info_v1(self, media_pk: str) -> Media:
        """
        Get Media from PK by Private Mobile API

        Parameters
        ----------
        media_pk: str
            Unique identifier of the media

        Returns
        -------
        Media
            An object of Media type
        """
        try:
            result = self.private_request(f"media/{media_pk}/info/")
        except ClientNotFoundError as e:
            raise MediaNotFound(e, media_pk=media_pk, **self.last_json)
        except ClientError as e:
            if "Media not found" in str(e):
                raise MediaNotFound(e, media_pk=media_pk, **self.last_json)
            raise e
        return extract_media_v1(result["items"].pop())

    def media_info(self, media_pk: str, use_cache: bool = True) -> Media:
        """
        Get Media Information from PK

        Parameters
        ----------
        media_pk: str
            Unique identifier of the media
        use_cache: bool, optional
            Whether or not to use information from cache, default value is True

        Returns
        -------
        Media
            An object of Media type
        """
        media_pk = self.media_pk(media_pk)
        if not use_cache or media_pk not in self._medias_cache:
            try:
                try:
                    media = self.media_info_gql(media_pk)
                except ClientLoginRequired as e:
                    if not self.inject_sessionid_to_public():
                        raise e
                    media = self.media_info_gql(media_pk)  # retry
            except Exception as e:
                if not isinstance(e, ClientError):
                    self.logger.exception(e)  # Register unknown error
                # Restricted Video: This video is not available in your country.
                # Or private account
                media = self.media_info_v1(media_pk)
            self._medias_cache[media_pk] = media
        return deepcopy(
            self._medias_cache[media_pk]
        )  # return copy of cache (dict changes protection)

    def media_delete(self, media_id: str) -> bool:
        """
        Delete media by Media ID

        Parameters
        ----------
        media_id: str
            Unique identifier of the media

        Returns
        -------
        bool
            A boolean value
        """
        assert self.user_id, "Login required"
        media_id = self.media_id(media_id)
        result = self.private_request(
            f"media/{media_id}/delete/", self.with_default_data({"media_id": media_id})
        )
        self._medias_cache.pop(self.media_pk(media_id), None)
        return result.get("did_delete")

    def media_edit(
        self,
        media_id: str,
        caption: str,
        title: str = "",
        usertags: List[Usertag] = [],
        location: Location = None,
    ) -> Dict:
        """
        Edit caption for media

        Parameters
        ----------
        media_id: str
            Unique identifier of the media
        caption: str
            Media caption
        title: str
            Title of the media
        usertags: List[Usertag], optional
            List of users to be tagged on this upload, default is empty list.
        location: Location, optional
            Location tag for this upload, default is None

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        assert self.user_id, "Login required"
        media_id = self.media_id(media_id)
        media = self.media_info(media_id)  # from cache
        usertags = [
            {"user_id": tag.user.pk, "position": [tag.x, tag.y]} for tag in usertags
        ]
        data = {
            "caption_text": caption,
            "container_module": "edit_media_info",
            "feed_position": "0",
            "location": self.location_build(location),
            "usertags": json.dumps({"in": usertags}),
            "is_carousel_bumped_post": "false",
        }
        if media.product_type == "igtv":
            if not title:
                try:
                    title, caption = caption.split("\n", 1)
                except ValueError:
                    title = caption[:75]
            data = {
                "caption_text": caption,
                "title": title,
                "igtv_ads_toggled_on": "0",
            }
        self._medias_cache.pop(self.media_pk(media_id), None)  # clean cache
        result = self.private_request(
            f"media/{media_id}/edit_media/",
            self.with_default_data(data),
        )
        return result

    def media_user(self, media_pk: str) -> UserShort:
        """
        Get author of the media

        Parameters
        ----------
        media_pk: str
            Unique identifier of the media

        Returns
        -------
        UserShort
            An object of UserShort
        """
        return self.media_info_v1(media_pk).user

    def media_oembed(self, url: str) -> Dict:
        """
        Return info about media and user from post URL

        Parameters
        ----------
        url: str
            URL for a media

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        return extract_media_oembed(self.private_request(f"oembed?url={url}"))

    def media_like(self, media_id: str, revert: bool = False) -> bool:
        """
        Like a media

        Parameters
        ----------
        media_id: str
            Unique identifier of a Media
        revert: bool, optional
            If liked, whether or not to unlike. Default is False

        Returns
        -------
        bool
            A boolean value
        """
        assert self.user_id, "Login required"
        media_id = self.media_pk(media_id)
        data = {
            "inventory_source": "media_or_ad",
            "media_id": media_id,
            "radio_type": "wifi-none",
            "is_carousel_bumped_post": "false",
            "container_module": "feed_timeline",
            "feed_position": str(random.randint(0, 6)),
        }
        name = "unlike" if revert else "like"
        result = self.private_request(
            f"media/{media_id}/{name}/", self.with_action_data(data)
        )
        return result["status"] == "ok"

    def media_unlike(self, media_id: str) -> bool:
        """
        Unlike a media

        Parameters
        ----------
        media_id: str
            Unique identifier of a Media

        Returns
        -------
        bool
            A boolean value
        """
        return self.media_like(media_id, revert=True)

    def user_medias_paginated_gql(
        self, user_id: str, amount: int = 0, sleep: int = 2, end_cursor=None
    ) -> Tuple[List[Media], str]:
        """
        Get a page of a user's media by Public Graphql API

        Parameters
        ----------
        user_id: str
        amount: int, optional
            Maximum number of media to return, default is 0 (all medias)
        sleep: int, optional
            Timeout between pages iterations, default is 2
        end_cursor: str, optional
            Cursor value to start at, obtained from previous call to this method
        Returns
        -------
        Tuple[List[Media], str]
            A tuple containing a list of medias and the next end_cursor value
        """
        amount = int(amount)
        user_id = int(user_id)
        medias = []
        variables = {
            "id": user_id,
            "first": 50 if not amount or amount > 50 else amount,
            # These are Instagram restrictions, you can only specify <= 50
        }
        variables["after"] = end_cursor
        data = self.public_graphql_request(
            variables, query_hash="e7e2f4da4b02303f74f0841279e52d76"
        )
        page_info = json_value(
            data, "user", "edge_owner_to_timeline_media", "page_info", default={}
        )
        edges = json_value(
            data, "user", "edge_owner_to_timeline_media", "edges", default=[]
        )
        for edge in edges:
            medias.append(edge["node"])
        end_cursor = page_info.get("end_cursor")
        if amount:
            medias = medias[:amount]
        return ([extract_media_gql(media) for media in medias], end_cursor)

    def user_medias_gql(
        self, user_id: str, amount: int = 0, sleep: int = 0
    ) -> List[Media]:
        """
        Get a user's media by Public Graphql API

        Parameters
        ----------
        user_id: str
        amount: int, optional
            Maximum number of media to return, default is 0 (all medias)
        sleep: int, optional
            Timeout between pages iterations, default is a random number between 1 and 3.

        Returns
        -------
        List[Media]
            A list of objects of Media
        """
        amount = int(amount)
        user_id = int(user_id)
        sleep = int(sleep)
        medias = []
        end_cursor = None
        variables = {
            "id": user_id,
            "first": 50 if not amount or amount > 50 else amount,
            # These are Instagram restrictions, you can only specify <= 50
        }
        while True:
            self.logger.info(f"user_medias_gql: {amount}, {end_cursor}")
            if end_cursor:
                variables["after"] = end_cursor

            if not sleep:
                sleep = random.randint(1, 3)

            medias_page, end_cursor = self.user_medias_paginated_gql(
                user_id, amount, sleep, end_cursor=end_cursor
            )
            medias.extend(medias_page)
            if not end_cursor or len(medias_page) == 0:
                break
            if amount and len(medias) >= amount:
                break
            time.sleep(sleep)
        if amount:
            medias = medias[:amount]
        return medias

    def user_videos_paginated_v1(
        self, user_id: str, amount: int = 50, end_cursor: str = ""
    ) -> Tuple[List[Media], str]:
        """
        Get a page of user's video by Private Mobile API

        Parameters
        ----------
        user_id: str
        amount: int, optional
            Maximum number of media to return, default is 0 (all medias)
        end_cursor: str, optional
            Cursor value to start at, obtained from previous call to this method

        Returns
        -------
        Tuple[List[Media], str]
            A tuple containing a list of medias and the next end_cursor value
        """
        items = []
        amount = int(amount)
        user_id = int(user_id)
        medias = []
        next_max_id = end_cursor
        try:
            resp = self.private_request(
                "igtv/channel/", params={"id": f"uservideo_{user_id}", "count": 50}
            )
            items = resp["items"]
        except PrivateError as e:
            raise e
        except Exception as e:
            self.logger.exception(e)
            return [], None
        medias.extend(items)
        next_max_id = self.last_json.get("next_max_id", "")
        if amount:
            medias = medias[:amount]
        return ([extract_media_v1(media) for media in medias], next_max_id)

    def user_videos_v1(self, user_id: str, amount: int = 0) -> List[Media]:
        """
        Get a user's video by Private Mobile API

        Parameters
        ----------
        user_id: str
        amount: int, optional
            Maximum number of media to return, default is 0 (all medias)

        Returns
        -------
        List[Media]
            A list of objects of Media
        """
        amount = int(amount)
        user_id = int(user_id)
        medias = []
        next_max_id = ""
        while True:
            try:
                medias_page, next_max_id = self.user_videos_paginated_v1(
                    user_id, amount, end_cursor=next_max_id
                )
            except PrivateError as e:
                raise e
            except Exception as e:
                self.logger.exception(e)
                break
            medias.extend(medias_page)
            if not next_max_id:
                break
            if amount and len(medias) >= amount:
                break
        if amount:
            medias = medias[:amount]
        return medias

    def user_medias_paginated_v1(
        self, user_id: str, amount: int = 33, end_cursor: str = ""
    ) -> Tuple[List[Media], str]:
        """
        Get a page of user's media by Private Mobile API

        Parameters
        ----------
        user_id: str
        amount: int, optional
            Maximum number of media to return, default is 0 (all medias)
        end_cursor: str, optional
            Cursor value to start at, obtained from previous call to this method

        Returns
        -------
        Tuple[List[Media], str]
            A tuple containing a list of medias and the next end_cursor value
        """
        amount = int(amount)
        user_id = int(user_id)
        medias = []
        next_max_id = end_cursor
        min_timestamp = None
        try:
            items = self.private_request(
                f"feed/user/{user_id}/",
                params={
                    "max_id": next_max_id,
                    "count": amount,
                    "min_timestamp": min_timestamp,
                    "rank_token": self.rank_token,
                    "ranked_content": "true",
                },
            )["items"]
        except PrivateError as e:
            raise e
        except Exception as e:
            self.logger.exception(e)
            return [], None
        medias.extend(items)
        next_max_id = self.last_json.get("next_max_id", "")
        if amount:
            medias = medias[:amount]
        return ([extract_media_v1(media) for media in medias], next_max_id)

    def user_medias_v1(self, user_id: str, amount: int = 0) -> List[Media]:
        """
        Get a user's media by Private Mobile API

        Parameters
        ----------
        user_id: str
        amount: int, optional
            Maximum number of media to return, default is 0 (all medias)

        Returns
        -------
        List[Media]
            A list of objects of Media
        """
        amount = int(amount)
        user_id = int(user_id)
        medias = []
        next_max_id = ""
        while True:
            try:
                medias_page, next_max_id = self.user_medias_paginated_v1(
                    user_id, amount, end_cursor=next_max_id
                )
            except PrivateError as e:
                raise e
            except Exception as e:
                self.logger.exception(e)
                break
            medias.extend(medias_page)
            if not next_max_id:
                break
            if amount and len(medias) >= amount:
                break
        if amount:
            medias = medias[:amount]
        return medias

    def user_medias_paginated(
        self, user_id: str, amount: int = 0, end_cursor: str = ""
    ) -> Tuple[List[Media], str]:
        """
        Get a page of user's media

        Parameters
        ----------
        user_id: str
        amount: int, optional
            Maximum number of media to return, default is 0 (all medias)
        end_cursor: str, optional
            Cursor value to start at, obtained from previous call to this method

        Returns
        -------
        Tuple[List[Media], str]
            A tuple containing a list of medias and the next end_cursor value
        """

        class EndCursorIsV1(Exception):
            pass

        try:
            if end_cursor and "_" in end_cursor:
                # end_cursor is a v1 next_max_id, so we need to use v1 API
                raise EndCursorIsV1
            try:
                medias, end_cursor = self.user_medias_paginated_gql(
                    user_id, amount, end_cursor=end_cursor
                )
            except ClientLoginRequired as e:
                if not self.inject_sessionid_to_public():
                    raise e
                medias, end_cursor = self.user_medias_paginated_gql(
                    user_id, amount, end_cursor=end_cursor
                )
        except PrivateError as e:
            raise e
        except Exception as e:
            if isinstance(e, EndCursorIsV1):
                pass
            elif not isinstance(e, ClientError):
                self.logger.exception(e)
            medias, end_cursor = self.user_medias_paginated_v1(
                user_id, amount, end_cursor=end_cursor
            )
        return medias, end_cursor

    def user_pinned_medias(self, user_id) -> List[Media]:
        """
        Get a pinned medias

        Parameters
        ----------
        user_id: str

        Returns
        -------
        List[Media]
            A list of objects of Media
        """
        default_nav = self.base_headers["X-IG-Nav-Chain"]
        self.base_headers[
            "X-IG-Nav-Chain"
        ] = "MainFeedFragment:feed_timeline:12:main_home::,UserDetailFragment:profile:13:button::"
        medias = self.private_request(
            f"feed/user/{user_id}/",
            params={
                "exclude_comment": "true",
                "only_fetch_first_carousel_media": "false",
            },
        )
        pinned_medias = []
        for media in medias["items"]:
            if media.get("timeline_pinned_user_ids") is not None:
                pinned_medias.append(extract_media_v1(media))
        self.base_headers["X-IG-Nav-Chain"] = default_nav
        return pinned_medias

    def user_medias(self, user_id: str, amount: int = 0, sleep: int = 0) -> List[Media]:
        """
        Get a user's media

        Parameters
        ----------
        user_id: str
        amount: int, optional
            Maximum number of media to return, default is 0 (all medias)
        sleep: int, optional
            Timeout between page iterations

        Returns
        -------
        List[Media]
            A list of objects of Media
        """
        amount = int(amount)
        user_id = int(user_id)
        sleep = int(sleep)
        try:
            try:
                medias = self.user_medias_gql(user_id, amount, sleep)
            except ClientLoginRequired as e:
                if not self.inject_sessionid_to_public():
                    raise e
                medias = self.user_medias_gql(user_id, amount, sleep)  # retry
        except PrivateError as e:
            raise e
        except Exception as e:
            if not isinstance(e, ClientError):
                self.logger.exception(e)
            # User may been private, attempt via Private API
            # (You can check is_private, but there may be other reasons,
            #  it is better to try through a Private API)
            medias = self.user_medias_v1(user_id, amount)
        return medias

    def user_clips_paginated_v1(
        self, user_id: str, amount: int = 50, end_cursor: str = ""
    ) -> Tuple[List[Media], str]:
        """
        Get a page of user's clip (reels) by Private Mobile API

        Parameters
        ----------
        user_id: str
        amount: int, optional
            Maximum number of media to return, default is 0 (all medias)
        end_cursor: str, optional
            Cursor value to start at, obtained from previous call to this method

        Returns
        -------
        Tuple[List[Media], str]
            A tuple containing a list of medias and the next end_cursor value
        """
        amount = int(amount)
        user_id = int(user_id)
        medias = []
        next_max_id = end_cursor
        try:
            items = self.private_request(
                "clips/user/",
                data={
                    "target_user_id": user_id,
                    "max_id": next_max_id,
                    "page_size": amount,  # default from app: 12
                    "include_feed_video": "true",
                },
            )["items"]
        except PrivateError as e:
            raise e
        except Exception as e:
            self.logger.exception(e)
            return [], None
        medias.extend(items)
        next_max_id = json_value(self.last_json, "paging_info", "max_id", default="")
        if amount:
            medias = medias[:amount]
        return ([extract_media_v1(media["media"]) for media in medias], next_max_id)

    def user_clips_v1(self, user_id: str, amount: int = 0) -> List[Media]:
        """
        Get a user's clip (reels) by Private Mobile API

        Parameters
        ----------
        user_id: str
        amount: int, optional
            Maximum number of media to return, default is 0 (all medias)

        Returns
        -------
        List[Media]
            A list of objects of Media
        """
        amount = int(amount)
        user_id = int(user_id)
        medias = []
        next_max_id = ""
        while True:
            try:
                medias_page, next_max_id = self.user_clips_paginated_v1(
                    user_id, end_cursor=next_max_id
                )
            except PrivateError as e:
                raise e
            except Exception as e:
                self.logger.exception(e)
                break
            medias.extend(medias_page)
            if not next_max_id:
                break
            if amount and len(medias) >= amount:
                break
        if amount:
            medias = medias[:amount]
        return medias

    def user_clips(self, user_id: str, amount: int = 0) -> List[Media]:
        """
        Get a user's clip (reels)

        Parameters
        ----------
        user_id: str
        amount: int, optional
            Maximum number of media to return, default is 0 (all medias)

        Returns
        -------
        List[Media]
            A list of objects of Media
        """
        amount = int(amount)
        user_id = int(user_id)
        return self.user_clips_v1(user_id, amount)

    def media_seen(self, media_ids: List[str], skipped_media_ids: List[str] = []):
        """
        Mark a media as seen

        Parameters
        ----------
        media_id: str

        Returns
        -------
        bool
            A boolean value
        """

        def gen(media_ids):
            result = {}
            for media_id in media_ids:
                media_pk, user_id = self.media_id(media_id).split("_")
                end = int(datetime.now().timestamp())
                begin = end - random.randint(100, 3000)
                result[f"{media_pk}_{user_id}_{user_id}"] = [f"{begin}_{end}"]
            return result

        data = {
            "container_module": "feed_timeline",
            "live_vods_skipped": {},
            "nuxes_skipped": {},
            "nuxes": {},
            "reels": gen(media_ids),
            "live_vods": {},
            "reel_media_skipped": gen(skipped_media_ids),
        }
        result = self.private_request(
            "/v2/media/seen/?reel=1&live_vod=0", self.with_default_data(data)
        )
        return result["status"] == "ok"

    def media_likers(self, media_id: str) -> List[UserShort]:
        """
        Get user's likers

        Parameters
        ----------
        media_pk: str

        Returns
        -------
        List[UserShort]
            List of objects of User type
        """
        media_id = self.media_id(media_id)
        result = self.private_request(f"media/{media_id}/likers/")
        return [extract_user_short(u) for u in result["users"]]

    def media_archive(self, media_id: str, revert: bool = False) -> bool:
        """
        Archive a media

        Parameters
        ----------
        media_id: str
            Unique identifier of a Media
        revert: bool, optional
            Flag for archive or unarchive. Default is False

        Returns
        -------
        bool
            A boolean value
        """
        media_id = self.media_id(media_id)
        name = "undo_only_me" if revert else "only_me"
        result = self.private_request(
            f"media/{media_id}/{name}/", self.with_action_data({"media_id": media_id})
        )
        return result["status"] == "ok"

    def media_unarchive(self, media_id: str) -> bool:
        """
        Unarchive a media

        Parameters
        ----------
        media_id: str
            Unique identifier of a Media

        Returns
        -------
        bool
            A boolean value
        """
        return self.media_archive(media_id, revert=True)

    def usertag_medias_gql(
        self, user_id: str, amount: int = 0, sleep: int = 2
    ) -> List[Media]:
        """
        Get medias where a user is tagged (by Public GraphQL API)

        Parameters
        ----------
        user_id: str
        amount: int, optional
            Maximum number of media to return, default is 0 (all medias)
        sleep: int, optional
            Timeout between pages iterations, default is 2

        Returns
        -------
        List[Media]
            A list of objects of Media
        """
        amount = int(amount)
        user_id = int(user_id)
        medias = []
        end_cursor = None
        variables = {
            "id": user_id,
            "first": 50 if not amount or amount > 50 else amount,
            # These are Instagram restrictions, you can only specify <= 50
        }
        while True:
            if end_cursor:
                variables["after"] = end_cursor
            data = self.public_graphql_request(
                variables, query_hash="be13233562af2d229b008d2976b998b5"
            )
            page_info = json_value(
                data, "user", "edge_user_to_photos_of_you", "page_info", default={}
            )
            edges = json_value(
                data, "user", "edge_user_to_photos_of_you", "edges", default=[]
            )
            for edge in edges:
                medias.append(edge["node"])
            end_cursor = page_info.get("end_cursor")
            if not page_info.get("has_next_page") or not end_cursor or len(edges) == 0:
                break
            if amount and len(medias) >= amount:
                break
            time.sleep(sleep)
        if amount:
            medias = medias[:amount]
        return [extract_media_gql(media) for media in medias]

    def usertag_medias_v1(self, user_id: str, amount: int = 0) -> List[Media]:
        """
        Get medias where a user is tagged (by Private Mobile API)

        Parameters
        ----------
        user_id: str
        amount: int, optional
            Maximum number of media to return, default is 0 (all medias)

        Returns
        -------
        List[Media]
            A list of objects of Media
        """
        amount = int(amount)
        user_id = int(user_id)
        medias = []
        next_max_id = ""
        while True:
            try:
                items = self.private_request(
                    f"usertags/{user_id}/feed/", params={"max_id": next_max_id}
                )["items"]
            except PrivateError as e:
                raise e
            except Exception as e:
                self.logger.exception(e)
                break
            medias.extend(items)
            if not self.last_json.get("more_available"):
                break
            if amount and len(medias) >= amount:
                break
            next_max_id = self.last_json.get("next_max_id", "")
        if amount:
            medias = medias[:amount]
        return [extract_media_v1(media) for media in medias]

    def usertag_medias(self, user_id: str, amount: int = 0) -> List[Media]:
        """
        Get medias where a user is tagged

        Parameters
        ----------
        user_id: str
        amount: int, optional
            Maximum number of media to return, default is 0 (all medias)

        Returns
        -------
        List[Media]
            A list of objects of Media
        """
        amount = int(amount)
        user_id = int(user_id)
        try:
            medias = self.usertag_medias_gql(user_id, amount)
        except ClientError:
            medias = self.usertag_medias_v1(user_id, amount)
        return medias

    def media_pin(self, media_pk: str, revert: bool = False):
        """
        Pin post to user profile

        Parameters
        ----------
        media_pk: str
        revert: bool, optional
            Unpin when True

        Returns
        -------
        bool
        A boolean value
        """
        data = self.with_action_data({"post_id": media_pk, "_uuid": self.uuid})
        name = "unpin" if revert else "pin"

        result = self.private_request(f"users/{name}_timeline_media/", data)
        return result["status"] == "ok"

    def media_unpin(self, media_pk):
        """
        Pin post to user profile

        Parameters
        ----------
        media_pk: str

        Returns
        -------
        bool
        A boolean value
        """
        return self.media_pin(media_pk, True)

    def media_create_livestream(self, title="Instagram Live"):
        """
        Create a new live broadcast.

        Parameters
        ----------
        title : str
            The title of the live broadcast.

        Returns
        -------
        dict
            Information about the streaming server and the stream key.
        """
        data = {
            "_uuid": self.uuid,
            "_uid": self.user_id,
            "preview_height": 1920,
            "preview_width": 1080,
            "broadcast_message": title,
            "broadcast_type": "RTMP",
            "internal_only": 0,
            "_csrftoken": self.token,
        }
        try:
            response = self.private_request("live/create/", data=data)
            broadcast_id = response["broadcast_id"]
            upload_url = response["upload_url"].split(str(broadcast_id))
            if len(upload_url) >= 2:
                stream_server = upload_url[0]
                stream_key = f"{broadcast_id}{upload_url[1]}"
                return {
                    "broadcast_id": broadcast_id,
                    "stream_server": stream_server,
                    "stream_key": stream_key,
                }
        except Exception as e:
            self.logger.error(f"Error creating live broadcast: {e}")
            raise

    def media_start_livestream(self, broadcast_id):
        """
        Start a live broadcast.

        Parameters
        ----------
        broadcast_id : str
            The ID of the live broadcast.

        Returns
        -------
        bool
            True if the broadcast started successfully, False otherwise.
        """
        data = {
            "_uuid": self.uuid,
            "_uid": self.user_id,
            "should_send_notifications": 1,
            "_csrftoken": self.token,
        }
        try:
            response = self.private_request(f"live/{broadcast_id}/start/", data=data)
            return response.get("status") == "ok"
        except Exception as e:
            self.logger.error(f"Error starting live broadcast: {e}")
            return False

    def media_end_livestream(self, broadcast_id):
        """
        End a live broadcast.

        Parameters
        ----------
        broadcast_id : str
            The ID of the live broadcast.

        Returns
        -------
        bool
            True if the broadcast ended successfully, False otherwise.
        """
        data = {
            "_uuid": self.uuid,
            "_uid": self.user_id,
            "_csrftoken": self.token,
        }
        try:
            response = self.private_request(f"live/{broadcast_id}/end_broadcast/", data=data)
            return response.get("status") == "ok"
        except Exception as e:
            self.logger.error(f"Error ending live broadcast: {e}")
            return False

    def media_get_livestream_info(self, broadcast_id):
        """
        Retrieve information about the live broadcast.

        Parameters
        ----------
        broadcast_id : str
            The ID of the live broadcast.

        Returns
        -------
        dict
            Information about the live broadcast.
        """
        try:
            response = self.private_request(f"live/{broadcast_id}/info/")
            return response
        except Exception as e:
            self.logger.error(f"Error retrieving live info: {e}")
            raise

    def media_get_livestream_comments(self, broadcast_id):
        """
        Retrieve comments from the live broadcast.

        Parameters
        ----------
        broadcast_id : str
            The ID of the live broadcast.

        Returns
        -------
        list
            A list of comments.
        """
        try:
            response = self.private_request(f"live/{broadcast_id}/get_comment/")
            if "comments" in response:
                return [{"username": c["user"]["username"], "text": c["text"]} for c in response["comments"]]
            return []
        except Exception as e:
            self.logger.error(f"Error retrieving live comments: {e}")
            raise

    def media_get_livestream_viewers(self, broadcast_id):
        """
        Retrieve the list of viewers of the live broadcast.

        Parameters
        ----------
        broadcast_id : str
            The ID of the live broadcast.

        Returns
        -------
        list
            A list of viewers.
        """
        try:
            response = self.private_request(f"live/{broadcast_id}/get_viewer_list/")
            return [{"username": user["username"], "pk": user["pk"]} for user in response.get("users", [])]
        except Exception as e:
            self.logger.error(f"Error retrieving live viewers: {e}")
            raise



================================================
FILE: instagrapi/mixins/multiple_accounts.py
================================================
class MultipleAccountsMixin:
    """
    Helpers for multiple accounts.
    """

    def featured_accounts_v1(self, target_user_id: str) -> dict:
        target_user_id = str(target_user_id)
        return self.private_request(
            "multiple_accounts/get_featured_accounts/",
            params={"target_user_id": target_user_id},
        )

    def get_account_family_v1(self) -> dict:
        return self.private_request("multiple_accounts/get_account_family/")



================================================
FILE: instagrapi/mixins/note.py
================================================
from typing import List

from instagrapi.types import Note


class NoteMixin:
    def get_notes(self) -> List[Note]:
        """
        Retrieves Notes in Direct

        Returns
        -------
        List[Notes]
            List of all the Notes in Direct
        """
        result = self.private_request("notes/get_notes/")
        assert result.get("status", "") == "ok", "Failed to retrieve Notes in Direct"

        notes = []
        for item in result.get("items", []):
            notes.append(Note(**item))
        return notes

    def last_seen_update_note(self) -> bool:
        """
        Updating your Notes last seen

        Returns
        -------
        bool
            A boolean value
        """
        result = self.private_request(
            "notes/update_notes_last_seen_timestamp/", data={"_uuid": self.uuid}
        )
        return result.get("status", "") == "ok"

    def delete_note(self, note_id: int) -> bool:
        """
        Delete one of your personal notes

        Parameters
        ----------
        note_id: int
            ID of the Note to delete

        Returns
        -------
        bool
            A boolean value
        """
        result = self.private_request(
            "notes/delete_note/", data={"id": note_id, "_uuid": self.uuid}
        )
        return result.get("status", "") == "ok"

    def create_note(self, text: str, audience: int = 0) -> Note:
        """
        Create personal Note

        Parameters
        ----------
        text: str
            Content of the Note
        audience: optional
            Audience to see Note, deafult 0 (Followers you follow back).
            Best Friends - 1

        Returns
        -------
        Note
            Created Note

        """
        assert self.user_id, "Login required"
        assert audience in (
            0,
            1,
        ), f"Invalid audience parameter={audience} (must be 0 or 1)"

        data = {"note_style": 0, "text": text, "_uuid": self.uuid, "audience": audience}
        result = self.private_request("notes/create_note", data=data)

        assert result.pop("status", "") == "ok", "Failed to create new Note"
        return Note(**result)



================================================
FILE: instagrapi/mixins/notification.py
================================================
MUTE_ALL_ITEMS = ("cancel", "15_minutes", "1_hour", "2_hour", "4_hour", "8_hour")
SETTING_VALUE_ITEMS = ("off", "following_only", "everyone")

try:
    from typing import Literal

    MUTE_ALL = Literal[MUTE_ALL_ITEMS]
    SETTING_VALUE = Literal[SETTING_VALUE_ITEMS]
except ImportError:
    # python <= 3.8
    MUTE_ALL = str
    SETTING_VALUE = str


class NotificationMixin:
    """
    Helpers for notification settings
    """

    def notification_settings(self, content_type: str, setting_value: str) -> bool:
        data = {
            "content_type": content_type,
            "setting_value": setting_value,
            "_uid": str(self.user_id),
            "_uuid": self.uuid,
        }
        result = self.private_request(
            "notifications/change_notification_settings/", data=data
        )
        return result.get("status") == "ok"

    def notification_disable(self) -> bool:
        """
        Disable All Notification

        Returns
        -------
        bool
        """
        notifications = (
            self.notification_likes,
            self.notification_like_and_comment_on_photo_user_tagged,
            self.notification_user_tagged,
            self.notification_comments,
            self.notification_comment_likes,
            self.notification_first_post,
            self.notification_new_follower,
            self.notification_follow_request_accepted,
            self.notification_connection,
            self.notification_tagged_in_bio,
            self.notification_pending_direct_share,
            self.notification_direct_share_activity,
            self.notification_direct_group_requests,
            self.notification_video_call,
            self.notification_rooms,
            self.notification_live_broadcast,
            self.notification_felix_upload_result,
            self.notification_view_count,
            self.notification_fundraiser_creator,
            self.notification_fundraiser_supporter,
            self.notification_reminders,
            self.notification_announcements,
            self.notification_report_updated,
            self.notification_login,
        )
        return all(func("off") for func in notifications)

    def notification_mute_all(self, setting_value: MUTE_ALL = "8_hour") -> bool:
        """
        Manage Mute All Notification Settings

        Parameters
        ----------
        setting_value: MUTE_ALL
            Value of settings, default "8_hour"

        Returns
        -------
        bool
        """
        assert (
            setting_value in MUTE_ALL_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {MUTE_ALL_ITEMS}'
        return self.notification_settings("mute_all", setting_value)

    def notification_likes(self, setting_value: SETTING_VALUE = "off") -> bool:
        """
        Manage Likes Notification Settings

        Parameters
        ----------
        setting_value: SETTING_VALUE
            Value of settings, default "off"

        Returns
        -------
        bool
        """
        assert (
            setting_value in SETTING_VALUE_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {SETTING_VALUE_ITEMS}'
        return self.notification_settings("likes", setting_value)

    def notification_like_and_comment_on_photo_user_tagged(
        self, setting_value: SETTING_VALUE = "off"
    ) -> bool:
        """
        Manage Like And Comment On Photo User Tagged Settings

        Parameters
        ----------
        setting_value: SETTING_VALUE
            Value of settings, default "off"

        Returns
        -------
        bool
        """
        assert (
            setting_value in SETTING_VALUE_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {SETTING_VALUE_ITEMS}'
        return self.notification_settings(
            "like_and_comment_on_photo_user_tagged", setting_value
        )

    def notification_user_tagged(self, setting_value: SETTING_VALUE = "off") -> bool:
        """
        Manage User Tagged NotificationSettings

        Parameters
        ----------
        setting_value: SETTING_VALUE
            Value of settings, default "off"

        Returns
        -------
        bool
        """
        assert (
            setting_value in SETTING_VALUE_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {SETTING_VALUE_ITEMS}'
        return self.notification_settings("user_tagged", setting_value)

    def notification_comments(self, setting_value: SETTING_VALUE = "off") -> bool:
        """
        Manage Comments Notification Settings

        Parameters
        ----------
        setting_value: SETTING_VALUE
            Value of settings, default "off"

        Returns
        -------
        bool
        """
        assert (
            setting_value in SETTING_VALUE_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {SETTING_VALUE_ITEMS}'
        return self.notification_settings("comments", setting_value)

    def notification_comment_likes(self, setting_value: SETTING_VALUE = "off") -> bool:
        """
        Manage Comment Likes Notification Settings

        Parameters
        ----------
        setting_value: SETTING_VALUE
            Value of settings, default "off"

        Returns
        -------
        bool
        """
        assert (
            setting_value in SETTING_VALUE_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {SETTING_VALUE_ITEMS}'
        return self.notification_settings("comment_likes", setting_value)

    def notification_first_post(self, setting_value: SETTING_VALUE = "off") -> bool:
        """
        Manage First Post Notification Settings

        Parameters
        ----------
        setting_value: SETTING_VALUE
            Value of settings, default "off"

        Returns
        -------
        bool
        """
        assert (
            setting_value in SETTING_VALUE_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {SETTING_VALUE_ITEMS}'
        return self.notification_settings("first_post", setting_value)

    def notification_new_follower(self, setting_value: SETTING_VALUE = "off") -> bool:
        """
        Manage New Follower Notification Settings

        Parameters
        ----------
        setting_value: SETTING_VALUE
            Value of settings, default "off"

        Returns
        -------
        bool
        """
        assert (
            setting_value in SETTING_VALUE_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {SETTING_VALUE_ITEMS}'
        return self.notification_settings("new_follower", setting_value)

    def notification_follow_request_accepted(
        self, setting_value: SETTING_VALUE = "off"
    ) -> bool:
        """
        Manage Follow Request Accepted Notification Settings

        Parameters
        ----------
        setting_value: SETTING_VALUE
            Value of settings, default "off"

        Returns
        -------
        bool
        """
        assert (
            setting_value in SETTING_VALUE_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {SETTING_VALUE_ITEMS}'
        return self.notification_settings("follow_request_accepted", setting_value)

    def notification_connection(self, setting_value: SETTING_VALUE = "off") -> bool:
        """
        Manage Connection Notification Settings

        Parameters
        ----------
        setting_value: SETTING_VALUE
            Value of settings, default "off"

        Returns
        -------
        bool
        """
        assert (
            setting_value in SETTING_VALUE_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {SETTING_VALUE_ITEMS}'
        return self.notification_settings("connection_notification", setting_value)

    def notification_tagged_in_bio(self, setting_value: SETTING_VALUE = "off") -> bool:
        """
        Manage Tagged In Bio Notification Settings

        Parameters
        ----------
        setting_value: SETTING_VALUE
            Value of settings, default "off"

        Returns
        -------
        bool
        """
        assert (
            setting_value in SETTING_VALUE_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {SETTING_VALUE_ITEMS}'
        return self.notification_settings("tagged_in_bio", setting_value)

    def notification_pending_direct_share(
        self, setting_value: SETTING_VALUE = "off"
    ) -> bool:
        """
        Manage Pending Direct Share Notification Settings

        Parameters
        ----------
        setting_value: SETTING_VALUE
            Value of settings, default "off"

        Returns
        -------
        bool
        """
        assert (
            setting_value in SETTING_VALUE_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {SETTING_VALUE_ITEMS}'
        return self.notification_settings("pending_direct_share", setting_value)

    def notification_direct_share_activity(
        self, setting_value: SETTING_VALUE = "off"
    ) -> bool:
        """
        Manage Direct Share Activity Notification Settings

        Parameters
        ----------
        setting_value: SETTING_VALUE
            Value of settings, default "off"

        Returns
        -------
        bool
        """
        assert (
            setting_value in SETTING_VALUE_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {SETTING_VALUE_ITEMS}'
        return self.notification_settings("direct_share_activity", setting_value)

    def notification_direct_group_requests(
        self, setting_value: SETTING_VALUE = "off"
    ) -> bool:
        """
        Manage Direct Group Requests Notification Settings

        Parameters
        ----------
        setting_value: SETTING_VALUE
            Value of settings, default "off"

        Returns
        -------
        bool
        """
        assert (
            setting_value in SETTING_VALUE_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {SETTING_VALUE_ITEMS}'
        return self.notification_settings("direct_group_requests", setting_value)

    def notification_video_call(self, setting_value: SETTING_VALUE = "off") -> bool:
        """
        Manage Video Call Notification Settings

        Parameters
        ----------
        setting_value: SETTING_VALUE
            Value of settings, default "off"

        Returns
        -------
        bool
        """
        assert (
            setting_value in SETTING_VALUE_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {SETTING_VALUE_ITEMS}'
        return self.notification_settings("video_call", setting_value)

    def notification_rooms(self, setting_value: SETTING_VALUE = "off") -> bool:
        """
        Manage Rooms Notification Settings

        Parameters
        ----------
        setting_value: SETTING_VALUE
            Value of settings, default "off"

        Returns
        -------
        bool
        """
        assert (
            setting_value in SETTING_VALUE_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {SETTING_VALUE_ITEMS}'
        return self.notification_settings("rooms", setting_value)

    def notification_live_broadcast(self, setting_value: SETTING_VALUE = "off") -> bool:
        """
        Manage Live Broadcast Notification Settings

        Parameters
        ----------
        setting_value: SETTING_VALUE
            Value of settings, default "off"

        Returns
        -------
        bool
        """
        assert (
            setting_value in SETTING_VALUE_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {SETTING_VALUE_ITEMS}'
        return self.notification_settings("live_broadcast", setting_value)

    def notification_felix_upload_result(
        self, setting_value: SETTING_VALUE = "off"
    ) -> bool:
        """
        Manage Felix Upload Result Notification Settings

        Parameters
        ----------
        setting_value: SETTING_VALUE
            Value of settings, default "off"

        Returns
        -------
        bool
        """
        assert (
            setting_value in SETTING_VALUE_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {SETTING_VALUE_ITEMS}'
        return self.notification_settings("felix_upload_result", setting_value)

    def notification_view_count(self, setting_value: SETTING_VALUE = "off") -> bool:
        """
        Manage View Count Notification Settings

        Parameters
        ----------
        setting_value: SETTING_VALUE
            Value of settings, default "off"

        Returns
        -------
        bool
        """
        assert (
            setting_value in SETTING_VALUE_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {SETTING_VALUE_ITEMS}'
        return self.notification_settings("view_count", setting_value)

    def notification_fundraiser_creator(
        self, setting_value: SETTING_VALUE = "off"
    ) -> bool:
        """
        Manage Fundraiser Creator Notification Settings

        Parameters
        ----------
        setting_value: SETTING_VALUE
            Value of settings, default "off"

        Returns
        -------
        bool
        """
        assert (
            setting_value in SETTING_VALUE_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {SETTING_VALUE_ITEMS}'
        return self.notification_settings("fundraiser_creator", setting_value)

    def notification_fundraiser_supporter(
        self, setting_value: SETTING_VALUE = "off"
    ) -> bool:
        """
        Manage Fundraiser Supporter Notification Settings

        Parameters
        ----------
        setting_value: SETTING_VALUE
            Value of settings, default "off"

        Returns
        -------
        bool
        """
        assert (
            setting_value in SETTING_VALUE_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {SETTING_VALUE_ITEMS}'
        return self.notification_settings("fundraiser_supporter", setting_value)

    def notification_reminders(self, setting_value: SETTING_VALUE = "off") -> bool:
        """
        Manage Notification Reminders Settings

        Parameters
        ----------
        setting_value: SETTING_VALUE
            Value of settings, default "off"

        Returns
        -------
        bool
        """
        assert (
            setting_value in SETTING_VALUE_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {SETTING_VALUE_ITEMS}'
        return self.notification_settings("notification_reminders", setting_value)

    def notification_announcements(self, setting_value: SETTING_VALUE = "off") -> bool:
        """
        Manage Announcements Notification Settings

        Parameters
        ----------
        setting_value: SETTING_VALUE
            Value of settings, default "off"

        Returns
        -------
        bool
        """
        assert (
            setting_value in SETTING_VALUE_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {SETTING_VALUE_ITEMS}'
        return self.notification_settings("announcements", setting_value)

    def notification_report_updated(self, setting_value: SETTING_VALUE = "off") -> bool:
        """
        Manage Report Updated Notification Settings

        Parameters
        ----------
        setting_value: SETTING_VALUE
            Value of settings, default "off"

        Returns
        -------
        bool
        """
        assert (
            setting_value in SETTING_VALUE_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {SETTING_VALUE_ITEMS}'
        return self.notification_settings("report_updated", setting_value)

    def notification_login(self, setting_value: SETTING_VALUE = "off") -> bool:
        """
        Manage Login Notification Settings

        Parameters
        ----------
        setting_value: SETTING_VALUE
            Value of settings, default "off"

        Returns
        -------
        bool
        """
        assert (
            setting_value in SETTING_VALUE_ITEMS
        ), f'Unsupported setting_value="{setting_value}" {SETTING_VALUE_ITEMS}'
        return self.notification_settings("login_notification", setting_value)



================================================
FILE: instagrapi/mixins/password.py
================================================
import base64
import time

from Cryptodome.Cipher import AES, PKCS1_v1_5
from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes


class PasswordMixin:
    def password_encrypt(self, password):
        publickeyid, publickey = self.password_publickeys()
        session_key = get_random_bytes(32)
        iv = get_random_bytes(12)
        timestamp = str(int(time.time()))
        decoded_publickey = base64.b64decode(publickey.encode())
        recipient_key = RSA.import_key(decoded_publickey)
        cipher_rsa = PKCS1_v1_5.new(recipient_key)
        rsa_encrypted = cipher_rsa.encrypt(session_key)
        cipher_aes = AES.new(session_key, AES.MODE_GCM, iv)
        cipher_aes.update(timestamp.encode())
        aes_encrypted, tag = cipher_aes.encrypt_and_digest(password.encode("utf8"))
        size_buffer = len(rsa_encrypted).to_bytes(2, byteorder="little")
        payload = base64.b64encode(
            b"".join(
                [
                    b"\x01",
                    publickeyid.to_bytes(1, byteorder="big"),
                    iv,
                    size_buffer,
                    rsa_encrypted,
                    tag,
                    aes_encrypted,
                ]
            )
        )
        return f"#PWD_INSTAGRAM:4:{timestamp}:{payload.decode()}"

    def password_publickeys(self):
        resp = self.public.get("https://i.instagram.com/api/v1/qe/sync/")
        publickeyid = int(resp.headers.get("ig-set-password-encryption-key-id"))
        publickey = resp.headers.get("ig-set-password-encryption-pub-key")
        return publickeyid, publickey



================================================
FILE: instagrapi/mixins/photo.py
================================================
import json
import random
import shutil
import time
from pathlib import Path
from typing import Dict, List
from urllib.parse import urlparse
from uuid import uuid4

import requests

from instagrapi import config
from instagrapi.exceptions import (
    PhotoConfigureError,
    PhotoConfigureStoryError,
    PhotoNotUpload,
)
from instagrapi.extractors import extract_media_v1
from instagrapi.image_util import prepare_image
from instagrapi.types import (
    Location,
    Media,
    Story,
    StoryHashtag,
    StoryLink,
    StoryLocation,
    StoryMedia,
    StoryMention,
    StoryPoll,
    StorySticker,
    Usertag,
)
from instagrapi.utils import date_time_original, dumps

try:
    from PIL import Image
except ImportError:
    raise Exception("You don't have PIL installed. Please install PIL or Pillow>=8.1.1")


class DownloadPhotoMixin:
    """
    Helpers for downloading photo
    """

    def photo_download(self, media_pk: int, folder: Path = "") -> Path:
        """
        Download photo using media pk

        Parameters
        ----------
        media_pk: int
            Unique Media ID
        folder: Path, optional
            Directory in which you want to download the photo, default is "" and will download the files to working
                directory

        Returns
        -------
        Path
            Path for the file downloaded
        """
        media = self.media_info(media_pk)
        assert media.media_type == 1, "Must been photo"
        filename = "{username}_{media_pk}".format(
            username=media.user.username, media_pk=media_pk
        )
        return self.photo_download_by_url(media.thumbnail_url, filename, folder)

    def photo_download_by_url(
        self, url: str, filename: str = "", folder: Path = ""
    ) -> Path:
        """
        Download photo using URL

        Parameters
        ----------
        url: str
            URL for a media
        filename: str, optional
            Filename for the media
        folder: Path, optional
            Directory in which you want to download the photo, default is "" and will download the files to working
                directory

        Returns
        -------
        Path
            Path for the file downloaded
        """
        url = str(url)
        fname = urlparse(url).path.rsplit("/", 1)[1]
        filename = "%s.%s" % (filename, fname.rsplit(".", 1)[1]) if filename else fname
        path = Path(folder) / filename
        response = requests.get(url, stream=True, timeout=self.request_timeout)
        response.raise_for_status()
        with open(path, "wb") as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)
        return path.resolve()

    def photo_download_by_url_origin(self, url: str) -> bytes:
        """
        Download photo using URL

        Parameters
        ----------
        url: str
            URL for a media

        Returns
        -------
        bytes
        """
        url = str(url)
        response = requests.get(url, stream=True, timeout=self.request_timeout)
        response.raise_for_status()
        response.raw.decode_content = True
        return response.content


class UploadPhotoMixin:
    """
    Helpers for downloading photo
    """

    def photo_rupload(
        self,
        path: Path,
        upload_id: str = "",
        to_album: bool = False,
        for_story: bool = False,
    ) -> tuple:
        """
        Upload photo to Instagram

        Parameters
        ----------
        path: Path
            Path to the media
        upload_id: str, optional
            Unique upload_id (String). When None, then generate automatically. Example from video.video_configure
        to_album: bool, optional
        for_story: bool, optional
            Useful for resize util only

        Returns
        -------
        tuple
            (Upload ID for the media, width, height)
        """
        assert isinstance(path, Path), f"Path must been Path, now {path} ({type(path)})"
        valid_extensions = [".jpg", ".jpeg", ".png", ".webp"]
        if path.suffix.lower() not in valid_extensions:
            raise ValueError(
                "Invalid file format. Only JPG/JPEG/PNG/WEBP files are supported."
            )
        image_type = "image/jpeg"
        if path.suffix.lower() == ".png":
            image_type = "image/png"
        elif path.suffix.lower() == ".webp":
            image_type = "image/webp"

        # upload_id = 516057248854759
        upload_id = upload_id or str(int(time.time() * 1000))
        assert path, "Not specified path to photo"
        waterfall_id = str(uuid4())
        # upload_name example: '1576102477530_0_7823256191'
        upload_name = "{upload_id}_0_{rand}".format(
            upload_id=upload_id, rand=random.randint(1000000000, 9999999999)
        )
        # media_type: "2" when from video/igtv/album thumbnail, "1" - upload photo only
        rupload_params = {
            "retry_context": '{"num_step_auto_retry":0,"num_reupload":0,"num_step_manual_retry":0}',
            "media_type": "1",  # "2" if upload_id else "1",
            "xsharing_user_ids": "[]",
            "upload_id": upload_id,
            "image_compression": json.dumps(
                {"lib_name": "moz", "lib_version": "3.1.m", "quality": "80"}
            ),
        }
        if to_album:
            rupload_params["is_sidecar"] = "1"
        if for_story:
            photo_data, photo_size = prepare_image(
                str(path),
                max_side=1080,
                aspect_ratios=(9 / 16, 90 / 47),
                max_size=(1080, 1920),
            )
        else:
            photo_data, photo_size = prepare_image(str(path), max_side=1080)
        photo_len = str(len(photo_data))
        headers = {
            "Accept-Encoding": "gzip",
            "X-Instagram-Rupload-Params": json.dumps(rupload_params),
            "X_FB_PHOTO_WATERFALL_ID": waterfall_id,
            "X-Entity-Type": image_type,
            "Offset": "0",
            "X-Entity-Name": upload_name,
            "X-Entity-Length": photo_len,
            "Content-Type": "application/octet-stream",
            "Content-Length": photo_len,
        }
        response = self.private.post(
            "https://{domain}/rupload_igphoto/{name}".format(
                domain=config.API_DOMAIN, name=upload_name
            ),
            data=photo_data,
            headers=headers,
        )
        self.request_log(response)
        if response.status_code != 200:
            self.logger.error(
                "Photo Upload failed with the following response: %s", response
            )
            last_json = self.last_json  # local variable for read in sentry
            raise PhotoNotUpload(response.text, response=response, **last_json)
        with Image.open(path) as im:
            width, height = im.size
        return upload_id, width, height

    def photo_upload(
        self,
        path: Path,
        caption: str,
        upload_id: str = "",
        usertags: List[Usertag] = [],
        location: Location = None,
        extra_data: Dict[str, str] = {},
    ) -> Media:
        """
        Upload photo and configure to feed

        Parameters
        ----------
        path: Path
            Path to the media
        caption: str
            Media caption
        upload_id: str, optional
            Unique upload_id (String). When None, then generate automatically. Example from video.video_configure
        usertags: List[Usertag], optional
            List of users to be tagged on this upload, default is empty list.
        location: Location, optional
            Location tag for this upload, default is None
        extra_data: Dict[str, str], optional
            Dict of extra data, if you need to add your params, like {"share_to_facebook": 1}.

        Returns
        -------
        Media
            An object of Media class
        """
        path = Path(path)
        valid_extensions = [".jpg", ".jpeg", ".png", ".webp"]
        if path.suffix.lower() not in valid_extensions:
            raise ValueError(
                "Invalid file format. Only JPG/JPEG/PNG/WEBP files are supported."
            )

        upload_id, width, height = self.photo_rupload(path, upload_id)
        for attempt in range(10):
            self.logger.debug(f"Attempt #{attempt} to configure Photo: {path}")
            time.sleep(3)
            if self.photo_configure(
                upload_id,
                width,
                height,
                caption,
                usertags,
                location,
                extra_data=extra_data,
            ):
                media = self.last_json.get("media")
                self.expose()
                return extract_media_v1(media)
        raise PhotoConfigureError(response=self.last_response, **self.last_json)

    def photo_configure(
        self,
        upload_id: str,
        width: int,
        height: int,
        caption: str,
        usertags: List[Usertag] = [],
        location: Location = None,
        extra_data: Dict[str, str] = {},
    ) -> Dict:
        """
        Post Configure Photo (send caption to Instagram)

        Parameters
        ----------
        upload_id: str
            Unique upload_id
        width: int
            Width of the video in pixels
        height: int
            Height of the video in pixels
        caption: str
            Media caption
        usertags: List[Usertag], optional
            List of users to be tagged on this upload, default is empty list.
        location: Location, optional
            Location tag for this upload, default is None
        extra_data: Dict[str, str], optional
            Dict of extra data, if you need to add your params, like {"share_to_facebook": 1}.

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        usertags = [
            {"user_id": tag.user.pk, "position": [tag.x, tag.y]} for tag in usertags
        ]
        data = {
            "timezone_offset": str(self.timezone_offset),
            "camera_model": self.device.get("model", ""),
            "camera_make": self.device.get("manufacturer", ""),
            "scene_type": "?",
            "nav_chain": (
                "8rL:self_profile:4,ProfileMediaTabFragment:self_profile:5,"
                "UniversalCreationMenuFragment:universal_creation_menu:7,"
                "ProfileMediaTabFragment:self_profile:8,"
                "MediaCaptureFragment:tabbed_gallery_camera:9,"
                "Dd3:photo_filter:10,"
                "FollowersShareFragment:metadata_followers_share:11"
            ),
            "date_time_original": date_time_original(time.localtime()),
            "date_time_digitalized": date_time_original(time.localtime()),
            "creation_logger_session_id": self.client_session_id,
            "scene_capture_type": "standard",
            "software": config.SOFTWARE.format(**self.device_settings),
            "multi_sharing": "1",
            "location": self.location_build(location),
            "media_folder": "Camera",
            "source_type": "4",
            "caption": caption,
            "upload_id": upload_id,
            "device": self.device,
            "usertags": json.dumps({"in": usertags}),
            "edits": {
                "crop_original_size": [width * 1.0, height * 1.0],
                "crop_center": [0.0, 0.0],
                "crop_zoom": 1.0,
            },
            "extra": {"source_width": width, "source_height": height},
            **extra_data,
        }
        return self.private_request("media/configure/", self.with_default_data(data))

    def photo_upload_to_story(
        self,
        path: Path,
        caption: str = "",
        upload_id: str = "",
        mentions: List[StoryMention] = [],
        locations: List[StoryLocation] = [],
        links: List[StoryLink] = [],
        hashtags: List[StoryHashtag] = [],
        stickers: List[StorySticker] = [],
        medias: List[StoryMedia] = [],
        polls: List[StoryPoll] = [],
        extra_data: Dict[str, str] = {},
    ) -> Story:
        """
        Upload photo as a story and configure it

        Parameters
        ----------
        path: Path
            Path to the media
        caption: str
            Media caption
        upload_id: str, optional
            Unique upload_id (String). When None, then generate automatically. Example from video.video_configure
        mentions: List[StoryMention], optional
            List of mentions to be tagged on this upload, default is empty list.
        locations: List[StoryLocation], optional
            List of locations to be tagged on this upload, default is empty list.
        links: List[StoryLink]
            URLs for Swipe Up
        hashtags: List[StoryHashtag], optional
            List of hashtags to be tagged on this upload, default is empty list.
        stickers: List[StorySticker], optional
            List of stickers to be tagged on this upload, default is empty list.
        medias: List[StoryMedia], optional
            List of medias to be tagged on this upload, default is empty list.
        polls: List[StoryPoll], optional
            List of polls to be included on this upload, default is empty list.
        extra_data: Dict[str, str], optional
            Dict of extra data, if you need to add your params, like {"share_to_facebook": 1}.

        Returns
        -------
        Story
            An object of Media class
        """
        path = Path(path)
        upload_id, width, height = self.photo_rupload(path, upload_id, for_story=True)
        for attempt in range(10):
            self.logger.debug(f"Attempt #{attempt} to configure Photo: {path}")
            time.sleep(3)
            if self.photo_configure_to_story(
                upload_id,
                width,
                height,
                caption,
                mentions,
                locations,
                links,
                hashtags,
                stickers,
                medias,
                polls,
                extra_data=extra_data,
            ):
                media = self.last_json.get("media")
                self.expose()
                return Story(
                    links=links,
                    mentions=mentions,
                    hashtags=hashtags,
                    locations=locations,
                    stickers=stickers,
                    medias=medias,
                    polls=polls,
                    **extract_media_v1(media).dict(),
                )
        raise PhotoConfigureStoryError(response=self.last_response, **self.last_json)

    def photo_configure_to_story(
        self,
        upload_id: str,
        width: int,
        height: int,
        caption: str,
        mentions: List[StoryMention] = [],
        locations: List[StoryLocation] = [],
        links: List[StoryLink] = [],
        hashtags: List[StoryHashtag] = [],
        stickers: List[StorySticker] = [],
        medias: List[StoryMedia] = [],
        polls: List[StoryPoll] = [],
        extra_data: Dict[str, str] = {},
    ) -> Dict:
        """
        Post configure photo

        Parameters
        ----------
        upload_id: str
            Unique upload_id
        width: int
            Width of the video in pixels
        height: int
            Height of the video in pixels
        caption: str
            Media caption
        mentions: List[StoryMention], optional
            List of mentions to be tagged on this upload, default is empty list.
        locations: List[StoryLocation], optional
            List of locations to be tagged on this upload, default is empty list.
        links: List[StoryLink]
            URLs for Swipe Up
        hashtags: List[StoryHashtag], optional
            List of hashtags to be tagged on this upload, default is empty list.
        stickers: List[StorySticker], optional
            List of stickers to be tagged on this upload, default is empty list.
        medias: List[StoryMedia], optional
            List of medias to be tagged on this upload, default is empty list.
        polls: List[StoryPoll], optional
            List of polls to be included on this upload, default is empty list.
        extra_data: Dict[str, str], optional
            Dict of extra data, if you need to add your params, like {"share_to_facebook": 1}.

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        timestamp = int(time.time())
        mentions = mentions.copy()
        locations = locations.copy()
        links = links.copy()
        hashtags = hashtags.copy()
        stickers = stickers.copy()
        medias = medias.copy()
        polls = polls.copy()
        story_sticker_ids = []
        data = {
            "text_metadata": (
                '[{"font_size":40.0,"scale":1.0,"width":611.0,"height":169.0,'
                '"x":0.51414347,"y":0.8487708,"rotation":0.0}]'
            ),  # REMOVEIT
            "supported_capabilities_new": json.dumps(config.SUPPORTED_CAPABILITIES),
            "has_original_sound": "1",
            "camera_session_id": self.client_session_id,
            "scene_capture_type": "",
            "timezone_offset": str(self.timezone_offset),
            "client_shared_at": str(timestamp - 5),  # 5 seconds ago
            "story_sticker_ids": "",
            "media_folder": "Camera",
            "configure_mode": "1",
            "source_type": "4",
            "creation_surface": "camera",
            "imported_taken_at": (timestamp - 3 * 24 * 3600),  # 3 days ago
            "capture_type": "normal",
            "rich_text_format_types": '["default"]',  # REMOVEIT
            "upload_id": upload_id,
            "client_timestamp": str(timestamp),
            "device": self.device,
            "_uid": self.user_id,
            "_uuid": self.uuid,
            "device_id": self.android_device_id,
            "composition_id": self.generate_uuid(),
            "app_attribution_android_namespace": "",
            "media_transformation_info": dumps(
                {
                    "width": str(width),
                    "height": str(height),
                    "x_transform": "0",
                    "y_transform": "0",
                    "zoom": "1.0",
                    "rotation": "0.0",
                    "background_coverage": "0.0",
                }
            ),
            "original_media_type": "photo",
            "camera_entry_point": str(random.randint(25, 164)),  # e.g. 25
            "edits": {
                "crop_original_size": [width * 1.0, height * 1.0],
                # "crop_center": [0.0, 0.0],
                # "crop_zoom": 1.0,
                "filter_type": 0,
                "filter_strength": 1.0,
            },
            "extra": {"source_width": width, "source_height": height},
        }
        if caption:
            data["caption"] = caption
        data.update(extra_data)
        tap_models = []
        static_models = []
        if mentions:
            for mention in mentions:
                reel_mentions = [
                    {
                        "x": mention.x,
                        "y": mention.y,
                        "z": 0,
                        "width": mention.width,
                        "height": mention.height,
                        "rotation": 0.0,
                        "type": "mention",
                        "user_id": str(mention.user.pk),
                        "is_sticker": False,
                        "display_type": "mention_username",
                    }
                ]
                data["reel_mentions"] = json.dumps(reel_mentions)
                tap_models.extend(reel_mentions)
        if hashtags:
            story_sticker_ids.append("hashtag_sticker")
            for mention in hashtags:
                item = {
                    "x": mention.x,
                    "y": mention.y,
                    "z": 0,
                    "width": mention.width,
                    "height": mention.height,
                    "rotation": 0.0,
                    "type": "hashtag",
                    "tag_name": mention.hashtag.name,
                    "is_sticker": True,
                    "tap_state": 0,
                    "tap_state_str_id": "hashtag_sticker_gradient",
                }
                tap_models.append(item)
        if locations:
            story_sticker_ids.append("location_sticker")
            for mention in locations:
                mention.location = self.location_complete(mention.location)
                item = {
                    "x": mention.x,
                    "y": mention.y,
                    "z": 0,
                    "width": mention.width,
                    "height": mention.height,
                    "rotation": 0.0,
                    "type": "location",
                    "location_id": str(mention.location.pk),
                    "is_sticker": True,
                    "tap_state": 0,
                    "tap_state_str_id": "location_sticker_vibrant",
                }
                tap_models.append(item)
        if links:
            # instagram allow one link now
            link = links[0]
            self.private_request(
                "media/validate_reel_url/",
                {
                    "url": str(link.webUri),
                    "_uid": str(self.user_id),
                    "_uuid": str(self.uuid),
                },
            )
            stickers.append(
                StorySticker(
                    type="story_link",
                    x=link.x,
                    y=link.y,
                    z=link.z,
                    width=link.width,
                    height=link.height,
                    rotation=link.rotation,
                    extra=dict(
                        link_type="web",
                        url=str(link.webUri),
                        tap_state_str_id="link_sticker_default",
                    ),
                )
            )
            story_sticker_ids.append("link_sticker_default")
        if stickers:
            for sticker in stickers:
                sticker_extra = sticker.extra or {}
                if sticker.id:
                    sticker_extra["str_id"] = sticker.id
                    story_sticker_ids.append(sticker.id)
                tap_models.append(
                    {
                        "x": sticker.x,
                        "y": sticker.y,
                        "z": sticker.z,
                        "width": sticker.width,
                        "height": sticker.height,
                        "rotation": sticker.rotation,
                        "type": sticker.type,
                        "is_sticker": True,
                        "selected_index": 0,
                        "tap_state": 0,
                        **sticker_extra,
                    }
                )
                if sticker.type == "gif":
                    data["has_animated_sticker"] = "1"
        if medias:
            for feed_media in medias:
                assert feed_media.media_pk, "Required StoryMedia.media_pk"
                # if not feed_media.user_id:
                #     user = self.media_user(feed_media.media_pk)
                #     feed_media.user_id = user.pk
                item = {
                    "x": feed_media.x,
                    "y": feed_media.y,
                    "z": feed_media.z,
                    "width": feed_media.width,
                    "height": feed_media.height,
                    "rotation": feed_media.rotation,
                    "type": "feed_media",
                    "media_id": str(feed_media.media_pk),
                    "media_owner_id": str(feed_media.user_id or ""),
                    "product_type": "feed",
                    "is_sticker": True,
                    "tap_state": 0,
                    "tap_state_str_id": "feed_post_sticker_square",
                }
                tap_models.append(item)
            data["reshared_media_id"] = str(feed_media.media_pk)
        if polls:
            story_sticker_ids.append("polling_sticker_v2")
            for poll in polls:
                poll_extra = poll.extra or {}
                tap_models.append(
                    {
                        "x": round(poll.x, 7),
                        "y": round(poll.y, 7),
                        "z": poll.z,
                        "width": round(poll.width, 7),
                        "height": round(poll.height, 7),
                        "rotation": poll.rotation,
                        "type": poll.type,
                        "poll_type": poll.poll_type,
                        "is_sticker": True,
                        "tap_state": 0,
                        "tap_state_str_id": "polling_sticker_v2",
                        "is_multi_option_poll": poll.is_multi_option,
                        "is_shared_result": poll.is_shared_result,
                        "viewer_can_vote": poll.viewer_can_vote,
                        "finished": poll.finished,
                        "color": poll.color,
                        "question": poll.question,
                        "tallies": [
                            {
                                "count": 0,
                                "font_size": 39.0,
                                "text": o
                            }
                            for o in poll.options
                        ],
                        **poll_extra,
                    }
                )
        if tap_models:
            data["tap_models"] = dumps(tap_models)
        if static_models:
            data["static_models"] = dumps(static_models)
        if story_sticker_ids:
            data["story_sticker_ids"] = story_sticker_ids[0]
        return self.private_request(
            "media/configure_to_story/", self.with_default_data(data)
        )



================================================
FILE: instagrapi/mixins/private.py
================================================
import json
import logging
import random
import time
from json.decoder import JSONDecodeError

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from instagrapi import config
from instagrapi.exceptions import (
    BadPassword,
    ChallengeRequired,
    ClientBadRequestError,
    ClientConnectionError,
    ClientError,
    ClientForbiddenError,
    ClientJSONDecodeError,
    ClientNotFoundError,
    ClientRequestTimeout,
    ClientThrottledError,
    FeedbackRequired,
    InvalidMediaId,
    InvalidTargetUser,
    LoginRequired,
    MediaUnavailable,
    PleaseWaitFewMinutes,
    PrivateAccount,
    ProxyAddressIsBlocked,
    RateLimitError,
    SentryBlock,
    TwoFactorRequired,
    UnknownError,
    UserNotFound,
    VideoTooLongException,
)
from instagrapi.utils import dumps, generate_signature, random_delay


def manual_input_code(self, username: str, choice=None):
    """
    Manual security code helper

    Parameters
    ----------
    username: str
        User name of a Instagram account
    choice: optional
        Whether sms or email

    Returns
    -------
    str
        Code
    """
    code = None
    while True:
        code = input(f"Enter code (6 digits) for {username} ({choice}): ").strip()
        if code and code.isdigit():
            break
    return code  # is not int, because it can start from 0


def manual_change_password(self, username: str):
    pwd = None
    while not pwd:
        pwd = input(f"Enter password for {username}: ").strip()
    return pwd


class PrivateRequestMixin:
    """
    Helpers for private request
    """

    private_requests_count = 0
    handle_exception = None
    challenge_code_handler = manual_input_code
    change_password_handler = manual_change_password
    private_request_logger = logging.getLogger("private_request")
    request_timeout = 1
    domain = config.API_DOMAIN
    last_response = None
    last_json = {}

    def __init__(self, *args, **kwargs):
        # setup request session with retries
        session = requests.Session()
        try:
            retry_strategy = Retry(
                total=3,
                status_forcelist=[429, 500, 502, 503, 504],
                allowed_methods=["GET", "POST"],
                backoff_factor=2,
            )
        except TypeError:
            retry_strategy = Retry(
                total=3,
                status_forcelist=[429, 500, 502, 503, 504],
                method_whitelist=["GET", "POST"],
                backoff_factor=2,
            )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        self.private = session
        self.private.verify = False  # fix SSLError/HTTPSConnectionPool
        self.email = kwargs.pop("email", None)
        self.phone_number = kwargs.pop("phone_number", None)
        self.request_timeout = kwargs.pop("request_timeout", self.request_timeout)
        super().__init__(*args, **kwargs)

    def small_delay(self):
        """
        Small Delay

        Returns
        -------
        Void
        """
        time.sleep(random.uniform(0.75, 3.75))

    def very_small_delay(self):
        """
        Very small delay

        Returns
        -------
        Void
        """
        time.sleep(random.uniform(0.175, 0.875))

    @property
    def base_headers(self):
        locale = self.locale.replace("-", "_")
        accept_language = ["en-US"]
        if locale:
            lang = locale.replace("_", "-")
            if lang not in accept_language:
                accept_language.insert(0, lang)
        headers = {
            "X-IG-App-Locale": locale,
            "X-IG-Device-Locale": locale,
            "X-IG-Mapped-Locale": locale,
            "X-Pigeon-Session-Id": self.generate_uuid("UFS-", "-1"),
            "X-Pigeon-Rawclienttime": str(round(time.time(), 3)),
            # "X-IG-Connection-Speed": "-1kbps",
            "X-IG-Bandwidth-Speed-KBPS": str(
                random.randint(2500000, 3000000) / 1000
            ),  # "-1.000"
            "X-IG-Bandwidth-TotalBytes-B": str(
                random.randint(5000000, 90000000)
            ),  # "0"
            "X-IG-Bandwidth-TotalTime-MS": str(random.randint(2000, 9000)),  # "0"
            # "X-IG-EU-DC-ENABLED": "true", # <- type of DC? Eu is euro, but we use US
            # "X-IG-Prefetch-Request": "foreground",  # OLD from instabot
            "X-IG-App-Startup-Country": self.country.upper(),
            "X-Bloks-Version-Id": self.bloks_versioning_id,
            "X-IG-WWW-Claim": "0",
            # X-IG-WWW-Claim: hmac.AR3zruvyGTlwHvVd2ACpGCWLluOppXX4NAVDV-iYslo9CaDd
            "X-Bloks-Is-Layout-RTL": "false",
            "X-Bloks-Is-Panorama-Enabled": "true",
            "X-IG-Device-ID": self.uuid,
            "X-IG-Family-Device-ID": self.phone_id,
            "X-IG-Android-ID": self.android_device_id,
            "X-IG-Timezone-Offset": str(self.timezone_offset),
            "X-IG-Connection-Type": "WIFI",
            "X-IG-Capabilities": "3brTvx0=",  # "3brTvwE=" in instabot
            "X-IG-App-ID": self.app_id,
            "Priority": "u=3",
            "User-Agent": self.user_agent,
            "Accept-Language": ", ".join(accept_language),
            "X-MID": self.mid,  # e.g. X--ijgABABFjLLQ1NTEe0A6JSN7o, YRwa1QABBAF-ZA-1tPmnd0bEniTe
            "Accept-Encoding": "gzip, deflate",  # ignore zstd
            "Host": self.domain,
            "X-FB-HTTP-Engine": "Liger",
            "Connection": "keep-alive",
            # "Pragma": "no-cache",
            # "Cache-Control": "no-cache",
            "X-FB-Client-IP": "True",
            "X-FB-Server-Cluster": "True",
            "IG-INTENDED-USER-ID": str(self.user_id or 0),
            "X-IG-Nav-Chain": "9MV:self_profile:2,ProfileMediaTabFragment:self_profile:3,9Xf:self_following:4",
            "X-IG-SALT-IDS": str(random.randint(1061162222, 1061262222)),
        }
        if self.user_id:
            next_year = time.time() + 31536000  # + 1 year in seconds
            headers.update(
                {
                    "IG-U-DS-USER-ID": str(self.user_id),
                    # Direct:
                    "IG-U-IG-DIRECT-REGION-HINT": (
                        f"LLA,{self.user_id},{next_year}:"
                        "01f7bae7d8b131877d8e0ae1493252280d72f6d0d554447cb1dc9049b6b2c507c08605b7"
                    ),
                    "IG-U-SHBID": (
                        f"12695,{self.user_id},{next_year}:"
                        "01f778d9c9f7546cf3722578fbf9b85143cd6e5132723e5c93f40f55ca0459c8ef8a0d9f"
                    ),
                    "IG-U-SHBTS": (
                        f"{int(time.time())},{self.user_id},{next_year}:"
                        "01f7ace11925d0388080078d0282b75b8059844855da27e23c90a362270fddfb3fae7e28"
                    ),
                    "IG-U-RUR": (
                        f"RVA,{self.user_id},{next_year}:"
                        "01f7f627f9ae4ce2874b2e04463efdb184340968b1b006fa88cb4cc69a942a04201e544c"
                    ),
                }
            )
        if self.ig_u_rur:
            headers.update({"IG-U-RUR": self.ig_u_rur})
        if self.ig_www_claim:
            headers.update({"X-IG-WWW-Claim": self.ig_www_claim})
        return headers

    def set_country(self, country: str = "US"):
        """Set you country code (ISO 3166-1/3166-2)

        Parameters
        ----------
        country: str
            Your country code (ISO 3166-1/3166-2) string identifier (e.g. US, UK, RU)
            Advise to specify the country code of your proxy

        Returns
        -------
        bool
            A boolean value
        """
        self.settings["country"] = self.country = str(country)
        return True

    def set_country_code(self, country_code: int = 1):
        """Set country calling code

        Parameters
        ----------
        country_code: int

        Returns
        -------
        bool
            A boolean value
        """
        self.settings["country_code"] = self.country_code = int(country_code)
        return True

    def set_locale(self, locale: str = "en_US"):
        """Set you locale (ISO 3166-1/3166-2)

        Parameters
        ----------
        locale: str
            Your locale code (ISO 3166-1/3166-2) string identifier (e.g. US, UK, RU)
            Advise to specify the locale code of your proxy

        Returns
        -------
        bool
            A boolean value
        """
        user_agent = (self.settings.get("user_agent") or "").replace(
            self.locale, locale
        )
        self.settings["locale"] = self.locale = str(locale)
        self.set_user_agent(user_agent)  # update locale in user_agent
        if "_" in locale:
            self.set_country(locale.rsplit("_", 1)[1])
        return True

    def set_timezone_offset(self, seconds: int = 0):
        """Set you timezone offset in seconds

        Parameters
        ----------
        seconds: int
            Specify the offset in seconds from UTC

        Returns
        -------
        bool
            A boolean value
        """
        self.settings["timezone_offset"] = self.timezone_offset = int(seconds)
        return True

    def set_ig_u_rur(self, value):
        self.settings["ig_u_rur"] = self.ig_u_rur = value
        return True

    def set_ig_www_claim(self, value):
        self.settings["ig_www_claim"] = self.ig_www_claim = value
        return True

    @staticmethod
    def with_query_params(data, params):
        return dict(data, **{"query_params": json.dumps(params, separators=(",", ":"))})

    def _send_private_request(
        self,
        endpoint,
        data=None,
        params=None,
        login=False,
        with_signature=True,
        headers=None,
        extra_sig=None,
        domain: str = None,
    ):
        self.last_response = None
        self.last_json = last_json = {}  # for Sentry context in traceback
        self.private.headers.update(self.base_headers)
        if headers:
            self.private.headers.update(headers)
        if not login:
            time.sleep(self.request_timeout)
        # if self.user_id and login:
        #     raise Exception(f"User already logged ({self.user_id})")
        try:
            if not endpoint.startswith("/"):
                endpoint = f"/v1/{endpoint}"

            if endpoint == "/challenge/":  # wow so hard, is it safe tho?
                endpoint = "/v1/challenge/"

            api_url = f"https://{domain or config.API_DOMAIN}/api{endpoint}"
            self.logger.info(api_url)
            if data:  # POST
                # Client.direct_answer raw dict
                # data = json.dumps(data)
                self.private.headers[
                    "Content-Type"
                ] = "application/x-www-form-urlencoded; charset=UTF-8"
                if with_signature:
                    # Client.direct_answer doesn't need a signature
                    data = generate_signature(dumps(data))
                    if extra_sig:
                        data += "&".join(extra_sig)
                response = self.private.post(
                    api_url, data=data, params=params, proxies=self.private.proxies
                )
            else:  # GET
                self.private.headers.pop("Content-Type", None)
                response = self.private.get(
                    api_url, params=params, proxies=self.private.proxies
                )
            self.logger.debug(
                "private_request %s: %s (%s)",
                response.status_code,
                response.url,
                response.text,
            )
            mid = response.headers.get("ig-set-x-mid")
            if mid:
                self.mid = mid
            self.request_log(response)
            self.last_response = response
            response.raise_for_status()
            # last_json - for Sentry context in traceback
            self.last_json = last_json = response.json()
            self.logger.debug("last_json %s", last_json)
        except JSONDecodeError as e:
            self.logger.error(
                "Status %s: JSONDecodeError in private_request (user_id=%s, endpoint=%s) >>> %s",
                response.status_code,
                self.user_id,
                endpoint,
                response.text,
            )
            raise ClientJSONDecodeError(
                "JSONDecodeError {0!s} while opening {1!s}".format(e, response.url),
                response=response,
            )
        except requests.HTTPError as e:
            try:
                self.last_json = last_json = response.json()
            except JSONDecodeError:
                pass
            message = last_json.get("message", "")
            if "Please wait a few minutes" in message:
                raise PleaseWaitFewMinutes(e, response=e.response, **last_json)
            if e.response.status_code == 403:
                if message == "login_required":
                    raise LoginRequired(response=e.response, **last_json)
                if len(e.response.text) < 512:
                    last_json["message"] = e.response.text
                raise ClientForbiddenError(e, response=e.response, **last_json)
            elif e.response.status_code == 400:
                error_type = last_json.get("error_type")
                if last_json.get("two_factor_info"):
                    if not last_json.get("message"):
                        last_json["message"] = "Two-factor authentication required"
                    if last_json.get("error_type") != "two_factor_required":
                        self.logger.info(
                            f"Changing error_type from {last_json.get('error_type')} to two_factor_required due to presence of two_factor_info"
                        )
                        last_json["error_type"] = "two_factor_required"
                    raise TwoFactorRequired(**last_json)
                elif message == "challenge_required":
                    raise ChallengeRequired(**last_json)
                elif message == "feedback_required":
                    raise FeedbackRequired(
                        **dict(
                            last_json,
                            message="%s: %s"
                            % (message, last_json.get("feedback_message")),
                        )
                    )
                elif error_type == "sentry_block":
                    raise SentryBlock(**last_json)
                elif error_type == "rate_limit_error":
                    raise RateLimitError(**last_json)
                elif error_type == "bad_password":
                    msg = last_json.get("message", "").strip()
                    if msg:
                        if not msg.endswith("."):
                            msg = "%s." % msg
                        msg = "%s " % msg
                    last_json["message"] = (
                        "%sIf you are sure that the password is correct, then change your IP address, "
                        "because it is added to the blacklist of the Instagram Server"
                    ) % msg
                    raise BadPassword(**last_json)
                elif error_type == "two_factor_required":
                    if not last_json["message"]:
                        last_json["message"] = "Two-factor authentication required"
                    raise TwoFactorRequired(**last_json)
                elif "VideoTooLongException" in message:
                    raise VideoTooLongException(e, response=e.response, **last_json)
                elif "Not authorized to view user" in message:
                    raise PrivateAccount(e, response=e.response, **last_json)
                elif "Invalid target user" in message:
                    raise InvalidTargetUser(e, response=e.response, **last_json)
                elif "Invalid media_id" in message:
                    raise InvalidMediaId(e, response=e.response, **last_json)
                elif (
                    "Media is unavailable" in message
                    or "Media not found or unavailable" in message
                ):
                    raise MediaUnavailable(e, response=e.response, **last_json)
                elif "has been deleted" in message:
                    # Sorry, this photo has been deleted.
                    raise MediaUnavailable(e, response=e.response, **last_json)
                elif "unable to fetch followers" in message:
                    # returned when user not found
                    raise UserNotFound(e, response=e.response, **last_json)
                elif "The username you entered" in message:
                    # The username you entered doesn't appear to belong to an account.
                    # Please check your username and try again.
                    last_json["message"] = (
                        "Instagram has blocked your IP address, "
                        "use a quality proxy provider (not free, not shared)"
                    )
                    raise ProxyAddressIsBlocked(**last_json)
                elif error_type or message:
                    raise UnknownError(**last_json)
                # TODO: Handle last_json with {'message': 'counter get error', 'status': 'fail'}
                self.logger.exception(e)
                self.logger.warning(
                    "Status 400: %s",
                    message or "Empty response message. Maybe enabled Two-factor auth?",
                )
                raise ClientBadRequestError(e, response=e.response, **last_json)
            elif e.response.status_code == 429:
                self.logger.warning("Status 429: Too many requests")
                raise ClientThrottledError(e, response=e.response, **last_json)
            elif e.response.status_code == 404:
                self.logger.warning("Status 404: Endpoint %s does not exist", endpoint)
                raise ClientNotFoundError(e, response=e.response, **last_json)
            elif e.response.status_code == 408:
                self.logger.warning("Status 408: Request Timeout")
                raise ClientRequestTimeout(e, response=e.response, **last_json)
            raise ClientError(e, response=e.response, **last_json)
        except requests.ConnectionError as e:
            raise ClientConnectionError("{e.__class__.__name__} {e}".format(e=e))
        if last_json.get("status") == "fail":
            raise ClientError(response=response, **last_json)
        elif "error_title" in last_json:
            """Example: {
            'error_title': 'bad image input extra:{}', <-------------
            'media': {
                'device_timestamp': '1588184737203',
                'upload_id': '1588184737203'
            },
            'message': 'media_needs_reupload', <-------------
            'status': 'ok' <-------------
            }"""
            raise ClientError(response=response, **last_json)
        return last_json

    def request_log(self, response):
        self.private_request_logger.info(
            "%s [%s] %s %s (%s)",
            self.username,
            response.status_code,
            response.request.method,
            response.url,
            "{app_version}, {manufacturer} {model}".format(
                app_version=self.device_settings.get("app_version"),
                manufacturer=self.device_settings.get("manufacturer"),
                model=self.device_settings.get("model"),
            ),
        )

    def private_request(
        self,
        endpoint,
        data=None,
        params=None,
        login=False,
        with_signature=True,
        headers=None,
        extra_sig=None,
        domain: str = None,
    ):
        if self.authorization:
            if not headers:
                headers = {}
            if "authorization" not in headers:
                headers.update({"Authorization": self.authorization})
        kwargs = dict(
            data=data,
            params=params,
            login=login,
            with_signature=with_signature,
            headers=headers,
            extra_sig=extra_sig,
            domain=domain,
        )
        try:
            if self.delay_range:
                random_delay(delay_range=self.delay_range)
            self.private_requests_count += 1
            self._send_private_request(endpoint, **kwargs)
        except ClientRequestTimeout:
            self.logger.info(
                "Wait 60 seconds and try one more time (ClientRequestTimeout)"
            )
            time.sleep(60)
            return self._send_private_request(endpoint, **kwargs)
        # except BadPassword as e:
        #     raise e
        except Exception as e:
            if self.handle_exception:
                self.handle_exception(self, e)
            elif isinstance(e, ChallengeRequired):
                self.challenge_resolve(self.last_json)
            else:
                raise e
            if login and self.user_id:
                # After challenge resolve return last_json
                return self.last_json
            return self._send_private_request(endpoint, **kwargs)
        return self.last_json



================================================
FILE: instagrapi/mixins/public.py
================================================
import json
import logging
import time

try:
    from simplejson.errors import JSONDecodeError
except ImportError:
    from json.decoder import JSONDecodeError

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from instagrapi.exceptions import (
    ClientBadRequestError,
    ClientConnectionError,
    ClientError,
    ClientForbiddenError,
    ClientGraphqlError,
    ClientIncompleteReadError,
    ClientJSONDecodeError,
    ClientLoginRequired,
    ClientNotFoundError,
    ClientThrottledError,
    ClientUnauthorizedError,
)
from instagrapi.utils import random_delay


class PublicRequestMixin:
    public_requests_count = 0
    PUBLIC_API_URL = "https://www.instagram.com/"
    GRAPHQL_PUBLIC_API_URL = "https://www.instagram.com/graphql/query/"
    last_public_response = None
    last_public_json = {}
    public_request_logger = logging.getLogger("public_request")
    request_timeout = 1
    last_response_ts = 0

    def __init__(self, *args, **kwargs):
        # setup request session with retries
        session = requests.Session()
        try:
            retry_strategy = Retry(
                total=3,
                status_forcelist=[429, 500, 502, 503, 504],
                allowed_methods=["GET", "POST"],
                backoff_factor=2,
            )
        except TypeError:
            retry_strategy = Retry(
                total=3,
                status_forcelist=[429, 500, 502, 503, 504],
                method_whitelist=["GET", "POST"],
                backoff_factor=2,
            )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        self.public = session
        self.public.verify = False  # fix SSLError/HTTPSConnectionPool
        self.public.headers.update(
            {
                "Connection": "Keep-Alive",
                "Accept": "*/*",
                "Accept-Encoding": "gzip,deflate",
                "Accept-Language": "en-US",
                "User-Agent": (
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 "
                    "(KHTML, like Gecko) Version/11.1.2 Safari/605.1.15"
                ),
            }
        )
        self.request_timeout = kwargs.pop("request_timeout", self.request_timeout)
        super().__init__(*args, **kwargs)

    def public_request(
        self,
        url,
        data=None,
        params=None,
        headers=None,
        update_headers=None,
        return_json=False,
        retries_count=3,
        retries_timeout=2,
    ):
        kwargs = dict(
            data=data,
            params=params,
            headers=headers,
            return_json=return_json,
        )
        assert retries_count <= 10, "Retries count is too high"
        assert retries_timeout <= 600, "Retries timeout is too high"
        for iteration in range(retries_count):
            try:
                if self.delay_range:
                    random_delay(delay_range=self.delay_range)
                return self._send_public_request(url, update_headers=update_headers, **kwargs)
            except (
                ClientLoginRequired,
                ClientNotFoundError,
                ClientBadRequestError,
            ) as e:
                raise e  # Stop retries
            # except JSONDecodeError as e:
            #     raise ClientJSONDecodeError(e, respones=self.last_public_response)
            except ClientError as e:
                msg = str(e)
                if all(
                    (
                        isinstance(e, ClientConnectionError),
                        "SOCKSHTTPSConnectionPool" in msg,
                        "Max retries exceeded with url" in msg,
                        "Failed to establish a new connection" in msg,
                    )
                ):
                    raise e
                if retries_count > iteration + 1:
                    time.sleep(retries_timeout)
                else:
                    raise e
                continue

    def _send_public_request(
        self, url, data=None, params=None, headers=None, return_json=False, stream=None, timeout=None, update_headers=None
    ):
        self.public_requests_count += 1
        if headers:
            if update_headers in [None, True] :
                self.public.headers.update(headers)
            elif update_headers == False :
                pass
        if self.last_response_ts and (time.time() - self.last_response_ts) < 1.0:
            time.sleep(1.0)
        if self.request_timeout:
            time.sleep(self.request_timeout)
        try:
            if data is not None:  # POST
                response = self.public.data(
                    url,
                    data=data,
                    params=params,
                    proxies=self.public.proxies,
                    timeout=timeout,
                )
            else:  # GET
                response = self.public.get(
                    url,
                    params=params,
                    proxies=self.public.proxies,
                    stream=stream,
                    timeout=timeout,
                )

            if stream:
                return response

            expected_length = int(response.headers.get("Content-Length") or 0)
            actual_length = response.raw.tell()
            if actual_length < expected_length:
                raise ClientIncompleteReadError(
                    "Incomplete read ({} bytes read, {} more expected)".format(
                        actual_length, expected_length
                    ),
                    response=response,
                )

            self.public_request_logger.debug(
                "public_request %s: %s", response.status_code, response.url
            )

            self.public_request_logger.info(
                "[%s] [%s] %s %s",
                self.public.proxies.get("https"),
                response.status_code,
                "POST" if data else "GET",
                response.url,
            )
            self.last_public_response = response
            response.raise_for_status()
            if return_json:
                self.last_public_json = response.json()
                return self.last_public_json
            return response.text

        except JSONDecodeError as e:
            if "/login/" in response.url:
                raise ClientLoginRequired(e, response=response)

            self.public_request_logger.error(
                "Status %s: JSONDecodeError in public_request (url=%s) >>> %s",
                response.status_code,
                response.url,
                response.text,
            )
            raise ClientJSONDecodeError(
                "JSONDecodeError {0!s} while opening {1!s}".format(e, url),
                response=response,
            )
        except requests.HTTPError as e:
            if e.response.status_code == 401:
                # HTTPError: 401 Client Error: Unauthorized for url: https://i.instagram.com/api/v1/users....
                raise ClientUnauthorizedError(e, response=e.response)
            elif e.response.status_code == 403:
                raise ClientForbiddenError(e, response=e.response)
            elif e.response.status_code == 400:
                raise ClientBadRequestError(e, response=e.response)
            elif e.response.status_code == 429:
                raise ClientThrottledError(e, response=e.response)
            elif e.response.status_code == 404:
                raise ClientNotFoundError(e, response=e.response)
            raise ClientError(e, response=e.response)

        except requests.ConnectionError as e:
            raise ClientConnectionError("{} {}".format(e.__class__.__name__, str(e)))
        finally:
            self.last_response_ts = time.time()

    def public_a1_request(self, endpoint, data=None, params=None, headers=None):
        url = (self.PUBLIC_API_URL + str(endpoint)).replace(
            ".com//", ".com/"
        )  # (jarrodnorwell) fixed KeyError: 'data', fixed // error
        params = params or {}
        params.update({"__a": 1, "__d": "dis"})

        response = self.public_request(
            url, data=data, params=params, headers=headers, return_json=True
        )
        return response.get("graphql") or response

    def public_a1_request_user_info_by_username(self, username, data=None, params=None):
        params = params or {}
        url = self.PUBLIC_API_URL + f"api/v1/users/web_profile_info/?username={username}"
        headers = {'x-ig-app-id': '936619743392459'}
        response = self.public_request(
            url, data=data, params=params, headers=headers, return_json=True
        )
        return response.get("user") or response

    def public_graphql_request(
        self,
        variables,
        query_hash=None,
        query_id=None,
        data=None,
        params=None,
        headers=None,
    ):
        assert query_id or query_hash, "Must provide valid one of: query_id, query_hash"
        default_params = {"variables": json.dumps(variables, separators=(",", ":"))}
        if query_id:
            default_params["query_id"] = query_id

        if query_hash:
            default_params["query_hash"] = query_hash

        if params:
            params.update(default_params)
        else:
            params = default_params

        try:
            body_json = self.public_request(
                self.GRAPHQL_PUBLIC_API_URL,
                data=data,
                params=params,
                headers=headers,
                return_json=True,
            )

            if body_json.get("status", None) != "ok":
                raise ClientGraphqlError(
                    "Unexpected status '{}' in response. Message: '{}'".format(
                        body_json.get("status", None), body_json.get("message", None)
                    ),
                    response=body_json,
                )

            return body_json["data"]

        except ClientBadRequestError as e:
            message = None
            try:
                body_json = e.response.json()
                message = body_json.get("message", None)
            except JSONDecodeError:
                pass
            raise ClientGraphqlError(
                "Error: '{}'. Message: '{}'".format(e, message), response=e.response
            )


class TopSearchesPublicMixin:
    def top_search(self, query):
        """Anonymous IG search request"""
        url = "https://www.instagram.com/web/search/topsearch/"
        params = {
            "context": "blended",
            "query": query,
            "rank_token": 0.7763938004511706,
            "include_reel": "true",
        }
        response = self.public_request(url, params=params, return_json=True)
        return response


class ProfilePublicMixin:
    def location_feed(self, location_id, count=16, end_cursor=None):
        if count > 50:
            raise ValueError("Count cannot be greater than 50")
        variables = {
            "id": location_id,
            "first": int(count),
        }
        if end_cursor:
            variables["after"] = end_cursor
        data = self.public_graphql_request(
            variables, query_hash="1b84447a4d8b6d6d0426fefb34514485"
        )
        return data["location"]

    def profile_related_info(self, profile_id):
        variables = {
            "user_id": profile_id,
            "include_chaining": True,
            "include_reel": True,
            "include_suggested_users": True,
            "include_logged_out_extras": True,
            "include_highlight_reels": True,
            "include_related_profiles": True,
        }
        data = self.public_graphql_request(
            variables, query_hash="e74d51c10ecc0fe6250a295b9bb9db74"
        )
        return data["user"]



================================================
FILE: instagrapi/mixins/share.py
================================================
import base64
from urllib.parse import urlparse

from instagrapi.types import Share


class ShareMixin:
    def share_info(self, code: str) -> Share:
        """
        Get Share object by code

        Parameters
        ----------
        code: str
            Share code

        Returns
        -------
        Share
            Share object
        """
        if isinstance(code, str):
            code = code.encode()
        # ignore example from instagram: b'highli\xb1\xdb\x1dght:17988089629383770'
        data = (
            base64.b64decode(code)
            .decode(errors="ignore")
            .replace("\x1d", "")
            .split(":")
        )
        return Share(type=data[0], pk=data[1])

    def share_info_by_url(self, url: str) -> Share:
        """
        Get Share object by URL

        Parameters
        ----------
        url: str
            URL of the share object

        Returns
        -------
        Share
            Share object
        """
        return self.share_info(self.share_code_from_url(url))

    def share_code_from_url(self, url: str) -> str:
        """
        Get Share code from URL

        Parameters
        ----------
        url: str
            URL of the share object

        Returns
        -------
        str
            Share code
        """
        path = urlparse(url).path
        parts = [p for p in path.split("/") if p]
        return parts.pop()



================================================
FILE: instagrapi/mixins/signup.py
================================================
import random
import time
from uuid import uuid4

from instagrapi.exceptions import (
    AgeEligibilityError,
    CaptchaChallengeRequired,
    ClientError,
    EmailInvalidError,
    EmailNotAvailableError,
    EmailVerificationSendError,
)
from instagrapi.extractors import extract_user_short
from instagrapi.types import UserShort

CHOICE_EMAIL = 1


class SignUpMixin:
    waterfall_id = str(uuid4())
    adid = str(uuid4())
    wait_seconds = 5

    def signup(
        self,
        username: str,
        password: str,
        email: str,
        phone_number: str,
        full_name: str = "",
        year: int = None,
        month: int = None,
        day: int = None,
    ) -> UserShort:
        self.get_signup_config()
        check = self.check_email(email)
        if not check.get("valid"):
            raise EmailInvalidError(
                f"Email not valid: {check.get('error_title', check)}"
            )
        if not check.get("available"):
            raise EmailNotAvailableError(
                f"Email not available: {check.get('feedback_message', check)}"
            )
        sent = self.send_verify_email(email)
        if not sent.get("email_sent"):
            raise EmailVerificationSendError(
                f"Failed to send verification email: {sent}"
            )

        # Date of Birth (DOB) Age Eligibility Check
        if year and month and day:
            age_check_result = self.check_age_eligibility(year, month, day)
            if not age_check_result.get(
                "eligible"
            ):  # Assuming "eligible": True is success
                raise AgeEligibilityError(
                    f"Account not eligible based on age criteria: {age_check_result}"
                )

        # send code confirmation
        code = ""
        for attempt in range(1, 11):
            code = self.challenge_code_handler(username, CHOICE_EMAIL)
            if code:
                break
            time.sleep(self.wait_seconds * attempt)
        print(
            f'Enter code "{code}" for {username} '
            f"({attempt} attempts, by {self.wait_seconds} seconds)"
        )
        signup_code = self.check_confirmation_code(email, code).get("signup_code")
        retries = 0
        kwargs = {
            "username": username,
            "password": password,
            "email": email,
            "signup_code": signup_code,
            "full_name": full_name,
            "year": year,
            "month": month,
            "day": day,
        }
        while retries < 3:
            data = self.accounts_create(**kwargs)
            if data.get("message") != "challenge_required":
                break
            if self.challenge_flow(data["challenge"]):
                kwargs.update({"suggestedUsername": "", "sn_result": "MLA"})
            retries += 1
        return extract_user_short(data["created_user"])

    def get_signup_config(self) -> dict:
        return self.private_request(
            "consent/get_signup_config/",
            params={"guid": self.uuid, "main_account_selected": False},
        )

    def check_email(self, email) -> dict:
        """Check available (free, not registred) email"""
        return self.private_request(
            "users/check_email/",
            {
                "android_device_id": self.device_id,
                "login_nonce_map": "{}",
                "login_nonces": "[]",
                "email": email,
                "qe_id": str(uuid4()),
                "waterfall_id": self.waterfall_id,
            },
        )

    def send_verify_email(self, email) -> dict:
        """Send request to receive code to email"""
        return self.private_request(
            "accounts/send_verify_email/",
            {
                "phone_id": self.phone_id,
                "device_id": self.device_id,
                "email": email,
                "waterfall_id": self.waterfall_id,
                "auto_confirm_only": "false",
            },
        )

    def check_confirmation_code(self, email, code) -> dict:
        """Enter code from email"""
        return self.private_request(
            "accounts/check_confirmation_code/",
            {
                "code": code,
                "device_id": self.device_id,
                "email": email,
                "waterfall_id": self.waterfall_id,
            },
        )

    def check_age_eligibility(self, year, month, day):
        return self.private.post(
            "consent/check_age_eligibility/",
            data={"_csrftoken": self.token, "day": day, "year": year, "month": month},
        ).json()

    def accounts_create(
        self,
        username: str,
        password: str,
        email: str,
        signup_code: str,
        full_name: str = "",
        year: int = None,
        month: int = None,
        day: int = None,
        **kwargs,
    ) -> dict:
        # timestamp = datetime.now().strftime("%s")  # Unused variable
        # nonce = f'{username}|{timestamp}|\xb9F"\x8c\xa2I\xaaz|\xf6xz\x86\x92\x91Y\xa5\xaa#f*o%\x7f'  # Unused variable
        data = {
            "is_secondary_account_creation": "true",
            "jazoest": str(int(random.randint(22300, 22399))),  # "22341",
            "suggestedUsername": "sn_result",
            "do_not_auto_login_if_credentials_match": "false",
            "phone_id": self.phone_id,
            "enc_password": self.password_encrypt(password),
            "username": str(username),
            "first_name": str(full_name),
            "adid": self.adid,
            "guid": self.uuid,
            "device_id": self.device_id,
            "_uuid": self.uuid,
            "email": email,
            "force_sign_up_code": signup_code,
            "waterfall_id": self.waterfall_id,
            "one_tap_opt_in": "true",
            **kwargs,
        }
        return self.private_request(
            "accounts/create/", data, domain="www.instagram.com"
        )

    def challenge_flow(self, data):
        data = self.challenge_api(data)
        while True:
            if data.get("message") == "challenge_required":
                data = self.challenge_captcha(data["challenge"])
                continue
            elif data.get("challengeType") == "SubmitPhoneNumberForm":
                data = self.challenge_submit_phone_number(data)
                continue
            elif data.get("challengeType") == "VerifySMSCodeFormForSMSCaptcha":
                data = self.challenge_verify_sms_captcha(data)
                continue

    def challenge_api(self, data):
        resp = self.private.get(
            f"https://i.instagram.com/api/v1{data['api_path']}",
            params={
                "guid": self.uuid,
                "device_id": self.device_id,
                "challenge_context": data["challenge_context"],
            },
        )
        return resp.json()

    def challenge_captcha(self, challenge_json_data):
        api_path = challenge_json_data.get("api_path")
        site_key = challenge_json_data.get("fields", {}).get("sitekey")
        challenge_type = challenge_json_data.get("challengeType")  # For logging/context

        if not site_key or not api_path:
            self.logger.error(
                f"Malformed captcha challenge data from Instagram: site_key={site_key}, api_path={api_path}"
            )
            raise ClientError(
                "Malformed captcha challenge data from Instagram (missing site_key or api_path)."
            )

        challenge_post_url = f"https://i.instagram.com{api_path}"

        captcha_details_for_solver = {
            "site_key": site_key,
            "challenge_type": challenge_type,
            "raw_challenge_json": challenge_json_data,
            "page_url": "https://www.instagram.com/accounts/emailsignup/",  # Common page for signup captcha
        }

        try:
            # self.captcha_resolve is assumed to be implemented on the main Client class
            # and is expected to raise CaptchaChallengeRequired if it cannot obtain a token.
            g_recaptcha_response = self.captcha_resolve(**captcha_details_for_solver)
        except CaptchaChallengeRequired:
            self.logger.warning(
                "Captcha solution was required by Instagram but not provided/resolved by any configured handler."
            )
            raise  # Re-raise for the user of instagrapi to handle or be informed.
        except Exception as e:
            self.logger.error(
                f"An unexpected error occurred during the captcha resolution process: {e}",
                exc_info=True,
            )
            raise ClientError(
                f"Captcha resolution process failed: {e}"
            )  # Wrap other errors

        # Proceed to POST the g_recaptcha_response:
        resp = self.private.post(
            challenge_post_url,
            data={"g-recaptcha-response": g_recaptcha_response},
        )
        return resp.json()

    def challenge_submit_phone_number(self, data, phone_number):
        api_path = data.get("navigation", {}).get("forward")
        resp = self.private.post(
            f"https://i.instagram.com{api_path}",
            data={
                "phone_number": phone_number,
                "challenge_context": data["challenge_context"],
            },
        )
        return resp.json()

    def challenge_verify_sms_captcha(self, data, security_code):
        api_path = data.get("navigation", {}).get("forward")
        resp = self.private.post(
            f"https://i.instagram.com{api_path}",
            data={
                "security_code": security_code,
                "challenge_context": data["challenge_context"],
            },
        )
        return resp.json()



================================================
FILE: instagrapi/mixins/story.py
================================================
import json
import shutil
from copy import deepcopy
from pathlib import Path
from typing import List
from urllib.parse import urlparse

from instagrapi import config
from instagrapi.exceptions import ClientNotFoundError, StoryNotFound, UserNotFound
from instagrapi.extractors import (
    extract_story_gql,
    extract_story_v1,
    extract_user_short,
)
from instagrapi.types import Story, UserShort


class StoryMixin:
    _stories_cache = {}  # pk -> object

    def story_pk_from_url(self, url: str) -> str:
        """
        Get Story (media) PK from URL

        Parameters
        ----------
        url: str
            URL of the story

        Returns
        -------
        str
            Media PK

        Examples
        --------
        https://www.instagram.com/stories/dhbastards/2581281926631793076/ -> 2581281926631793076
        """
        path = urlparse(url).path
        parts = [p for p in path.split("/") if p and p.isdigit()]
        return str(parts[0])

    def story_info_v1(self, story_pk: str) -> Story:
        """
        Get Story by pk or id

        Parameters
        ----------
        story_pk: str
            Unique identifier of the story

        Returns
        -------
        Story
            An object of Story type
        """
        story_id = self.media_id(story_pk)
        story_pk, user_id = story_id.split("_")

        stories = self.user_stories_v1(user_id)
        for story in stories:
            self._stories_cache[story.pk] = story
        if story_pk not in self._stories_cache:
            raise StoryNotFound(story_pk=story_pk, **self.last_json)
        story = self._stories_cache[story_pk]
        return deepcopy(story)

    def story_info(self, story_pk: str, use_cache: bool = True) -> Story:
        """
        Get Story by pk or id

        Parameters
        ----------
        story_pk: str
            Unique identifier of the story
        use_cache: bool, optional
            Whether or not to use information from cache, default value is True

        Returns
        -------
        Story
            An object of Story type
        """
        if not use_cache or story_pk not in self._stories_cache:
            story = self.story_info_v1(story_pk)
            self._stories_cache[story_pk] = story
        return deepcopy(self._stories_cache[story_pk])

    def story_delete(self, story_pk: str) -> bool:
        """
        Delete story

        Parameters
        ----------
        story_pk: str
            Unique identifier of the story

        Returns
        -------
        bool
            A boolean value
        """
        assert self.user_id, "Login required"
        media_id = self.media_id(story_pk)
        self._stories_cache.pop(self.media_pk(media_id), None)
        return self.media_delete(media_id)

    def users_stories_gql(
        self, user_ids: List[int], amount: int = 0
    ) -> List[UserShort]:
        """
        Get a user's stories (Public API)

        Parameters
        ----------
        user_ids: List[int]
            List of users
        amount: int
            Max amount of stories

        Returns
        -------
        List[UserShort]
            A list of objects of UserShort for each user_id
        """
        assert isinstance(user_ids, list), "user_ids should be a list of user_id"
        self.inject_sessionid_to_public()

        def _userid_chunks():
            assert user_ids is not None
            user_ids_per_query = 50
            for i in range(0, len(user_ids), user_ids_per_query):
                end = i + user_ids_per_query
                yield user_ids[i:end]

        stories_un = {}
        for userid_chunk in _userid_chunks():
            res = self.public_graphql_request(
                query_hash="303a4ae99711322310f25250d988f3b7",
                variables={"reel_ids": userid_chunk, "precomposed_overlay": False},
            )
            stories_un.update(res)
        users = []
        for media in stories_un["reels_media"]:
            user = extract_user_short(media["owner"])
            items = media["items"]
            if amount:
                items = items[:amount]
            user.stories = [extract_story_gql(m) for m in items]
            users.append(user)
        return users

    def user_stories_gql(self, user_id: str, amount: int = None) -> List[Story]:
        """
        Get a user's stories (Public API)

        Parameters
        ----------
        user_id: str
        amount: int, optional
            Maximum number of story to return, default is all

        Returns
        -------
        List[UserShort]
            A list of objects of UserShort for each user_id
        """
        user = self.users_stories_gql([user_id], amount=amount)[0]
        stories = deepcopy(user.stories)
        if amount:
            stories = stories[:amount]
        return stories

    def user_stories_v1(self, user_id: str, amount: int = None) -> List[Story]:
        """
        Get a user's stories (Private API)

        Parameters
        ----------
        user_id: str
        amount: int, optional
            Maximum number of story to return, default is all

        Returns
        -------
        List[Story]
            A list of objects of Story
        """
        params = {
            "supported_capabilities_new": json.dumps(config.SUPPORTED_CAPABILITIES)
        }
        user_id = int(user_id)
        reel = (
            self.private_request(f"feed/user/{user_id}/story/", params=params).get(
                "reel"
            )
            or {}
        )
        stories = []
        for item in reel.get("items", []):
            stories.append(extract_story_v1(item))
        if amount:
            stories = stories[: int(amount)]
        return stories

    def user_stories(self, user_id: str, amount: int = None) -> List[Story]:
        """
        Get a user's stories

        Parameters
        ----------
        user_id: str
        amount: int, optional
            Maximum number of story to return, default is all

        Returns
        -------
        List[Story]
            A list of objects of STory
        """
        try:
            return self.user_stories_gql(user_id, amount)
        except ClientNotFoundError as e:
            raise UserNotFound(e, user_id=user_id, **self.last_json)
        except IndexError:
            return []
        except Exception:
            return self.user_stories_v1(user_id, amount)

    def story_seen(self, story_pks: List[int], skipped_story_pks: List[int] = []):
        """
        Mark stories as seen

        Parameters
        ----------
        story_pks: List[int]

        Returns
        -------
        bool
            A boolean value
        """
        assert isinstance(story_pks, list), "story_pks should be a list of story.pk"
        return self.media_seen(
            [self.media_id(mid) for mid in story_pks],
            [self.media_id(mid) for mid in skipped_story_pks],
        )

    def story_download(
        self, story_pk: str, filename: str = "", folder: Path = ""
    ) -> Path:
        """
        Download story media by media_type

        Parameters
        ----------
        story_pk: str

        Returns
        -------
        Path
            Path for the file downloaded
        """
        story = self.story_info(story_pk)
        url = str(story.thumbnail_url if story.media_type == 1 else story.video_url)
        return self.story_download_by_url(url, filename, folder)

    def story_download_by_url(
        self, url: str, filename: str = "", folder: Path = ""
    ) -> Path:
        """
        Download story media using URL

        Parameters
        ----------
        url: str
            URL for a media
        filename: str, optional
            Filename for the media
        folder: Path, optional
            Directory in which you want to download the album, default is "" and will download the files to working
                directory

        Returns
        -------
        Path
            Path for the file downloaded
        """
        url = str(url)
        fname = urlparse(url).path.rsplit("/", 1)[1].strip()
        assert fname, (
            """The URL must contain the path to the file (mp4 or jpg).\n"""
            """Read the documentation https://subzeroid.github.io/instagrapi/usage-guide/story.html"""
        )
        filename = "%s.%s" % (filename, fname.rsplit(".", 1)[1]) if filename else fname
        path = Path(folder) / filename

        response = self._send_public_request(
            url, stream=True, timeout=self.request_timeout
        )
        response.raise_for_status()

        with open(path, "wb") as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)
        return path.resolve()

    def story_viewers(self, story_pk: int, amount: int = 0) -> List[UserShort]:
        """
        List of story viewers (Private API)

        Parameters
        ----------
        story_pk: int
        amount: int, optional
            Maximum number of story viewers

        Returns
        -------
        List[UserShort]
            A list of objects of UserShort
        """
        users = []
        next_max_id = None
        story_pk = self.media_pk(story_pk)
        params = {
            "supported_capabilities_new": json.dumps(config.SUPPORTED_CAPABILITIES)
        }
        while True:
            try:
                if next_max_id:
                    params["max_id"] = next_max_id
                result = self.private_request(
                    f"media/{story_pk}/list_reel_media_viewer/", params=params
                )
                for item in result["users"]:
                    users.append(extract_user_short(item))
                if amount and len(users) >= amount:
                    break
                next_max_id = result.get("next_max_id")
                if not next_max_id:
                    break
            except Exception as e:
                self.logger.exception(e)
                break
        if amount:
            users = users[: int(amount)]
        return users

    def story_like(self, story_id: str, revert: bool = False) -> bool:
        """
        Like a story

        Parameters
        ----------
        story_id: str
            Unique identifier of a Story
        revert: bool, optional
            If liked, whether or not to unlike. Default is False

        Returns
        -------
        bool
            A boolean value
        """
        assert self.user_id, "Login required"
        media_id = self.media_id(story_id)
        data = {
            "media_id": media_id,
            "_uid": str(self.user_id),
            "source_of_like": "button",
            "tray_session_id": self.tray_session_id,
            "viewer_session_id": self.client_session_id,
            "container_module": "reel_feed_timeline",
        }
        name = "unsend" if revert else "send"
        result = self.private_request(
            f"story_interactions/{name}_story_like", self.with_action_data(data)
        )
        return result["status"] == "ok"

    def story_unlike(self, story_id: str) -> bool:
        """
        Unlike a story

        Parameters
        ----------
        story_id: str
            Unique identifier of a Story

        Returns
        -------
        bool
            A boolean value
        """
        return self.story_like(story_id, revert=True)

    def sticker_tray(self) -> dict:
        """
        Getting a sticker tray from Instagram

        Returns
        -------
        dict
            Sticker Tray
        """
        data = {"_uid": self.user_id, "type": "static_stickers", "_uuid": self.uuid}
        result = self.private_request(
            "creatives/sticker_tray/",
            data=data,
            with_signature=True,
        )
        assert result["status"] == "ok"
        return result



================================================
FILE: instagrapi/mixins/timeline.py
================================================
from typing import List

from instagrapi.extractors import extract_media_v1
from instagrapi.types import Media


class ReelsMixin:
    """
    Helpers for Reels
    """

    def reels(self, amount: int = 10, last_media_pk: int = 0) -> List[Media]:
        """
        Get connected reels media

        Parameters
        ----------
        amount: int, optional
            Maximum number of media to return, default is 10
        last_media_pk: int, optional
            Last PK user has seen, function will return medias after this pk. Default is 0
        Returns
        -------
        List[Media]
            A list of objects of Media
        """
        return self.reels_timeline_media("reels", amount, last_media_pk)

    def explore_reels(self, amount: int = 10, last_media_pk: int = 0) -> List[Media]:
        """
        Get discover reels media

        Parameters
        ----------
        amount: int, optional
            Maximum number of media to return, default is 10
        last_media_pk: int, optional
            Last PK user has seen, function will return medias after this pk. Default is 0
        Returns
        -------
        List[Media]
            A list of objects of Media
        """
        return self.reels_timeline_media("explore_reels", amount, last_media_pk)

    def reels_timeline_media(
        self, collection_pk: str, amount: int = 10, last_media_pk: int = 0
    ) -> List[Media]:
        """
        Get reels timeline media in a collection

        Parameters
        ----------
        collection_pk: str
            Unique identifier of a timeline
        amount: int, optional
            Maximum number of media to return, default is 10
        last_media_pk: int, optional
            Last PK user has seen, function will return medias after this pk. Default is 0

        Returns
        -------
        List[Media]
            A list of objects of Media
        """

        if collection_pk == "reels":
            private_request_endpoint = "clips/connected/"
        elif collection_pk == "explore_reels":
            private_request_endpoint = "clips/discover/"

        last_media_pk = last_media_pk and int(last_media_pk)
        total_items = []
        next_max_id = ""
        while True:
            if len(total_items) >= float(amount):
                return total_items[:amount]
            try:
                result = self.private_request(
                    private_request_endpoint,
                    data=" ",
                    params={"max_id": next_max_id},
                )
            except Exception as e:
                self.logger.exception(e)
                return total_items

            for item in result["items"]:
                if last_media_pk and last_media_pk == item["media"]["pk"]:
                    return total_items
                total_items.append(extract_media_v1(item.get("media")))

            if not result.get("paging_info", {}).get("more_available"):
                return total_items

            next_max_id = result.get("paging_info", {}).get("more_available")



================================================
FILE: instagrapi/mixins/totp.py
================================================
import base64
import datetime
import hashlib
import hmac
import time
from typing import Any, List, Optional


class TOTP:
    """
    Base class for OTP handlers.
    """

    def __init__(
        self,
        s: str,
        digits: int = 6,
        digest: Any = hashlib.sha1,
        name: Optional[str] = None,
        issuer: Optional[str] = None,
    ) -> None:
        self.digits = digits
        self.digest = digest
        self.secret = s
        self.name = name or "Secret"
        self.issuer = issuer
        self.interval = 30

    def generate_otp(self, input: int) -> str:
        """
        :param input: the HMAC counter value to use as the OTP input.
        Usually either the counter, or the computed integer based on the Unix timestamp
        """
        if input < 0:
            raise ValueError("input must be positive integer")
        hasher = hmac.new(
            self.byte_secret(), self.int_to_bytestring(input), self.digest
        )
        hmac_hash = bytearray(hasher.digest())
        offset = hmac_hash[-1] & 0xF
        code = (
            (hmac_hash[offset] & 0x7F) << 24
            | (hmac_hash[offset + 1] & 0xFF) << 16
            | (hmac_hash[offset + 2] & 0xFF) << 8
            | (hmac_hash[offset + 3] & 0xFF)
        )
        str_code = str(code % 10**self.digits)
        while len(str_code) < self.digits:
            str_code = "0" + str_code
        return str_code

    def byte_secret(self) -> bytes:
        secret = self.secret
        missing_padding = len(secret) % 8
        if missing_padding != 0:
            secret += "=" * (8 - missing_padding)
        return base64.b32decode(secret, casefold=True)

    @staticmethod
    def int_to_bytestring(i: int, padding: int = 8) -> bytes:
        """
        Turns an integer to the OATH specified
        bytestring, which is fed to the HMAC
        along with the secret
        """
        result = bytearray()
        while i != 0:
            result.append(i & 0xFF)
            i >>= 8
            # It's necessary to convert the final result from bytearray to bytes
            # because the hmac functions in python 2.6 and 3.3 don't work with
            # bytearray
        return bytes(bytearray(reversed(result)).rjust(padding, b"\0"))

    def code(self):
        """
        Generate TOTP code
        """
        now = datetime.datetime.now()
        timecode = int(time.mktime(now.timetuple()) / self.interval)
        return self.generate_otp(timecode)


class TOTPMixin:
    def totp_generate_seed(self) -> str:
        """
        Generate 2FA TOTP seed

        Returns
        -------
        str
            TOTP seed (also known as "token" and "secret key")
        """
        result = self.private_request(
            "accounts/generate_two_factor_totp_key/", data=self.with_default_data({})
        )
        return result["totp_seed"]

    def totp_enable(self, verification_code: str) -> List[str]:
        """
        Enable TOTP 2FA

        Parameters
        ----------
        verification_code: str
            2FA verification code

        Returns
        -------
        List[str]
            Backup codes
        """
        result = self.private_request(
            "accounts/enable_totp_two_factor/",
            data=self.with_default_data({"verification_code": verification_code}),
        )
        return result["backup_codes"]

    def totp_disable(self) -> bool:
        """
        Disable TOTP 2FA

        Returns
        -------
        bool
        """
        result = self.private_request(
            "accounts/disable_totp_two_factor/", data=self.with_default_data({})
        )
        return result["status"] == "ok"

    def totp_generate_code(self, seed: str) -> str:
        """
        Generate 2FA TOTP code

        Parameters
        ----------
        seed: str
            TOTP seed (token, secret key)

        Returns
        -------
        str
            TOTP code
        """
        return TOTP(seed).code()



================================================
FILE: instagrapi/mixins/track.py
================================================
import shutil
from pathlib import Path
from typing import Any, Dict
from urllib.parse import urlparse

import requests

from instagrapi.exceptions import ClientError, TrackNotFound
from instagrapi.extractors import extract_track
from instagrapi.types import Track
from instagrapi.utils import json_value


class TrackMixin:
    def track_download_by_url(
        self, url: str, filename: str = "", folder: Path = ""
    ) -> Path:
        """
        Download track by URL

        Parameters
        ----------
        url: str
            URL for a track
        filename: str, optional
            Filename for the track
        folder: Path, optional
            Directory in which you want to download the track,
            default is "" and will download the files to working directory

        Returns
        -------
        Path
            Path for the file downloaded
        """
        url = str(url)
        fname = urlparse(url).path.rsplit("/", 1)[1].strip()
        assert fname, """The URL must contain the path to the file (m4a or mp3)."""
        filename = "%s.%s" % (filename, fname.rsplit(".", 1)[1]) if filename else fname
        path = Path(folder) / filename
        response = requests.get(url, stream=True, timeout=self.request_timeout)
        response.raise_for_status()
        with open(path, "wb") as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)
        return path.resolve()

    def _track_request(self, data: Dict[str, Any]) -> Dict:
        try:
            result = self.private_request("clips/music/", data)
        except ClientError as e:
            if not self.last_json:
                kw = {
                    k: v
                    for k, v in data.items()
                    if k in {"music_canonical_id", "original_sound_audio_asset_id"}
                }
                raise TrackNotFound(**kw)
            raise e
        return result

    def track_info_by_canonical_id(self, music_canonical_id: str) -> Track:
        """
        Get Track by music_canonical_id

        Parameters
        ----------
        music_canonical_id: str
            Unique identifier of the track

        Returns
        -------
        Track
            An object of Track type
        """
        data = {
            "tab_type": "clips",
            "referrer_media_id": "",
            "_uuid": self.uuid,
            "music_canonical_id": str(music_canonical_id),
        }
        result = self.private_request("clips/music/", data)
        track = json_value(result, "metadata", "music_info", "music_asset_info")
        return extract_track(track)

    def track_info_by_id(self, track_id: str, max_id: str = "") -> Dict:
        """
        Get Track by id

        Parameters
        ----------
        track_id: str
            Unique identifier of the track

        Returns
        -------
        Dict
            Raw insta response json
        """
        data = {
            "audio_cluster_id": track_id,
            "original_sound_audio_asset_id": track_id,
        }
        if max_id:
            data["max_id"] = max_id
        return self._track_request(data)



================================================
FILE: instagrapi/mixins/user.py
================================================
import json
from copy import deepcopy
from json.decoder import JSONDecodeError
from typing import Dict, List, Tuple

from instagrapi.exceptions import (
    ClientError,
    ClientJSONDecodeError,
    ClientLoginRequired,
    ClientNotFoundError,
    UserNotFound,
)
from instagrapi.extractors import extract_user_gql, extract_user_short, extract_user_v1
from instagrapi.types import Relationship, RelationshipShort, User, UserShort
from instagrapi.utils import json_value

MAX_USER_COUNT = 200
INFO_FROM_MODULES = ("self_profile", "feed_timeline", "reel_feed_timeline")

try:
    from typing import Literal

    INFO_FROM_MODULE = Literal[INFO_FROM_MODULES]
except Exception:
    INFO_FROM_MODULE = str


class UserMixin:
    """
    Helpers to manage user
    """

    _users_cache = {}  # user_pk -> User
    _userhorts_cache = {}  # user_pk -> UserShort
    _usernames_cache = {}  # username -> user_pk
    _users_following = {}  # user_pk -> dict(user_pk -> "short user object")
    _users_followers = {}  # user_pk -> dict(user_pk -> "short user object")

    def user_id_from_username(self, username: str) -> str:
        """
        Get full media id

        Parameters
        ----------
        username: str
            Username for an Instagram account

        Returns
        -------
        str
            User PK

        Example
        -------
        'example' -> 1903424587
        """
        username = str(username).lower()
        return str(self.user_info_by_username(username).pk)

    def user_short_gql(self, user_id: str, use_cache: bool = True) -> UserShort:
        """
        Get full media id

        Parameters
        ----------
        user_id: str
            User ID
        use_cache: bool, optional
            Whether or not to use information from cache, default value is True

        Returns
        -------
        UserShort
            An object of UserShort type
        """
        if use_cache:
            cache = self._userhorts_cache.get(user_id)
            if cache:
                return cache
        variables = {
            "user_id": str(user_id),
            "include_reel": True,
        }
        data = self.public_graphql_request(
            variables, query_hash="ad99dd9d3646cc3c0dda65debcd266a7"
        )
        if not data["user"]:
            raise UserNotFound(user_id=user_id, **data)
        user = extract_user_short(data["user"]["reel"]["user"])
        self._userhorts_cache[user_id] = user
        return user

    def username_from_user_id_gql(self, user_id: str) -> str:
        """
        Get username from user id

        Parameters
        ----------
        user_id: str
            User ID

        Returns
        -------
        str
            User name

        Example
        -------
        1903424587 -> 'example'
        """
        return self.user_short_gql(user_id).username

    def username_from_user_id(self, user_id: str) -> str:
        """
        Get username from user id

        Parameters
        ----------
        user_id: str
            User ID

        Returns
        -------
        str
            User name

        Example
        -------
        1903424587 -> 'example'
        """
        user_id = str(user_id)
        try:
            username = self.username_from_user_id_gql(user_id)
        except ClientError:
            username = self.user_info_v1(user_id).username
        return username

    def user_info_by_username_gql(self, username: str) -> User:
        """
        Get user object from user name

        Parameters
        ----------
        username: str
            User name of an instagram account

        Returns
        -------
        User
            An object of User type
        """
        username = str(username).lower()
        temporary_public_headers = {
            "Host": "www.instagram.com",
            "X-Requested-With": "XMLHttpRequest",
            "Sec-Ch-Prefers-Color-Scheme": "dark",
            "Sec-Ch-Ua-Platform": '"Linux"',
            "X-Ig-App-Id": "936619743392459",
            "Sec-Ch-Ua-Model": '""',
            "Sec-Ch-Ua-Mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36",
            "Accept": "*/*",
            "X-Asbd-Id": "129477",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://www.instagram.com/",
            "Accept-Language": "en-US,en;q=0.9",
            "Priority": "u=1, i",
        }
        data = extract_user_gql(
            json.loads(
                self.public_request(
                    f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}",
                    headers=temporary_public_headers,
                    update_headers=False,
                )
            )["data"]["user"]
        )
        return data

    def user_info_by_username_v1(self, username: str) -> User:
        """
        Get user object from user name

        Parameters
        ----------
        username: str
            User name of an instagram account

        Returns
        -------
        User
            An object of User type
        """
        username = str(username).lower()
        try:
            result = self.private_request(f"users/{username}/usernameinfo/")
        except ClientNotFoundError as e:
            raise UserNotFound(e, username=username, **self.last_json)
        except ClientError as e:
            if "User not found" in str(e):
                raise UserNotFound(e, username=username, **self.last_json)
            raise e
        return extract_user_v1(result["user"])

    def user_info_by_username(self, username: str, use_cache: bool = True) -> User:
        """
        Get user object from username

        Parameters
        ----------
        username: str
            User name of an instagram account
        use_cache: bool, optional
            Whether or not to use information from cache, default value is True

        Returns
        -------
        User
            An object of User type
        """
        username = str(username).lower()
        if not use_cache or username not in self._usernames_cache:
            try:
                try:
                    user = self.user_info_by_username_gql(username)
                except ClientLoginRequired as e:
                    if not self.inject_sessionid_to_public():
                        raise e
                    user = self.user_info_by_username_gql(username)  # retry
            except Exception as e:
                if not isinstance(e, ClientError):
                    self.logger.exception(e)  # Register unknown error
                user = self.user_info_by_username_v1(username)
            self._users_cache[user.pk] = user
            self._usernames_cache[user.username] = user.pk
        return self.user_info(self._usernames_cache[username])

    def user_info_gql(self, user_id: str) -> User:
        """
        Get user object from user id

        Parameters
        ----------
        user_id: str
            User id of an instagram account

        Returns
        -------
        User
            An object of User type
        """
        user_id = str(user_id)
        try:
            # GraphQL haven't method to receive user by id
            return self.user_info_by_username_gql(
                self.username_from_user_id_gql(user_id)
            )
        except JSONDecodeError as e:
            raise ClientJSONDecodeError(e, user_id=user_id)

    def user_info_v1(
        self,
        user_id: str,
        from_module: INFO_FROM_MODULE = "self_profile",
        is_app_start: bool = False,
    ) -> User:
        """
        Get user object from user id

        Parameters
        ----------
        user_id: str
            User id of an instagram account
        from_module: str
            Which module triggered request: self_profile, feed_timeline, reel_feed_timeline. Default: self_profile
        is_app_start: bool
            Boolean value specifying if profile is being retrieved on app launch

        Returns
        -------
        User
            An object of User type
        """
        user_id = str(user_id)
        try:
            params = {
                "is_prefetch": "false",
                "entry_point": "self_profile",
                "from_module": from_module,
                "is_app_start": is_app_start,
            }
            assert (
                from_module in INFO_FROM_MODULES
            ), f'Unsupported send_attribute="{from_module}" {INFO_FROM_MODULES}'
            if from_module != "self_profile":
                params["entry_point"] = "profile"

            result = self.private_request(f"users/{user_id}/info/", params=params)
        except ClientNotFoundError as e:
            raise UserNotFound(e, user_id=user_id, **self.last_json)
        except ClientError as e:
            if "User not found" in str(e):
                raise UserNotFound(e, user_id=user_id, **self.last_json)
            raise e
        return extract_user_v1(result["user"])

    def user_info(self, user_id: str, use_cache: bool = True) -> User:
        """
        Get user object from user id

        Parameters
        ----------
        user_id: str
            User id of an instagram account
        use_cache: bool, optional
            Whether or not to use information from cache, default value is True

        Returns
        -------
        User
            An object of User type
        """
        user_id = str(user_id)
        if not use_cache or user_id not in self._users_cache:
            try:
                try:
                    user = self.user_info_gql(user_id)
                except ClientLoginRequired as e:
                    if not self.inject_sessionid_to_public():
                        raise e
                    user = self.user_info_gql(user_id)  # retry
            except Exception as e:
                if not isinstance(e, ClientError):
                    self.logger.exception(e)
                user = self.user_info_v1(user_id)
            self._users_cache[user_id] = user
            self._usernames_cache[user.username] = user.pk
        return deepcopy(
            self._users_cache[user_id]
        )  # return copy of cache (dict changes protection)

    def new_feed_exist(self) -> bool:
        """
        Returns bool
        -------
        Check if new feed exist
        -------
        True if new feed exist ,
        After Login or load Settings always return False
        """
        results = self.private_request("feed/new_feed_posts_exist/")
        return results.get("new_feed_posts_exist", False)

    def user_friendships_v1(self, user_ids: List[str]) -> List[RelationshipShort]:
        """
        Get user friendship status

        Parameters
        ----------
        user_ids: List[str]
            List of user ID of an instagram account

        Returns
        -------
        List[RelationshipShort]
           List of RelationshipShorts with requested user_ids
        """
        user_ids_str = ",".join(user_ids)
        result = self.private_request(
            "friendships/show_many/",
            data={"user_ids": user_ids_str, "_uuid": self.uuid},
            with_signature=False,
        )
        assert result.get("status", "") == "ok"

        relationships = []
        for user_id, status in result.get("friendship_statuses", {}).items():
            relationships.append(RelationshipShort(user_id=user_id, **status))

        return relationships

    def user_friendship_v1(self, user_id: str) -> Relationship:
        """
        Get user friendship status

        Parameters
        ----------
        user_id: str
            User id of an instagram account

        Returns
        -------
        Relationship
            An object of Relationship type
        """

        try:
            params = {
                "is_external_deeplink_profile_view": "false",
            }
            result = self.private_request(f"friendships/show/{user_id}/", params=params)
            assert result.get("status", "") == "ok"

            return Relationship(user_id=user_id, **result)
        except ClientError as e:
            self.logger.exception(e)
            return None

    def search_users_v1(self, query: str, count: int) -> List[UserShort]:
        """
        Search users by a query (Private Mobile API)
        Parameters
        ----------
        query: str
            Query to search
        count: int
            The count of search results
        Returns
        -------
        List[UserShort]
            List of users
        """
        results = self.private_request(
            "users/search/", params={"query": query, "count": count}
        )
        users = results.get("users", [])
        return [extract_user_short(user) for user in users]

    def search_users(self, query: str, count: int = 50) -> List[UserShort]:
        """
        Search users by a query
        Parameters
        ----------
        query: str
            Query string to search
        count: int
            The count of search results
        Returns
        -------
        List[UserShort]
            List of User short object
        """
        return self.search_users_v1(query, count)

    def search_followers_v1(self, user_id: str, query: str) -> List[UserShort]:
        """
        Search users by followers (Private Mobile API)

        Parameters
        ----------
        user_id: str
            User id of an instagram account
        query: str
            Query to search

        Returns
        -------
        List[UserShort]
            List of users
        """
        results = self.private_request(
            f"friendships/{user_id}/followers/",
            params={
                "search_surface": "follow_list_page",
                "query": query,
                "enable_groups": "true",
            },
        )
        users = results.get("users", [])
        return [extract_user_short(user) for user in users]

    def search_followers(self, user_id: str, query: str) -> List[UserShort]:
        """
        Search by followers

        Parameters
        ----------
        user_id: str
            User id of an instagram account
        query: str
            Query string

        Returns
        -------
        List[UserShort]
            List of User short object
        """
        return self.search_followers_v1(user_id, query)

    def search_following_v1(self, user_id: str, query: str) -> List[UserShort]:
        """
        Search following users (Private Mobile API)

        Parameters
        ----------
        user_id: str
            User id of an instagram account
        query: str
            Query to search

        Returns
        -------
        List[UserShort]
            List of users
        """
        results = self.private_request(
            f"friendships/{user_id}/following/",
            params={
                "includes_hashtags": "false",
                "search_surface": "follow_list_page",
                "query": query,
                "enable_groups": "true",
            },
        )
        users = results.get("users", [])
        return [extract_user_short(user) for user in users]

    def search_following(self, user_id: str, query: str) -> List[UserShort]:
        """
        Search by following

        Parameters
        ----------
        user_id: str
            User id of an instagram account
        query: str
            Query string

        Returns
        -------
        List[UserShort]
            List of User short object
        """
        return self.search_following_v1(user_id, query)

    def user_following_gql(self, user_id: str, amount: int = 0) -> List[UserShort]:
        """
        Get user's following users information by Public Graphql API

        Parameters
        ----------
        user_id: str
            User id of an instagram account
        amount: int, optional
            Maximum number of media to return, default is 0

        Returns
        -------
        List[UserShort]
            List of objects of User type
        """
        user_id = str(user_id)
        end_cursor = None
        users = []
        variables = {
            "id": user_id,
            "include_reel": True,
            "fetch_mutual": False,
            "first": 24,
        }
        self.inject_sessionid_to_public()
        while True:
            if end_cursor:
                variables["after"] = end_cursor
            data = self.public_graphql_request(
                variables, query_hash="58712303d941c6855d4e888c5f0cd22f"
            )
            if not data["user"] and not users:
                raise UserNotFound(user_id=user_id, **data)
            page_info = json_value(data, "user", "edge_follow", "page_info", default={})
            edges = json_value(data, "user", "edge_follow", "edges", default=[])
            for edge in edges:
                users.append(extract_user_short(edge["node"]))
            end_cursor = page_info.get("end_cursor")
            if not page_info.get("has_next_page") or not end_cursor:
                break
            if amount and len(users) >= amount:
                break
            # time.sleep(sleep)
        if amount:
            users = users[:amount]
        return users

    def user_following_v1_chunk(
        self, user_id: str, max_amount: int = 0, max_id: str = ""
    ) -> Tuple[List[UserShort], str]:
        """
        Get user's following users information by Private Mobile API and max_id (cursor)

        Parameters
        ----------
        user_id: str
            User id of an instagram account
        max_amount: int, optional
            Maximum number of media to return, default is 0 - Inf
        max_id: str, optional
            Max ID, default value is empty String

        Returns
        -------
        Tuple[List[UserShort], str]
            Tuple of List of users and max_id
        """
        unique_set = set()
        users = []
        while True:
            result = self.private_request(
                f"friendships/{user_id}/following/",
                params={
                    "max_id": max_id,
                    "count": max_amount or MAX_USER_COUNT,
                    "rank_token": self.rank_token,
                    "search_surface": "follow_list_page",
                    "query": "",
                    "enable_groups": "true",
                },
            )
            for user in result["users"]:
                user = extract_user_short(user)
                if user.pk in unique_set:
                    continue
                unique_set.add(user.pk)
                users.append(user)
            max_id = result.get("next_max_id")
            if not max_id or (max_amount and len(users) >= max_amount):
                break
        return users, max_id

    def user_following_v1(self, user_id: str, amount: int = 0) -> List[UserShort]:
        """
        Get user's following users formation by Private Mobile API

        Parameters
        ----------
        user_id: str
            User id of an instagram account
        amount: int, optional
            Maximum number of media to return, default is 0 - Inf

        Returns
        -------
        List[UserShort]
            List of objects of User type
        """
        users, _ = self.user_following_v1_chunk(str(user_id), amount)
        if amount:
            users = users[:amount]
        return users

    def user_following(
        self, user_id: str, use_cache: bool = True, amount: int = 0
    ) -> Dict[str, UserShort]:
        """
        Get user's following information

        Parameters
        ----------
        user_id: str
            User id of an instagram account
        use_cache: bool, optional
            Whether or not to use information from cache, default value is True
        amount: int, optional
            Maximum number of media to return, default is 0

        Returns
        -------
        Dict[str, UserShort]
            Dict of user_id and User object
        """
        user_id = str(user_id)
        users = self._users_following.get(user_id, {})
        if not use_cache or not users or (amount and len(users) < amount):
            # Temporary: Instagram Required Login for GQL request
            # You can inject sessionid from private to public session
            # try:
            #     users = self.user_following_gql(user_id, amount)
            # except Exception as e:
            #     if not isinstance(e, ClientError):
            #         self.logger.exception(e)
            #     users = self.user_following_v1(user_id, amount)
            users = self.user_following_v1(user_id, amount)
            self._users_following[user_id] = {user.pk: user for user in users}
        following = self._users_following[user_id]
        if amount and len(following) > amount:
            following = dict(list(following.items())[:amount])
        return following

    def user_followers_gql_chunk(
        self, user_id: str, max_amount: int = 0, end_cursor: str = None
    ) -> Tuple[List[UserShort], str]:
        """
        Get user's followers information by Public Graphql API and end_cursor

        Parameters
        ----------
        user_id: str
            User id of an instagram account
        max_amount: int, optional
            Maximum number of media to return, default is 0 - Inf
        end_cursor: str, optional
            The cursor from which it is worth continuing to receive the list of followers

        Returns
        -------
        Tuple[List[UserShort], str]
            List of objects of User type with cursor
        """
        user_id = str(user_id)
        users = []
        variables = {
            "id": user_id,
            "include_reel": True,
            "fetch_mutual": False,
            "first": 12,
        }
        self.inject_sessionid_to_public()
        while True:
            if end_cursor:
                variables["after"] = end_cursor
            data = self.public_graphql_request(
                variables, query_hash="37479f2b8209594dde7facb0d904896a"
            )
            if not data["user"] and not users:
                raise UserNotFound(user_id=user_id, **data)
            page_info = json_value(
                data, "user", "edge_followed_by", "page_info", default={}
            )
            edges = json_value(data, "user", "edge_followed_by", "edges", default=[])
            for edge in edges:
                users.append(extract_user_short(edge["node"]))
            end_cursor = page_info.get("end_cursor")
            if not page_info.get("has_next_page") or not end_cursor:
                break
            if max_amount and len(users) >= max_amount:
                break
        return users, end_cursor

    def user_followers_gql(self, user_id: str, amount: int = 0) -> List[UserShort]:
        """
        Get user's followers information by Public Graphql API

        Parameters
        ----------
        user_id: str
            User id of an instagram account
        amount: int, optional
            Maximum number of media to return, default is 0 - Inf

        Returns
        -------
        List[UserShort]
            List of objects of User type
        """
        users, _ = self.user_followers_gql_chunk(str(user_id), amount)
        if amount:
            users = users[:amount]
        return users

    def user_followers_v1_chunk(
        self, user_id: str, max_amount: int = 0, max_id: str = ""
    ) -> Tuple[List[UserShort], str]:
        """
        Get user's followers information by Private Mobile API and max_id (cursor)

        Parameters
        ----------
        user_id: str
            User id of an instagram account
        max_amount: int, optional
            Maximum number of media to return, default is 0 - Inf
        max_id: str, optional
            Max ID, default value is empty String

        Returns
        -------
        Tuple[List[UserShort], str]
            Tuple of List of users and max_id
        """
        unique_set = set()
        users = []
        while True:
            result = self.private_request(
                f"friendships/{user_id}/followers/",
                params={
                    "max_id": max_id,
                    "count": max_amount or MAX_USER_COUNT,
                    "rank_token": self.rank_token,
                    "search_surface": "follow_list_page",
                    "query": "",
                    "enable_groups": "true",
                },
            )
            for user in result["users"]:
                user = extract_user_short(user)
                if user.pk in unique_set:
                    continue
                unique_set.add(user.pk)
                users.append(user)
            max_id = result.get("next_max_id")
            if not max_id or (max_amount and len(users) >= max_amount):
                break
        return users, max_id

    def user_followers_v1(self, user_id: str, amount: int = 0) -> List[UserShort]:
        """
        Get user's followers information by Private Mobile API

        Parameters
        ----------
        user_id: str
            User id of an instagram account
        amount: int, optional
            Maximum number of media to return, default is 0 - Inf

        Returns
        -------
        List[UserShort]
            List of objects of User type
        """
        users, _ = self.user_followers_v1_chunk(str(user_id), amount)
        if amount:
            users = users[:amount]
        return users

    def user_followers(
        self, user_id: str, use_cache: bool = True, amount: int = 0
    ) -> Dict[str, UserShort]:
        """
        Get user's followers

        Parameters
        ----------
        user_id: str
            User id of an instagram account
        use_cache: bool, optional
            Whether or not to use information from cache, default value is True
        amount: int, optional
            Maximum number of media to return, default is 0 - Inf

        Returns
        -------
        Dict[str, UserShort]
            Dict of user_id and User object
        """
        user_id = str(user_id)
        users = self._users_followers.get(user_id, {})
        if not use_cache or not users or (amount and len(users) < amount):
            try:
                users = self.user_followers_gql(user_id, amount)
            except Exception as e:
                if not isinstance(e, ClientError):
                    self.logger.exception(e)
                users = self.user_followers_v1(user_id, amount)
            self._users_followers[user_id] = {user.pk: user for user in users}
        followers = self._users_followers[user_id]
        if amount and len(followers) > amount:
            followers = dict(list(followers.items())[:amount])
        return followers

    def user_follow(self, user_id: str) -> bool:
        """
        Follow a user

        Parameters
        ----------
        user_id: str

        Returns
        -------
        bool
            A boolean value
        """
        assert self.user_id, "Login required"
        user_id = str(user_id)
        if user_id in self._users_following.get(self.user_id, []):
            self.logger.debug("User %s already followed", user_id)
            return False
        data = self.with_action_data({"user_id": user_id})
        result = self.private_request(f"friendships/create/{user_id}/", data)
        if self.user_id in self._users_following:
            self._users_following.pop(self.user_id)  # reset
        return result["friendship_status"]["following"] is True

    def user_unfollow(self, user_id: str) -> bool:
        """
        Unfollow a user

        Parameters
        ----------
        user_id: str

        Returns
        -------
        bool
            A boolean value
        """
        assert self.user_id, "Login required"
        user_id = str(user_id)
        data = self.with_action_data({"user_id": user_id})
        result = self.private_request(f"friendships/destroy/{user_id}/", data)
        if self.user_id in self._users_following:
            self._users_following[self.user_id].pop(user_id, None)
        return result["friendship_status"]["following"] is False

    def user_block(self, user_id: str, surface: str = "profile") -> bool:
        """
        Block a User

        Parameters
        ----------
        user_id: str
            User ID of an Instagram account
        surface: str, (optional)
            Surface of block (deafult "profile", also can be "direct_thread_info")

        Returns
        -------
        bool
            A boolean value
        """
        data = {
            "surface": surface,
            "is_auto_block_enabled": "false",
            "user_id": user_id,
            "_uid": self.user_id,
            "_uuid": self.uuid,
        }
        if surface == "direct_thread_info":
            data["client_request_id"] = self.request_id

        result = self.private_request(f"friendships/block/{user_id}/", data)
        assert result.get("status", "") == "ok"

        return result.get("friendship_status", {}).get("blocking") is True

    def user_unblock(self, user_id: str, surface: str = "profile") -> bool:
        """
        Unlock a User

        Parameters
        ----------
        user_id: str
            User ID of an Instagram account
        surface: str, (optional)
            Surface of block (deafult "profile", also can be "direct_thread_info")

        Returns
        -------
        bool
            A boolean value
        """
        data = {
            "container_module": surface,
            "user_id": user_id,
            "_uid": self.user_id,
            "_uuid": self.uuid,
        }
        if surface == "direct_thread_info":
            data["client_request_id"] = self.request_id

        result = self.private_request(f"friendships/unblock/{user_id}/", data)
        assert result.get("status", "") == "ok"

        return result.get("friendship_status", {}).get("blocking") is False

    def user_remove_follower(self, user_id: str) -> bool:
        """
        Remove a follower

        Parameters
        ----------
        user_id: str

        Returns
        -------
        bool
            A boolean value
        """
        assert self.user_id, "Login required"
        user_id = str(user_id)
        data = self.with_action_data({"user_id": str(user_id)})
        result = self.private_request(f"friendships/remove_follower/{user_id}/", data)
        if self.user_id in self._users_followers:
            self._users_followers[self.user_id].pop(user_id, None)
        return result["friendship_status"]["followed_by"] is False

    def mute_posts_from_follow(self, user_id: str, revert: bool = False) -> bool:
        """
        Mute posts from following user

        Parameters
        ----------
        user_id: str
            Unique identifier of a User
        revert: bool, optional
            Unmute when True

        Returns
        -------
        bool
            A boolean value
        """
        user_id = str(user_id)
        name = "unmute" if revert else "mute"
        result = self.private_request(
            f"friendships/{name}_posts_or_story_from_follow/",
            {
                # "media_id": media_pk,  # when feed_timeline
                "target_posts_author_id": str(user_id),
                "container_module": "media_mute_sheet",  # or "feed_timeline"
            },
        )
        return result["status"] == "ok"

    def unmute_posts_from_follow(self, user_id: str) -> bool:
        """
        Unmute posts from following user

        Parameters
        ----------
        user_id: str
            Unique identifier of a User

        Returns
        -------
        bool
            A boolean value
        """
        return self.mute_posts_from_follow(user_id, True)

    def mute_stories_from_follow(self, user_id: str, revert: bool = False) -> bool:
        """
        Mute stories from following user

        Parameters
        ----------
        user_id: str
            Unique identifier of a User
        revert: bool, optional
            Unmute when True

        Returns
        -------
        bool
            A boolean value
        """
        user_id = str(user_id)
        name = "unmute" if revert else "mute"
        result = self.private_request(
            f"friendships/{name}_posts_or_story_from_follow/",
            {
                # "media_id": media_pk,  # when feed_timeline
                "target_reel_author_id": str(user_id),
                "container_module": "media_mute_sheet",  # or "feed_timeline"
            },
        )
        return result["status"] == "ok"

    def unmute_stories_from_follow(self, user_id: str) -> bool:
        """
        Unmute stories from following user

        Parameters
        ----------
        user_id: str
            Unique identifier of a User

        Returns
        -------
        bool
            A boolean value
        """
        return self.mute_stories_from_follow(user_id, True)

    def enable_posts_notifications(self, user_id: str, disable: bool = False) -> bool:
        """
        Enable post notifications of a user

        Parameters
        ----------
        user_id: str
            Unique identifier of a User
        disable: bool, optional
            Unfavorite when True

        Returns
        -------
        bool
            A boolean value
        """
        assert self.user_id, "Login required"
        user_id = str(user_id)
        data = self.with_action_data({"user_id": user_id, "_uid": self.user_id})
        name = "unfavorite" if disable else "favorite"
        result = self.private_request(f"friendships/{name}/{user_id}/", data)
        return result["status"] == "ok"

    def disable_posts_notifications(self, user_id: str) -> bool:
        """
        Disable post notifications of a user

        Parameters
        ----------
        user_id: str
            Unique identifier of a User
        Returns
        -------
        bool
            A boolean value
        """
        return self.enable_posts_notifications(user_id, True)

    def enable_videos_notifications(self, user_id: str, revert: bool = False) -> bool:
        """
        Enable videos notifications of a user

        Parameters
        ----------
        user_id: str
            Unique identifier of a User
        revert: bool, optional
            Unfavorite when True

        Returns
        -------
        bool
        A boolean value
        """
        assert self.user_id, "Login required"
        user_id = str(user_id)
        data = self.with_action_data({"user_id": user_id, "_uid": self.user_id})
        name = "unfavorite" if revert else "favorite"
        result = self.private_request(f"friendships/{name}_for_igtv/{user_id}/", data)
        return result["status"] == "ok"

    def disable_videos_notifications(self, user_id: str) -> bool:
        """
        Disable videos notifications of a user

        Parameters
        ----------
        user_id: str
            Unique identifier of a User
        Returns
        -------
        bool
            A boolean value
        """
        return self.enable_videos_notifications(user_id, True)

    def enable_reels_notifications(self, user_id: str, revert: bool = False) -> bool:
        """
        Enable reels notifications of a user

        Parameters
        ----------
        user_id: str
            Unique identifier of a User
        revert: bool, optional
            Unfavorite when True

        Returns
        -------
        bool
        A boolean value
        """
        assert self.user_id, "Login required"
        user_id = str(user_id)
        data = self.with_action_data({"user_id": user_id, "_uid": self.user_id})
        name = "unfavorite" if revert else "favorite"
        result = self.private_request(f"friendships/{name}_for_clips/{user_id}/", data)
        return result["status"] == "ok"

    def disable_reels_notifications(self, user_id: str) -> bool:
        """
        Disable reels notifications of a user

        Parameters
        ----------
        user_id: str
            Unique identifier of a User
        Returns
        -------
        bool
            A boolean value
        """
        return self.enable_reels_notifications(user_id, True)

    def enable_stories_notifications(self, user_id: str, revert: bool = False) -> bool:
        """
        Enable stories notifications of a user

        Parameters
        ----------
        user_id: str
            Unique identifier of a User
        revert: bool, optional
            Unfavorite when True

        Returns
        -------
        bool
        A boolean value
        """
        assert self.user_id, "Login required"
        user_id = str(user_id)
        data = self.with_action_data({"user_id": user_id, "_uid": self.user_id})
        name = "unfavorite" if revert else "favorite"
        result = self.private_request(
            f"friendships/{name}_for_stories/{user_id}/", data
        )
        return result["status"] == "ok"

    def disable_stories_notifications(self, user_id: str) -> bool:
        """
        Disable stories notifications of a user

        Parameters
        ----------
        user_id: str
            Unique identifier of a User
        Returns
        -------
        bool
            A boolean value
        """
        return self.enable_stories_notifications(user_id, True)

    def close_friend_add(self, user_id: str):
        """
        Add to Close Friends List

        Parameters
        ----------
        user_id: str
            Unique identifier of a User
        Returns
        -------
        bool
            A boolean value
        """
        assert self.user_id, "Login required"
        user_id = str(user_id)
        data = {
            "block_on_empty_thread_creation": "false",
            "module": "CLOSE_FRIENDS_V2_SEARCH",
            "source": "audience_manager",
            "_uid": self.user_id,
            "_uuid": self.uuid,
            "remove": [],
            "add": [user_id],
        }
        result = self.private_request("friendships/set_besties/", data)
        return json_value(result, "friendship_statuses", user_id, "is_bestie")

    def close_friend_remove(self, user_id: str):
        """
        Remove from Close Friends List

        Parameters
        ----------
        user_id: str
            Unique identifier of a User
        Returns
        -------
        bool
            A boolean value
        """
        assert self.user_id, "Login required"
        user_id = str(user_id)
        data = {
            "block_on_empty_thread_creation": "false",
            "module": "CLOSE_FRIENDS_V2_SEARCH",
            "source": "audience_manager",
            "_uid": self.user_id,
            "_uuid": self.uuid,
            "remove": [user_id],
            "add": [],
        }
        result = self.private_request("friendships/set_besties/", data)
        return json_value(result, "friendship_statuses", user_id, "is_bestie") is False

    def creator_info(
        self, user_id: str, entry_point: str = "direct_thread"
    ) -> Tuple[UserShort, Dict]:
        """
        Retrieves Creator's information

        Parameters
        ----------
        user_id: str
            Unique identifier of a User
        entry_point: str, optional
            Entry point for retrieving, default - direct_thread
            When passing self_profile, own user_id must be provided

        Returns
        -------
        Tuple[UserShort, Dict]
            Retrieved User and his Creator's Info
        """
        assert self.user_id, "Login required"
        params = {
            "entry_point": entry_point,
            "surface_type": "android",
            "user_id": user_id,
        }

        result = self.private_request("creator/creator_info/", params=params)
        assert result.get("status", "") == "ok"

        creator_info = result.get("user", {}).pop("creator_info", {})
        user = extract_user_short(result.get("user", {}))
        return (user, creator_info)



================================================
FILE: instagrapi/mixins/video.py
================================================
import random
import time
from pathlib import Path
from typing import Dict, List
from urllib.parse import urlparse
from uuid import uuid4

import requests

from instagrapi import config
from instagrapi.exceptions import (
    VideoConfigureError,
    VideoConfigureStoryError,
    VideoNotDownload,
    VideoNotUpload,
)
from instagrapi.extractors import extract_direct_message, extract_media_v1
from instagrapi.types import (
    DirectMessage,
    Location,
    Media,
    Story,
    StoryHashtag,
    StoryLink,
    StoryLocation,
    StoryMedia,
    StoryMention,
    StoryPoll,
    StorySticker,
    Usertag,
)
from instagrapi.utils import date_time_original, dumps


class DownloadVideoMixin:
    """
    Helpers for downloading video
    """

    def video_download(self, media_pk: int, folder: Path = "") -> Path:
        """
        Download video using media pk

        Parameters
        ----------
        media_pk: int
            Unique Media ID
        folder: Path, optional
            Directory in which you want to download the video, default is "" and will download the files to working dir.

        Returns
        -------
        Path
            Path for the file downloaded
        """
        media = self.media_info(media_pk)
        assert media.media_type == 2, "Must been video"
        filename = "{username}_{media_pk}".format(
            username=media.user.username, media_pk=media_pk
        )
        return self.video_download_by_url(media.video_url, filename, folder)

    def video_download_by_url(
        self, url: str, filename: str = "", folder: Path = ""
    ) -> Path:
        """
        Download video using URL

        Parameters
        ----------
        url: str
            URL for a media
        filename: str, optional
            Filename for the media
        folder: Path, optional
            Directory in which you want to download the video, default is "" and will download the files to working
                directory

        Returns
        -------
        Path
            Path for the file downloaded
        """
        url = str(url)
        fname = urlparse(url).path.rsplit("/", 1)[1]
        filename = "%s.%s" % (filename, fname.rsplit(".", 1)[1]) if filename else fname
        path = Path(folder) / filename
        response = requests.get(url, stream=True, timeout=self.request_timeout)
        response.raise_for_status()
        try:
            content_length = int(response.headers.get("Content-Length"))
        except TypeError:
            print(
                """
                The program detected an mis-formatted link, and hence can't download it.
                This problem occurs when the URL is passed into
                    'video_download_by_url()' or the 'clip_download_by_url()'.
                The raw URL needs to be re-formatted into one that is recognizable by the methods.
                Use this code: url=self.cl.media_info(self.cl.media_pk_from_url('insert the url here')).video_url
                You can remove the 'self' from the code above if needed.
                """
            )
            raise Exception("The program detected an mis-formatted link.")
        file_length = len(response.content)
        if content_length != file_length:
            raise VideoNotDownload(
                f'Broken file "{path}" (Content-length={content_length}, but file length={file_length})'
            )
        with open(path, "wb") as f:
            f.write(response.content)
            f.close()
        return path.resolve()

    def video_download_by_url_origin(self, url: str) -> bytes:
        """
        Download video using URL

        Parameters
        ----------
        url: str
            URL for a media

        Returns
        -------
        bytes
            Bytes for the file downloaded
        """
        response = requests.get(url, stream=True, timeout=self.request_timeout)
        response.raise_for_status()
        content_length = int(response.headers.get("Content-Length"))
        file_length = len(response.content)
        if content_length != file_length:
            raise VideoNotDownload(
                f'Broken file from url "{url}" (Content-length={content_length}, but file length={file_length})'
            )
        return response.content


class UploadVideoMixin:
    """
    Helpers for downloading video
    """

    def video_rupload(
        self,
        path: Path,
        thumbnail: Path = None,
        to_album: bool = False,
        to_story: bool = False,
        to_direct: bool = False,
    ) -> tuple:
        """
        Upload video to Instagram

        Parameters
        ----------
        path: Path
            Path to the media
        thumbnail: str
            Path to thumbnail for video. When None, then thumbnail is generate automatically
        to_album: bool, optional
        to_story: bool, optional
        to_direct: bool, optional

        Returns
        -------
        tuple
            (Upload ID for the media, width, height)
        """
        assert isinstance(path, Path), f"Path must been Path, now {path} ({type(path)})"
        upload_id = str(int(time.time() * 1000))
        width, height, duration, thumbnail = analyze_video(path, thumbnail)
        waterfall_id = str(uuid4())
        # upload_name example: '1576102477530_0_7823256191'
        upload_name = "{upload_id}_0_{rand}".format(
            upload_id=upload_id, rand=random.randint(1000000000, 9999999999)
        )
        rupload_params = {
            "retry_context": '{"num_step_auto_retry":0,"num_reupload":0,"num_step_manual_retry":0}',
            "media_type": "2",
            "xsharing_user_ids": dumps([self.user_id]),
            "upload_id": upload_id,
            "upload_media_duration_ms": str(int(duration * 1000)),
            "upload_media_width": str(width),
            "upload_media_height": str(height),  # "1138" for Mi5s
        }
        if to_direct:
            rupload_params["direct_v2"] = "1"
            # "hflip": "false",
            # "rotate":"3",
        if to_album:
            rupload_params["is_sidecar"] = "1"
        if to_story:
            rupload_params = {
                "extract_cover_frame": "1",
                "content_tags": "has-overlay",
                "for_album": "1",
                **rupload_params,
            }
        headers = {
            "Accept-Encoding": "gzip, deflate",
            "X-Instagram-Rupload-Params": dumps(rupload_params),
            "X_FB_VIDEO_WATERFALL_ID": waterfall_id,
            # "X_FB_VIDEO_WATERFALL_ID": "88732215909430_55CF262450C9_Mixed_0",  # ALBUM
            # "X_FB_VIDEO_WATERFALL_ID": "1594919079102",  # VIDEO
        }
        if to_album:
            headers = {"Segment-Start-Offset": "0", "Segment-Type": "3", **headers}
        response = self.private.get(
            "https://{domain}/rupload_igvideo/{name}".format(
                domain=config.API_DOMAIN, name=upload_name
            ),
            headers=headers,
        )
        self.request_log(response)
        if response.status_code != 200:
            raise VideoNotUpload(response.text, response=response, **self.last_json)
        with open(path, "rb") as fp:
            video_data = fp.read()
            video_len = str(len(video_data))
        headers = {
            "Offset": "0",
            "X-Entity-Name": upload_name,
            "X-Entity-Length": video_len,
            "Content-Type": "application/octet-stream",
            "Content-Length": video_len,
            "X-Entity-Type": "video/mp4",
            **headers,
        }
        response = self.private.post(
            "https://{domain}/rupload_igvideo/{name}".format(
                domain=config.API_DOMAIN, name=upload_name
            ),
            data=video_data,
            headers=headers,
        )
        self.request_log(response)
        if response.status_code != 200:
            raise VideoNotUpload(response.text, response=response, **self.last_json)
        return upload_id, width, height, duration, Path(thumbnail)

    def video_upload(
        self,
        path: Path,
        caption: str,
        thumbnail: Path = None,
        usertags: List[Usertag] = [],
        location: Location = None,
        extra_data: Dict[str, str] = {},
    ) -> Media:
        """
        Upload video and configure to feed

        Parameters
        ----------
        path: Path
            Path to the media
        caption: str
            Media caption
        thumbnail: str
            Path to thumbnail for video. When None, then thumbnail is generate automatically
        usertags: List[Usertag], optional
            List of users to be tagged on this upload, default is empty list.
        location: Location, optional
            Location tag for this upload, default is None
        extra_data: Dict[str, str], optional
            Dict of extra data, if you need to add your params, like {"share_to_facebook": 1}.

        Returns
        -------
        Media
            An object of Media class
        """
        path = Path(path)
        if thumbnail is not None:
            thumbnail = Path(thumbnail)
        upload_id, width, height, duration, thumbnail = self.video_rupload(
            path, thumbnail, to_story=False
        )
        for attempt in range(50):
            self.logger.debug(f"Attempt #{attempt} to configure Video: {path}")
            time.sleep(3)
            try:
                configured = self.video_configure(
                    upload_id,
                    width,
                    height,
                    duration,
                    thumbnail,
                    caption,
                    usertags,
                    location,
                    extra_data=extra_data,
                )
            except Exception as e:
                if "Transcode not finished yet" in str(e):
                    """
                    Response 202 status:
                    {"message": "Transcode not finished yet.", "status": "fail"}
                    """
                    time.sleep(10)
                    continue
                raise e
            else:
                if configured:
                    media = configured.get("media")
                    self.expose()
                    return extract_media_v1(media)
        raise VideoConfigureError(response=self.last_response, **self.last_json)

    def video_configure(
        self,
        upload_id: str,
        width: int,
        height: int,
        duration: int,
        thumbnail: Path,
        caption: str,
        usertags: List[Usertag] = [],
        location: Location = None,
        extra_data: Dict[str, str] = {},
    ) -> Dict:
        """
        Post Configure Video (send caption, thumbnail and more to Instagram)

        Parameters
        ----------
        upload_id: str
            Unique upload_id
        width: int
            Width of the video in pixels
        height: int
            Height of the video in pixels
        duration: int
            Duration of the video in seconds
        thumbnail: str
            Path to thumbnail for video. When None, then thumbnail is generate automatically
        caption: str
            Media caption
        usertags: List[Usertag], optional
            List of users to be tagged on this upload, default is empty list.
        location: Location, optional
            Location tag for this upload, default is None
        extra_data: Dict[str, str], optional
            Dict of extra data, if you need to add your params, like {"share_to_facebook": 1}.

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        self.photo_rupload(Path(thumbnail), upload_id)
        usertags = [
            {"user_id": tag.user.pk, "position": [tag.x, tag.y]} for tag in usertags
        ]
        data = {
            "multi_sharing": "1",
            "creation_logger_session_id": self.client_session_id,
            "upload_id": upload_id,
            "source_type": "4",
            "location": self.location_build(location),
            "poster_frame_index": 0,
            "length": duration,
            "audio_muted": False,
            "usertags": dumps({"in": usertags}),
            "filter_type": "0",
            "date_time_original": date_time_original(time.localtime()),
            "timezone_offset": str(self.timezone_offset),
            "clips": [{"length": duration, "source_type": "4"}],
            "extra": {"source_width": width, "source_height": height},
            "device": self.device,
            "caption": caption,
            **extra_data,
        }
        return self.private_request(
            "media/configure/?video=1", self.with_default_data(data)
        )

    def video_upload_to_story(
        self,
        path: Path,
        caption: str = "",
        thumbnail: Path = None,
        mentions: List[StoryMention] = [],
        locations: List[StoryLocation] = [],
        links: List[StoryLink] = [],
        hashtags: List[StoryHashtag] = [],
        stickers: List[StorySticker] = [],
        medias: List[StoryMedia] = [],
        polls: List[StoryPoll] = [],
        extra_data: Dict[str, str] = {},
    ) -> Story:
        """
        Upload video as a story and configure it

        Parameters
        ----------
        path: Path
            Path to the media
        caption: str
            Story caption
        thumbnail: str
            Path to thumbnail for video. When None, then thumbnail is generate automatically
        mentions: List[StoryMention], optional
            List of mentions to be tagged on this upload, default is empty list.
        locations: List[StoryLocation], optional
            List of locations to be tagged on this upload, default is empty list.
        links: List[StoryLink]
            URLs for Swipe Up
        hashtags: List[StoryHashtag], optional
            List of hashtags to be tagged on this upload, default is empty list.
        stickers: List[StorySticker], optional
            List of stickers to be tagged on this upload, default is empty list.
        medias: List[StoryMedia], optional
            List of medias to be tagged on this upload, default is empty list.
        polls: List[StoryPoll], optional
            List of polls to be included on this upload, default is empty list.
        extra_data: Dict[str, str], optional
            Dict of extra data, if you need to add your params, like {"share_to_facebook": 1}.

        Returns
        -------
        Story
            An object of Media class
        """
        path = Path(path)
        if thumbnail is not None:
            thumbnail = Path(thumbnail)
        upload_id, width, height, duration, thumbnail = self.video_rupload(
            path, thumbnail, to_story=True
        )
        for attempt in range(50):
            self.logger.debug(f"Attempt #{attempt} to configure Video: {path}")
            time.sleep(3)
            try:
                configured = self.video_configure_to_story(
                    upload_id,
                    width,
                    height,
                    duration,
                    thumbnail,
                    caption,
                    mentions,
                    locations,
                    links,
                    hashtags,
                    stickers,
                    medias,
                    polls,
                    extra_data=extra_data,
                )
            except Exception as e:
                if "Transcode not finished yet" in str(e):
                    """
                    Response 202 status:
                    {"message": "Transcode not finished yet.", "status": "fail"}
                    """
                    time.sleep(10)
                    continue
                raise e
            if configured:
                media = configured.get("media")
                self.expose()
                return Story(
                    links=links,
                    mentions=mentions,
                    hashtags=hashtags,
                    locations=locations,
                    stickers=stickers,
                    medias=medias,
                    polls=polls,
                    **extract_media_v1(media).dict(),
                )
        raise VideoConfigureStoryError(response=self.last_response, **self.last_json)

    def video_configure_to_story(
        self,
        upload_id: str,
        width: int,
        height: int,
        duration: int,
        thumbnail: Path,
        caption: str,
        mentions: List[StoryMention] = [],
        locations: List[StoryLocation] = [],
        links: List[StoryLink] = [],
        hashtags: List[StoryHashtag] = [],
        stickers: List[StorySticker] = [],
        medias: List[StoryMedia] = [],
        polls: List[StoryPoll] = [],
        thread_ids: List[int] = [],
        extra_data: Dict[str, str] = {},
    ) -> Dict:
        """
        Story Configure for Photo

        Parameters
        ----------
        upload_id: str
            Unique upload_id
        width: int
            Width of the video in pixels
        height: int
            Height of the video in pixels
        duration: int
            Duration of the video in seconds
        thumbnail: str
            Path to thumbnail for video. When None, then thumbnail is generate automatically
        caption: str
            Media caption
        mentions: List[StoryMention], optional
            List of mentions to be tagged on this upload, default is empty list.
        locations: List[StoryLocation], optional
            List of locations to be tagged on this upload, default is empty list.
        links: List[StoryLink]
            URLs for Swipe Up
        hashtags: List[StoryHashtag], optional
            List of hashtags to be tagged on this upload, default is empty list.
        stickers: List[StorySticker], optional
            List of stickers to be tagged on this upload, default is empty list.
        medias: List[StoryMedia], optional
            List of medias to be tagged on this upload, default is empty list.
        polls: List[StoryPoll], optional
            List of polls to be included on this upload, default is empty list.
        thread_ids: List[int], optional
            List of Direct Message Thread ID (to send a story to a thread)
        extra_data: Dict[str, str], optional
            Dict of extra data, if you need to add your params, like {"share_to_facebook": 1}.

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        timestamp = int(time.time())
        mentions = mentions.copy()
        locations = locations.copy()
        links = links.copy()
        hashtags = hashtags.copy()
        stickers = stickers.copy()
        medias = medias.copy()
        polls = polls.copy()
        thread_ids = thread_ids.copy()
        story_sticker_ids = []
        data = {
            # USE extra_data TO EXTEND THE SETTINGS OF THE LOADED STORY,
            #   USE FOR EXAMPLE THE PROPERTIES SPECIFIED IN THE COMMENT:
            # ---------------------------------
            # When send to DIRECT:
            # "allow_multi_configures": "1",
            # "client_context":"6823316152962778207",
            #      ^----- token = random.randint(6800011111111111111, 6800099999999999999) from direct.py
            # "is_shh_mode":"0",
            # "mutation_token":"6824688191453546273",
            # "nav_chain":"1qT:feed_timeline:1,1qT:feed_timeline:7,ReelViewerFragment:reel_feed_timeline:21,5HT:attribution_quick_camera_fragment:22,4ji:reel_composer_preview:23,8wg:direct_story_audience_picker:24,4ij:reel_composer_camera:25,ReelViewerFragment:reel_feed_timeline:26",
            # "recipient_users":"[]",
            # "send_attribution":"direct_story_audience_picker",
            # "thread_ids":"[\"340282366841710300949128149448121770626\"]",  <-- send story to direct
            # "view_mode": "replayable",
            # ---------------------------------
            # Optional (markup for caption field) when tagging:
            # "story_captions":"[{\"text\":\"@user1+\\n\\n@user2+\",\"position_data\":{\"x\":0.5,\"y\":0.5,\"height\":272.0,\"width\":670.0,\"rotation\":0.0},\"scale\":1.0,\"font_size\":24.0,\"format_type\":\"classic_v2\",\"effects\":[\"disabled\"],\"colors\":[\"#ffffff\"],\"alignment\":\"center\",\"animation\":\"\"}]",
            # ---------------------------------
            # SEGMENT MODE (when file is too big):
            # "allow_multi_configures": "1",
            # "segmented_video_group_id": str(uuid4()),
            # "multi_upload_session_id": str(uuid4()),
            # "segmented_video_count": "4",  # "4"  # SEGMENT MODE
            # "segmented_video_index": "0",  # 0,1,2,3  # SEGMENT MODE
            # "is_multi_upload": "1",  # SEGMENT MODE
            # "is_segmented_video": "1",  # SEGMENT MODE
            # ---------------------------------
            # COMMON properties:
            "_uid": str(self.user_id),
            "supported_capabilities_new": dumps(config.SUPPORTED_CAPABILITIES),
            "has_original_sound": "1",
            "filter_type": "0",
            "camera_session_id": self.client_session_id,
            "camera_entry_point": str(random.randint(35, 164)),
            "composition_id": self.generate_uuid(),
            # "camera_make": self.device_settings.get("manufacturer", "Xiaomi"),
            # "camera_model": self.device_settings.get("model", "MI+5s"),
            "timezone_offset": str(self.timezone_offset),
            "client_timestamp": str(timestamp),
            "client_shared_at": str(timestamp - 7),  # 7 seconds ago
            # "imported_taken_at": str(timestamp - 5 * 24 * 3600),  # 5 days ago
            "date_time_original": date_time_original(time.localtime()),
            # "date_time_digitalized": date_time_original(time.localtime()),
            # "story_sticker_ids": "",
            # "media_folder": "Camera",
            "configure_mode": "1",
            # "configure_mode": "2", <- when direct
            "source_type": "3",  # "3"
            "video_result": "",
            "creation_surface": "camera",
            # "software": config.SOFTWARE.format(**self.device_settings),
            # "caption": caption,
            "capture_type": "normal",
            # "rich_text_format_types": '["classic_v2"]',  # default, typewriter
            "upload_id": upload_id,
            # "scene_capture_type": "standard",
            # "scene_type": "",
            "original_media_type": "video",
            "camera_position": "back",
            # Facebook Sharing Part:
            # "xpost_surface": "auto_xpost",
            # "share_to_fb_destination_type": "USER",
            # "share_to_fb_destination_id":"832928543",
            # "share_to_facebook":"1",
            # "fb_access_token":"EAABwzLixnjYBACVgqBfLyDuPWs6RN2sTZC........cnNkjHCH2",
            # "attempt_id": str(uuid4()),
            "device": self.device,
            "length": duration,
            "clips": [
                {"length": duration, "source_type": "3", "camera_position": "back"}
            ],
            # "edits": {
            #     "filter_type": 0,
            #     "filter_strength": 1.0,
            #     "crop_original_size": [width, height],
            #     # "crop_center": [0, 0],
            #     # "crop_zoom": 1
            # },
            "media_transformation_info": dumps(
                {
                    "width": str(width),
                    "height": str(height),
                    "x_transform": "0",
                    "y_transform": "0",
                    "zoom": "1.0",
                    "rotation": "0.0",
                    "background_coverage": "0.0",
                }
            ),
            "extra": {"source_width": width, "source_height": height},
            "audio_muted": False,
            "poster_frame_index": 0,
            # "app_attribution_android_namespace": "",
        }
        data.update(extra_data)
        tap_models = []
        static_models = []
        if mentions:
            reel_mentions = []
            text_metadata = []
            for mention in mentions:
                reel_mentions.append(
                    {
                        "x": mention.x,
                        "y": mention.y,
                        "z": 0,
                        "width": mention.width,
                        "height": mention.height,
                        "rotation": 0.0,
                        "type": "mention",
                        "user_id": str(mention.user.pk),
                        "is_sticker": False,
                        "display_type": "mention_username",
                        "tap_state": 0,
                        "tap_state_str_id": "mention_text",
                    }
                )
                text_metadata.append(
                    {
                        "font_size": 24.0,
                        "scale": 1.0,
                        "width": 366.0,
                        "height": 102.0,
                        "x": mention.x,
                        "y": mention.y,
                        "rotation": 0.0,
                    }
                )
            data["text_metadata"] = dumps(text_metadata)
            # data["reel_mentions"] = dumps(reel_mentions)
            tap_models.extend(reel_mentions)
        if hashtags:
            story_sticker_ids.append("hashtag_sticker")
            for mention in hashtags:
                item = {
                    "x": mention.x,
                    "y": mention.y,
                    "z": 0,
                    "width": mention.width,
                    "height": mention.height,
                    "rotation": 0.0,
                    "type": "hashtag",
                    "tag_name": mention.hashtag.name,
                    "is_sticker": True,
                    "tap_state": 0,
                    "tap_state_str_id": "hashtag_sticker_gradient",
                }
                tap_models.append(item)
        if locations:
            story_sticker_ids.append("location_sticker")
            for mention in locations:
                mention.location = self.location_complete(mention.location)
                item = {
                    "x": mention.x,
                    "y": mention.y,
                    "z": 0,
                    "width": mention.width,
                    "height": mention.height,
                    "rotation": 0.0,
                    "type": "location",
                    "location_id": str(mention.location.pk),
                    "is_sticker": True,
                    "tap_state": 0,
                    "tap_state_str_id": "location_sticker_vibrant",
                }
                tap_models.append(item)
        if links:
            # instagram allow one link now
            link = links[0]
            self.private_request(
                "media/validate_reel_url/",
                {
                    "url": str(link.webUri),
                    "_uid": str(self.user_id),
                    "_uuid": str(self.uuid),
                },
            )
            stickers.append(
                StorySticker(
                    type="story_link",
                    x=link.x,
                    y=link.y,
                    z=link.z,
                    width=link.width,
                    height=link.height,
                    rotation=link.rotation,
                    extra=dict(
                        link_type="web",
                        url=str(link.webUri),
                        tap_state_str_id="link_sticker_default",
                    ),
                )
            )
            story_sticker_ids.append("link_sticker_default")
        if stickers:
            for sticker in stickers:
                sticker_extra = sticker.extra or {}
                if sticker.id:
                    sticker_extra["str_id"] = sticker.id
                    story_sticker_ids.append(sticker.id)
                tap_models.append(
                    {
                        "x": round(sticker.x, 7),
                        "y": round(sticker.y, 7),
                        "z": sticker.z,
                        "width": round(sticker.width, 7),
                        "height": round(sticker.height, 7),
                        "rotation": sticker.rotation,
                        "type": sticker.type,
                        "is_sticker": True,
                        "selected_index": 0,
                        "tap_state": 0,
                        **sticker_extra,
                    }
                )
                if sticker.type == "gif":
                    data["has_animated_sticker"] = "1"
        if medias:
            for feed_media in medias:
                assert feed_media.media_pk, "Required StoryMedia.media_pk"
                # if not feed_media.user_id:
                #     user = self.media_user(feed_media.media_pk)
                #     feed_media.user_id = user.pk
                item = {
                    "x": feed_media.x,
                    "y": feed_media.y,
                    "z": feed_media.z,
                    "width": feed_media.width,
                    "height": feed_media.height,
                    "rotation": feed_media.rotation,
                    "type": "feed_media",
                    "media_id": str(feed_media.media_pk),
                    "media_owner_id": str(feed_media.user_id or ""),
                    "product_type": "feed",
                    "is_sticker": True,
                    "tap_state": 0,
                    "tap_state_str_id": "feed_post_sticker_square",
                }
                tap_models.append(item)
            data["reshared_media_id"] = str(feed_media.media_pk)
        if polls:
            story_sticker_ids.append("polling_sticker_v2")
            for poll in polls:
                poll_extra = poll.extra or {}
                tap_models.append(
                    {
                        "x": round(poll.x, 7),
                        "y": round(poll.y, 7),
                        "z": poll.z,
                        "width": round(poll.width, 7),
                        "height": round(poll.height, 7),
                        "rotation": poll.rotation,
                        "type": poll.type,
                        "poll_type": poll.poll_type,
                        "is_sticker": True,
                        "tap_state": 0,
                        "tap_state_str_id": "polling_sticker_v2",
                        "is_multi_option_poll": poll.is_multi_option,
                        "is_shared_result": poll.is_shared_result,
                        "viewer_can_vote": poll.viewer_can_vote,
                        "finished": poll.finished,
                        "color": poll.color,
                        "question": poll.question,
                        "tallies": [
                            {
                                "count": 0,
                                "font_size": 39.0,
                                "text": o
                            }
                            for o in poll.options
                        ],
                        **poll_extra,
                    }
                )
        if thread_ids:
            # Send to direct thread
            token = self.generate_mutation_token()
            data.update(
                {
                    "configure_mode": "2",
                    "allow_multi_configures": "1",
                    "client_context": token,
                    "is_shh_mode": "0",
                    "mutation_token": token,
                    "nav_chain": (
                        "1qT:feed_timeline:1,1qT:feed_timeline:7,ReelViewerFragment:reel_feed_timeline:21,"
                        "5HT:attribution_quick_camera_fragment:22,4ji:reel_composer_preview:23,"
                        "8wg:direct_story_audience_picker:24,4ij:reel_composer_camera:25,"
                        "ReelViewerFragment:reel_feed_timeline:26"
                    ),
                    "recipient_users": "[]",
                    "send_attribution": "direct_story_audience_picker",
                    "thread_ids": dumps([str(tid) for tid in thread_ids]),
                    "view_mode": "replayable",
                }
            )
        if tap_models:
            data["tap_models"] = dumps(tap_models)
        if static_models:
            data["static_models"] = dumps(static_models)
        if story_sticker_ids:
            data["story_sticker_ids"] = story_sticker_ids[0]
        return self.private_request(
            "media/configure_to_story/?video=1", self.with_default_data(data)
        )

    def video_upload_to_direct(
        self,
        path: Path,
        caption: str = "",
        thumbnail: Path = None,
        mentions: List[StoryMention] = [],
        medias: List[StoryMedia] = [],
        thread_ids: List[int] = [],
        extra_data: Dict[str, str] = {},
    ) -> DirectMessage:
        """
        Upload video to direct thread as a story and configure it

        Parameters
        ----------
        path: Path
            Path to the media
        caption: str
            Story caption
        thumbnail: str
            Path to thumbnail for video. When None, then thumbnail is generate automatically
        mentions: List[StoryMention], optional
            List of mentions to be tagged on this upload, default is empty list.
        thread_ids: List[int], optional
            List of Direct Message Thread ID (to send a story to a thread)
        extra_data: List[str, str], optional
            Dict of extra data, if you need to add your params, like {"share_to_facebook": 1}.

        Returns
        -------
        DirectMessage
            An object of DirectMessage class
        """
        path = Path(path)
        if thumbnail is not None:
            thumbnail = Path(thumbnail)
        upload_id, width, height, duration, thumbnail = self.video_rupload(
            path, thumbnail, to_story=True
        )
        for attempt in range(50):
            self.logger.debug(f"Attempt #{attempt} to configure Video: {path}")
            time.sleep(3)
            try:
                configured = self.video_configure_to_story(
                    upload_id,
                    width,
                    height,
                    duration,
                    thumbnail,
                    caption,
                    mentions=mentions,
                    medias=medias,
                    thread_ids=thread_ids,
                    extra_data=extra_data,
                )
            except Exception as e:
                if "Transcode not finished yet" in str(e):
                    """
                    Response 202 status:
                    {"message": "Transcode not finished yet.", "status": "fail"}
                    """
                    time.sleep(10)
                    continue
                raise e
            if configured and thread_ids:
                return extract_direct_message(configured.get("message_metadata", [])[0])
        raise VideoConfigureStoryError(response=self.last_response, **self.last_json)


def analyze_video(path: Path, thumbnail: Path = None) -> tuple:
    """
    Story Configure for Photo

    Parameters
    ----------
    path: Path
        Path to the media
    thumbnail: str
        Path to thumbnail for video. When None, then thumbnail is generate automatically

    Returns
    -------
    Tuple
        (width, height, duration, thumbnail)
    """

    try:
        import moviepy.editor as mp
    except ImportError:
        try:
            import moviepy as mp
        except ImportError:
            raise Exception("Please install moviepy>=1.0.3 and retry")

    print(f'Analyzing video file "{path}"')
    video = mp.VideoFileClip(str(path))
    width, height = video.size
    if not thumbnail:
        thumbnail = f"{path}.jpg"
        print(f'Generating thumbnail "{thumbnail}"...')
        video.save_frame(thumbnail, t=(video.duration / 2))
    # duration = round(video.duration + 0.001, 3)
    try:
        video.close()
    except AttributeError:
        pass
    return width, height, video.duration, thumbnail



================================================
FILE: .github/dependabot.yml
================================================
# To get started with Dependabot version updates, you'll need to specify which
# package ecosystems to update and where the package manifests are located.
# Please see the documentation for all configuration options:
# https://help.github.com/github/administering-a-repository/configuration-options-for-dependency-updates

version: 2
updates:
  - package-ecosystem: "pip" # See documentation for possible values
    directory: "/" # Location of package manifests
    schedule:
      interval: "daily"
  - package-ecosystem: "docker"
    directory: "/docker"
    schedule:
      interval: "daily"
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "daily"



================================================
FILE: .github/actions/install-dependencies/action.sh
================================================
set -euo pipefail

echo "Ensuring pip is up to date"
python -m pip install --upgrade pip

if [[ "${INSTALL_REQUIREMENTS}" == "true"  ]]; then
  echo "Installing code requirements"
  pip install -r requirements.txt
fi

if [[ "${INSTALL_TEST_REQUIREMENTS}" == "true"  ]]; then
  echo "Installing test requirements"
  pip install -r requirements-test.txt
fi

if [[ "${INSTALL_DOCS_REQUIREMENTS}" == "true"  ]]; then
  echo "Installing docs requirements"
  pip install -r requirements-docs.txt
fi



================================================
FILE: .github/actions/install-dependencies/action.yml
================================================
name: "Install Dependencies"
description: "Install Python dependencies"
inputs:
  requirements:
    description: "Should requirements.txt be installed"
    default: "false"
    required: false
  test-requirements:
    description: "Should requirements-test.txt be installed"
    default: "false"
    required: false
  docs-requirements:
    description: "Should requirements-docs.txt be installed"
    default: "false"
    required: false
runs:
  using: "composite"
  steps:
    - name: "Install Python dependencies"
      run: "$GITHUB_ACTION_PATH/action.sh"
      shell: "bash"
      env:
        INSTALL_REQUIREMENTS: ${{ inputs.requirements }}
        INSTALL_TEST_REQUIREMENTS: ${{ inputs.test-requirements }}
        INSTALL_DOCS_REQUIREMENTS: ${{ inputs.docs-requirements }}



================================================
FILE: .github/actions/publish-docs-with-mike/action.sh
================================================
#!/usr/bin/env bash

set -eo pipefail

echo "::group::Configure Git User"
"${GITHUB_ACTION_PATH}/configure_git_user.sh"
echo "::endgroup::"

echo "::group::Pull down latest docs commit"
git fetch --no-tags --prune --progress --no-recurse-submodules --depth=1 origin gh-pages
echo "::endgroup::"

echo "::group::Publish documentation"
if [[ "${NEW_VERSION}" == "false" ]]; then
  if [[ "${VERSION_NAME}" == "" ]]; then
    echo "::error::'version_name' must be specified when 'NEW_VERSION' is false."
    exit 1
  fi
  echo "mike deploy \"${VERSION_NAME}\""
  mike deploy "${VERSION_NAME}"
elif [[ "${GITHUB_EVENT_NAME:-}" != "release" ]]; then
  echo "::error::new_version can only be used for release events."
  exit 1
else
  # drop leading "v" from tag name to have just the version number
  "${GITHUB_ACTION_PATH}/update_docs_for_version.sh" "${RELEASE_TAG:1}"
fi
echo "git push origin gh-pages"
git push origin gh-pages
echo "::endgroup::"



================================================
FILE: .github/actions/publish-docs-with-mike/action.yml
================================================
name: "Publish Docs with Mike"
description: |
  Publish versioned documentation with Mike.
  Requires a python environment to already be setup with mike and any other documentation dependencies installed.
inputs:
  version_name:
    description: |
      Name a version to publish.
      Required when new_version is false.
    required: false
    default: ""
  new_version:
    description: |
      If true, publish a new docs version. If an existing version uses the alias/tile "latest",
      update the records so that the new version becomes the latest version.
      If version_name is given, that value will be used. Otherwise the release tag will be used.
    required: false
    default: "false"
  commit_user_name:
    description: "User name to use for commits. When omitted, the event values will be inspected to derive the name."
    default: ""
    required: false
  commit_user_email:
    description: "User email to use for commits. When omitted, the event values will be inspected to derive the email."
    default: ""
    required: false
runs:
  using: "composite"
  steps:
    - run: "$GITHUB_ACTION_PATH/action.sh"
      shell: "bash"
      env:
        USER_NAME: ${{ inputs.name }}
        USER_EMAIL: ${{ inputs.email }}
        VERSION_NAME: ${{ inputs.version_name }}
        NEW_VERSION: ${{ inputs.new_version }}
        RELEASE_TAG: ${{ github.event.release.tag_name }}



================================================
FILE: .github/actions/publish-docs-with-mike/configure_git_user.sh
================================================
#!/usr/bin/env bash

set -euo pipefail

NO_REPLY_SUFFIX="@users.noreply.github.com"

function set_and_exit() {
  local name="${USER_NAME:-$1}"
  local email="${USER_EMAIL:-$2}"
  git config --local user.name "${name}"
  git config --local user.email "${email}"
  exit 0
}

function json_query() {
  jq -e "${1}" "${GITHUB_EVENT_PATH}"
}

if [[ "${USER_NAME}" != "" && "${USER_EMAIL}" != "" ]]; then
  set_and_exit
fi

echo "::debug::Attempting push event pusher"
if json_query ".push.pusher" > /dev/null ; then
  echo "::debug::Found push event pusher"
  set_and_exit "$(json_query '.push.pusher.name')" "$(json_query '.push.pusher.email')"
fi

echo "::debug::Attempting merge merged by"
if json_query ".pull_request.merged_by" > /dev/null ; then
  echo "::debug::Found pull request event merged by"
  LOGIN="$(json_query '.pull_request.merged_by.login')"
  set_and_exit "${LOGIN}" "${LOGIN}${NO_REPLY_SUFFIX}"
fi

echo "::debug::Attempting event sender"
if json_query ".sender" > /dev/null ; then
  echo "::debug::Found pull event sender"
  LOGIN="$(json_query '.sender.login')"
  set_and_exit "${LOGIN}" "${LOGIN}${NO_REPLY_SUFFIX}"
fi

echo "::debug::Falling back to GITHUB_ACTOR"
LOGIN="${GITHUB_ACTOR:-github_action}"
set_and_exit "${LOGIN}" "${LOGIN}${NO_REPLY_SUFFIX}"



================================================
FILE: .github/actions/publish-docs-with-mike/update_docs_for_version.sh
================================================
#!/usr/bin/env bash

set -eo pipefail

NEW_VERSION="${1}"
PREV_LATEST="$(mike list --json | jq --raw-output '.[] | select(.aliases == ["latest"]) | .version')"

if [[ "${PREV_LATEST}" == "" ]]; then
  echo "No previous version found using the latest alias. Nothing to retitle."
else
  echo "mike retitle --message \"Remove latest from title of ${PREV_LATEST}\" \"${PREV_LATEST}\" \"${PREV_LATEST}\""
  mike retitle --message "Remove latest from title of ${PREV_LATEST}" "${PREV_LATEST}" "${PREV_LATEST}"
fi
echo "mike deploy --update-aliases --title \"${NEW_VERSION} (latest)\" \"${NEW_VERSION}\" \"latest\""
mike deploy --update-aliases --title "${NEW_VERSION} (latest)" "${NEW_VERSION}" "latest"



================================================
FILE: .github/ISSUE_TEMPLATE/bug_report.md
================================================
---
name: Bug report
about: Create a report to help us improve
title: "[BUG]"
labels: bug
assignees: ''

---

### Try Instagrapi SaaS with a free trial https://hikerapi.com/p/5GBWznd3

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Provide a piece of code to reproduce the problem.

**Traceback**
Show your full traceback so that it is clear where exactly the error occurred.

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Desktop (please complete the following information):**
 - OS: [e.g. Ubuntu 21.04]
 - Python version [e.g. 3.8.3]
 - instagrapi version [e.g. 1.9.3, not "latest"]
 - moveipy version if used
 - imagemagick version if used

**Additional context**
Add any other context about the problem here.



================================================
FILE: .github/ISSUE_TEMPLATE/feature_request.md
================================================
---
name: Feature request
about: Suggest an idea for this project
title: ''
labels: enhancement
assignees: ''

---

### Try Instagrapi SaaS with a free trial https://hikerapi.com/p/5GBWznd3

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request here.



================================================
FILE: .github/workflows/codeql-analysis.yml
================================================
# For most projects, this workflow file will not need changing; you simply need
# to commit it to your repository.
#
# You may wish to alter this file to override the set of languages analyzed,
# or to provide custom queries or build logic.
#
# ******** NOTE ********
# We have attempted to detect the languages in your repository. Please check
# the `language` matrix defined below to confirm you have the correct set of
# supported CodeQL languages.
#
name: "CodeQL"

on:
  push:
    branches: [ master ]
  pull_request:
    # The branches below must be a subset of the branches above
    branches: [ master ]
  schedule:
    - cron: '28 6 * * 5'

jobs:
  analyze:
    name: Analyze
    runs-on: ubuntu-latest
    permissions:
      actions: read
      contents: read
      security-events: write

    strategy:
      fail-fast: false
      matrix:
        language: [ 'python' ]
        # CodeQL supports [ 'cpp', 'csharp', 'go', 'java', 'javascript', 'python' ]
        # Learn more:
        # https://docs.github.com/en/free-pro-team@latest/github/finding-security-vulnerabilities-and-errors-in-your-code/configuring-code-scanning#changing-the-languages-that-are-analyzed

    steps:
    - name: Checkout repository
      uses: actions/checkout@v5

    # Initializes the CodeQL tools for scanning.
    - name: Initialize CodeQL
      uses: github/codeql-action/init@v3
      with:
        languages: ${{ matrix.language }}
        # If you wish to specify custom queries, you can do so here or in a config file.
        # By default, queries listed here will override any specified in a config file.
        # Prefix the list here with "+" to use these queries and those in the config file.
        # queries: ./path/to/local/query, your-org/your-repo/queries@main

    # Autobuild attempts to build any compiled languages  (C/C++, C#, or Java).
    # If this step fails, then you should remove it and run the build manually (see below)
    - name: Autobuild
      uses: github/codeql-action/autobuild@v3

    # ℹ️ Command-line programs to run using the OS shell.
    # 📚 https://git.io/JvXDl

    # ✏️ If the Autobuild fails above, remove it and uncomment the following three lines
    #    and modify them (or add more) to build your code if your project
    #    uses a compiled language

    #- run: |
    #   make bootstrap
    #   make release

    - name: Perform CodeQL Analysis
      uses: github/codeql-action/analyze@v3



================================================
FILE: .github/workflows/python-package.yml
================================================
# This workflow will install Python dependencies, run tests and lint with a variety of Python versions
# For more information see: https://help.github.com/actions/language-and-framework-guides/using-python-with-github-actions

name: Package

on:
  push:
    branches: [ "master" ]
  pull_request: {}

env:
  PYTHON_VERSION: "3.13.5"

jobs:
  bandit:
    runs-on: ubuntu-latest
    steps:
      - name: Check out code
        uses: actions/checkout@v5
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}
      - name: Install dependencies
        uses: ./.github/actions/install-dependencies
        with:
          test-requirements: "true"

      - name: Run bandit
        run: bandit --ini .bandit -r instagrapi

  flake8:
    runs-on: ubuntu-latest
    steps:
      - name: Check out code
        uses: actions/checkout@v5
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}
      - name: Install dependencies
        uses: ./.github/actions/install-dependencies
        with:
          test-requirements: "true"

      - name: Run flake8
        run: |
          # stop the build if there are Python syntax errors or undefined names
          flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
          # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
          flake8 . --count --exit-zero --statistics
  isort:
    runs-on: ubuntu-latest
    steps:
      - name: Check out code
        uses: actions/checkout@v5
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}
      - name: Install dependencies
        uses: ./.github/actions/install-dependencies
        with:
          requirements: "true"
          test-requirements: "true"

      - name: Run isort
        run: isort --check-only instagrapi

  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [ "3.13.5" ]
    env:
      TEST_ACCOUNTS_URL: ${{ secrets.TEST_ACCOUNTS_URL }}
    steps:
      - name: Check out code
        uses: actions/checkout@v5
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        uses: ./.github/actions/install-dependencies
        with:
          requirements: "true"
          test-requirements: "true"
      - name: Run media test
        run: pytest -sv tests.py::ClientMediaTestCase
      - name: Run user test
        run: pytest -sv tests.py::ClientUserTestCase
      # - name: Run comment test
      #   run: pytest -sv tests.py::ClientCommentTestCase
      # - name: Run location test
      #   run: pytest -sv tests.py::ClientLocationTestCase
      # - name: Run hashtag test
      #   run: pytest -sv tests.py::ClientHashtagTestCase
      # - name: Run share test
      #   run: pytest -sv tests.py::ClientShareTestCase
      # - name: Run highlight test
      #   run: pytest -sv tests.py::ClientHighlightTestCase

  build-docs:
    runs-on: ubuntu-latest
    if: github.event_name == 'pull_request'
    steps:
      - name: Check out code
        uses: actions/checkout@v5

      - uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Install dependencies
        uses: ./.github/actions/install-dependencies
        with:
          requirements: "true"
          test-requirements: "true"
          docs-requirements: "true"

      - name: Build Docs
        run: mkdocs build --strict

      # upload artifact for dev build
      - name: Upload coverage results artifact
        if: github.ref != 'refs/heads/main'
        uses: actions/upload-artifact@v4
        with:
          name: docs-site
          path: site/

  update-dev-docs:
    runs-on: ubuntu-latest
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    steps:
      - name: Check out code
        uses: actions/checkout@v5

      - uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Install dependencies
        uses: ./.github/actions/install-dependencies
        with:
          requirements: "true"
          test-requirements: "true"
          docs-requirements: "true"

      - name: Push documentation changes
        uses: ./.github/actions/publish-docs-with-mike
        with:
          version_name: dev



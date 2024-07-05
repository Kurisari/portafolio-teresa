import json


class Media:
    def __init__(self, email, cv, likedin, tel):
        self.email = email
        self.cv = cv
        self.likedin = likedin
        self.tel = tel



class Info:
    def __init__(self, icon, title, subtitle, description, date="", certificate="", technologies=[], image="", url="", github="", image_mobile="", list=[]):
        self.icon = icon
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.date = date
        self.certificate = certificate
        self.image = image
        self.image_mobile = image_mobile
        self.url = url
        self.github = github
        self.list=list


class Extra:
    def __init__(self, image, title, description, url):
        self.image = image
        self.title = title
        self.description = description
        self.url = url

class Skills:
    def __init__(self, title, percentage):
        self.title = title
        self.percentage = percentage


class Data:
    def __init__(
        self,
            title,
            description,
            image,
            avatar,
            name,
            skill,
            location,
            media,
            about,
            experience,
            projects,
            training,
            extras,
            skills_comp,
            skills_hab,
            languages,
            extra
    ):
        self.title = title
        self.description = description
        self.image = image
        self.avatar = avatar
        self.name = name
        self.skill = skill
        self.skills = skills_comp
        self.location = location
        self.media = Media(**media)
        self.about = about
        self.experience = [Info(**info) for info in experience]
        self.projects = [Info(**info) for info in projects]
        self.training = [Info(**info) for info in training]
        self.extras = [Extra(**info) for info in extras]
        self.skills_comp = [Skills(**info) for info in skills_comp]
        self.skills_hab = [Skills(**info) for info in skills_hab]
        self.languages = [Skills(**info) for info in languages]
        self.extra = [Info(**info) for info in extra]


with open("assets/data/data.json", 'r', encoding='utf-8') as file:
    json_data = json.load(file)

data = Data(**json_data)

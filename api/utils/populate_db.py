import random

from api.db.db import get_session, engine, Base
from api.db.models.Admin import Admin
from api.db.models.HomeContent import HomeContent
from api.db.models.Post import Post
from api.db.models.Project import Project
from api.db.models.Social import Social
from api.db.models.Tag import Tag

from faker import Faker


session = get_session()
fake = Faker()


def populate_admin():
    admins = session.query(Admin).filter(Admin.status == True).all()
    if admins:
        return "Admin is already existent"

    admin = Admin(
        username="adryell",
        password=123456,
        status=True,
    )

    session.add(admin)


def populate_home_contents():
    for _ in range(2):
        content = fake.text()
        contenttypes = ["whwoiam","whoido","hometitle","homefooter"]
        homecontentdb = session.query(HomeContent).filter(HomeContent.content == content,
                                                         HomeContent.homecontenttype == contenttypes[_]
                                                         ).one_or_none()
        if homecontentdb:
            continue

        home_content = HomeContent(
            content=content,
            homecontenttype=contenttypes[_]
        )

        session.add(home_content)


def populate_tags():
    tags = [
        "python", "javascript", ("produtividade", "produtivity"),
        ("organização", "organization"), ("finanças", "finances"), ("vida", "life"),
        ("rotina", "routine"), "php", "flask", "fastapi", ("estudos", "studies")
    ]
    for index, _ in enumerate(tags):
        has_english_name = False if isinstance(_, str) else True
        if has_english_name:
            tagdb = session.query(Tag).filter(Tag.portuguese_name == _[0], Tag.active == True).one_or_none()
            if tagdb:
                continue
        else:
            tagdb = session.query(Tag).filter(Tag.portuguese_name == _, Tag.active == True).one_or_none()
            if tagdb:
                continue

        tag = Tag(
            portuguese_name=tags[index] if isinstance(_, str) else tags[index][0],
            english_name=tags[index] if isinstance(_, str) else tags[index][1],
            active=True
        )

        session.add(tag)
        session.commit()


def populate_posts():
    for _ in range(8):
        title = [fake.sentence(nb_words=random.randint(3, 8)) for _ in range(2)]
        description = [fake.paragraph(nb_sentences=random.randint(1, 3)) for _ in range(2)]
        content = [fake.paragraph(nb_sentences=random.randint(2, 5)) for _ in range(2)]

        postdb = session.query(Post).filter(
            Post.active == True,
            Post.title == title[0],
            Post.description == description[0],
            Post.content == content[0]
        ).one_or_none()

        if postdb:
            continue

        else:
            post = Post(
                title=title[0],
                english_title=title[1],
                description=description[0],
                english_description=description[1],
                content=content[0],
                english_content=content[1],
                active=True,
            )

            post.tags = [
                random.choice(session.query(Tag).filter(Tag.active == True).all())for _ in range(random.randint(1, 3))
            ]

            session.add(post)


def populate_socials():
    names = ["Github", "Linkedin", "Youtube", "Instagram"]
    links = [
        "https://github.com/adryells",
        "https://www.linkedin.com/in/paulo-adryell-andrade-cardoso-849a4117a/",
        "https://www.youtube.com/channel/UC1yOkhK4hzBJit8RV5C4Aug",
        "https://www.instagram.com/_adryell.md/"
    ]

    medias = [
        '<i class="fab fa-github" aria-hidden="true"></i>',
        '<i class="fab fa-linkedin" aria-hidden="true"></i>',
        '<i class="fab fa-youtube" aria-hidden="true"></i>',
        '<i class="fab fa-instagram" aria-hidden="true"></i>'
    ]

    for _ in range(len(names)):
        social_network = session.query(Social).filter(
            Social.active == True,
            Social.name == names[_],
            Social.link == links[_],
            Social.media == medias[_]
        ).one_or_none()

        if social_network:
            continue

        social_network = Social(
            active=True,
            name=names[_],
            link=links[_],
            media=medias[_]
        )

        session.add(social_network)


def populate_projects():
    # TODO: to get from github api

    titles = [
        "imcPHP", "Tempo_Anime", "aestheticCALC", "PageStyleConfiguration", "PassaTempo-Eureka",
        "CalculatorJS", "Django-Polls", "AgendaDeContatos", "biblios", "Caxias"
    ]

    descriptions = [
        ("calculadora de imc em php", "IMC Calculator in PHP"),
        ("calcule o tempo necessário para terminar um anime", "To calc the time remains to watch a anime"),
        ("uma bela calculadora :D", "A beautiful calculator"),
        ("Pagina de Estilização de seções feita utilizando DOM em JavaScript",
         "Settinger style page was done using DOM JS"),
        ("Jogo desenvolvido em JavaScript para passar o tempo, acerte o Botão correto!",
         "Game developed in JS to pass the time, shot the correct button"),
        ("Calculadora desenvolvida em JS", "Calculator developed in JS"),
        ("Mini-votação desenvolvida estudando a documentação Django.", "Small pooler developed studying django doc"),
        ("Agenda de contatos desenvolvida utilizando o Web Framework Django e Bootstrap.",
         "Contact directory developed using the Django and Bootstrap Web Framework."),
        ("bibliotequinha virtual que tentei criar usando Django",
         "little virtual library that I tried to create using Django"),
        ("Website sobre caxias - MA, desenvolvido estudando css",
         "Website about caxias - MA, developed by studying css")
    ]

    bigdescriptions = [
        fake.paragraph(nb_sentences=random.randint(1, 4)) for _ in range(len(descriptions))
    ]

    link = [
        "https://github.com/adryells/imcPHP",
        "https://github.com/adryells/tempo_anime",
        "https://github.com/adryells/aestheticCALC",
        "https://github.com/adryells/PageStyleConfiguration",
        "https://github.com/adryells/PassaTempo-Eureka",
        "https://github.com/adryells/CalculatorJS",
        "https://github.com/adryells/Django-Polls",
        "https://github.com/adryells/AgendaDeContatos",
        "https://github.com/adryells/biblios",
        "https://github.com/adryells/caxias",
    ]
    for _ in range(len(titles)):
        project = Project(
            title=titles[_],
            english_title=fake.sentence(nb_words=random.randint(1, 3)),
            description=descriptions[_][0],
            english_description=descriptions[_][1],
            bigdescription=bigdescriptions[_],
            english_bigdescription=fake.paragraph(nb_sentences=random.randint(5, 11)),
            link=link[_]
        )

        project.tags = [
            random.choice(session.query(Tag).filter(Tag.active == True).all()) for _ in range(random.randint(1, 3))
        ]

        session.add(project)


def populate_database():
    func_handler = {
        "admin": populate_admin,
        "home_content": populate_home_contents,
        "tag": populate_tags,
        "post": populate_posts,
        "social": populate_socials,
        "project": populate_projects
    }

    for key, value in func_handler.items():
        value()

    session.commit()

# TODO: Dar uma revisada generosa pra melhorar o script de criação/atualização do db


Base.metadata.create_all(engine)
populate_database()

from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # print(content)

        parsed_toml = toml.loads(content)

        name = parsed_toml["tool"]["poetry"]["name"]
        # print('nimi:', name)

        desc = parsed_toml["tool"]["poetry"]["description"]
        # print('kuvaus', desc)
        # print(parsed_toml["tool"]["poetry"]["group"].keys())

        lic = parsed_toml["tool"]["poetry"]["license"]
        authors = parsed_toml["tool"]["poetry"]["authors"]
        
        deps = []
        for i in parsed_toml["tool"]["poetry"]["dependencies"]:
            deps.append(i)
        # print ("deps", deps)

        devdeps = []
        for i in parsed_toml["tool"]["poetry"]["group"]["dev"]["dependencies"]:
            devdeps.append(i)
        # print ("devdeps", devdeps)

        # print(parsed_toml)

        # deserialisoi TOML-formaatissa oleva merkkijono 
        # ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, lic, authors, deps, devdeps)

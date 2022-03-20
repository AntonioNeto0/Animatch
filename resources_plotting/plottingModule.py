import pandas as pd


class PlottingPackage:
    def __init__(self, name, description, chart, plotKind):
        self.name = name
        self.description = description
        self.chart = chart
        self.plotKind = plotKind

    def build_figure(self):
        return self.chart.plot(kind=self.plotKind).figure


class Handler:
    def __init__(self, ds):
        self.ds = ds
        self.packageList = []
        self.packageNameList = []
        self.fill_package_list()
        self.fill_name_list()

    def fill_package_list(self):
        self.packageList.append(PlottingPackage("Quantidade de Animes por season", "Descrição1",self.ds["Release_season"].value_counts(),"barh"))
        self.packageList.append(PlottingPackage("Quantidade de Animes por tipo","Descrição2",self.ds["Type"].value_counts(),"barh"))

    def fill_name_list(self):
        self.packageNameList = list(
            map(self.get_package_name, self.packageList))

    def get_package_name(self, package):
        return package.name

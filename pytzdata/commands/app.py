# -*- coding: utf-8 -*-

from cleo import Application

from .make import MakeCommand

app = Application('pytzdata')

app.add(MakeCommand())


if __name__ == '__main__':
    app.run()

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='package_prac_3',  # Имя пакета
    version='0.0.1',  # Версия пакета
    author='Балуева Мария',
    author_email='mashabalueva@mail.ru',
    description='Учебный пакет для задания 8 в практическом занятии 3',
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MarBalueva/package_prac_3",
    classifiers=["Programming Language :: Python :: 3"],
    )

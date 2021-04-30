from .models import Job

def data():

    d = {
        "ingeniero software":
        [
            'python',
            'react',
            'java',
            'c++',
            '.net',
            'devops',
            'javascript',
            'ingles',
            'flutter',
        ],
        "contador": [
            'sap',
            'crm',
            'finanzas',
            'economia',
            'sql',
            'office',
        ],
        "administracion": [
            'excel',
            'sap',
            'crm',
            'sql',
            'office',
        ],
        "diseno": [
            'photoshop',
            'illustrator',
            'indesign',
            'adobe',
            'grafico',
        ]
    }

    res = {}
    for profession in d.keys():
        professionals = Job.objects.filter(query=profession)
        hist = {}
        for word in d[profession]:
            hist[word] = professionals.filter(description__contains=word).count()
        res[profession] = hist

    return res



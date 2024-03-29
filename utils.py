import re

techmeta = {
"java" : set(['java','j2ee','weblogic','websphere']),
"data-pipelines" : set(['apache spark','hadoop','pyspark','hive','sqoop','kafka']),
"database" : set(['sql','db2','cassandra','mysql','postgresql','sql server','dynamodb','oracle']),
"mearnstack" : set(['nodejs','javascript','reactjs','angular','angularjs','jquery','bootstrap','expressjs']),
"unix" : set(['unix','vmware','perl','linux','bash','shell script','hp-ux', 'solaris']),
"datascience" : set(['data science','spacy','nltk','tensorflow','open.ai','streamlit','huggingface','scikit-learn','scikit','pandas','keras','spark','kafka','machine learning']),
"pythonstack":set(['python','pandas','scrapy']),
"busi-intel" : set(['informatica','tableau']),
"ci-cd" : set(['jenkins','github','ansible','circleci','travisci','gitlab','bitbucket','teamcity','devops']),
"cloud" : set(['amazon redshift','aws ec2','aws lambda','sagemaker', 'aws dynamodb', 'google cloud', 'amazon eks']),
"microsoft":set(['cobol','ado','azure','microsoft visual','c#','asp','windows','.net','visual basic','intellij','visual studio', 'crystal reports', 'business basic','ms sql server'])
  }



def categorize_tech(workhistory):
    tech_matrix={}
    techs_set=set()
    for job in workhistory:
        techslog=[]
        techlogset=set()
        if "techs" in job:
            for tech in job["techs"]:
                if "java" not in techlogset and tech in techmeta["java"]:
                    techslog.append(("java", job["days"]))
                    techlogset.add("java")
                if "datascience" not in techlogset and tech in techmeta["datascience"]:
                    techslog.append(("datascience", job["days"]))
                    techlogset.add("datascience")
                if "mearnstack" not in techlogset and tech in techmeta["mearnstack"]:
                    techslog.append(("mearnstack", job["days"]))
                    techlogset.add("mearnstack")
                if "database" not in techlogset and tech in techmeta["database"]:
                    techslog.append(("database", job["days"]))
                    techlogset.add("database")
                if "unix" not in techlogset and tech in techmeta["unix"]:
                    techslog.append(("unix", job["days"]))
                    techlogset.add("unix")
                if "busi-intel" not in techlogset and tech in techmeta["busi-intel"]:
                    techslog.append(("busi-intel", job["days"]))
                    techlogset.add("busi-intel")
                if "pythonstack" not in techlogset and tech in techmeta["pythonstack"]:
                    techslog.append(("pythonstack", job["days"]))
                    techlogset.add("pythonstack")
                if "ci-cd" not in techlogset and tech in techmeta["ci-cd"]:
                    techslog.append(("ci-cd", job["days"]))
                    techlogset.add("ci-cd")
                if "cloud" not in techlogset and tech in techmeta["cloud"]:
                    techslog.append(("cloud", job["days"]))
                    techlogset.add("cloud")
                if "microsoft" not in techlogset and tech in techmeta["microsoft"]:
                    techslog.append(("microsoft", job["days"]))
                    techlogset.add("microsoft")
                if "data-pipelines" not in techlogset and tech in techmeta["data-pipelines"]:
                    techslog.append(("data-pipelines", job["days"]))
                    techlogset.add("data-pipelines")
        for x in techslog:
            if x[0] in techs_set:
                tech_matrix[x[0]] = tech_matrix[x[0]] + x[1]
            else:
                tech_matrix[x[0]] = x[1]
                techs_set.add(x[0])

    return tech_matrix

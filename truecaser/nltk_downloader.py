import nltk

dler = nltk.downloader.Downloader()
dler._update_index()
dler._status_cache['panlex_lite'] = 'installed'
dler.download("all", "nltk_data/")
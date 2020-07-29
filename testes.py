




import dropbox
import re


nome_arquivo = 'gorpo.txt'
token_dropbox = 'sl.AeuCjBNDEHfTE_h_Gb9MPdzL7ivKysKH1zhJ6OCrRoAOJ_-yC8KcYj7-eJx7M7H31Ieq_wpIXuDanHp3hPhVn28RHz4vncB_LoJx68sWQ2O_zUWJTe_9MbV2SeXN_kHJbvXqaHq2x6U'
d = dropbox.Dropbox(token_dropbox)



targetfile = f"/Manicomio_bot/{nome_arquivo}"

with open(f'arquivos/{nome_arquivo}', "rb") as f:
    meta = d.files_upload(f.read(), targetfile, mode=dropbox.files.WriteMode("overwrite"))
link = d.sharing_create_shared_link(targetfile)
url = link.url
dl_url = re.sub(r"\?dl\=0", "?dl=1", url)
print(dl_url)
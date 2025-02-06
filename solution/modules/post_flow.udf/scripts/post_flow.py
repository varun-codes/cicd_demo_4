import logging
import os
import json
from instabase.ocr.client.libs.ibocr import ParsedIBOCRBuilder

def write_json(**kwargs):
  summary_dict = {"vinay" : "thapa"}
  fn_context = kwargs.get('_FN_CONTEXT_KEY')
  clients, _ = fn_context.get_by_col_name('CLIENTS')
  root_out_folder, _ = fn_context.get_by_col_name('ROOT_OUTPUT_FOLDER')
  
  _, err = clients.ibfile.write_file(os.path.join(root_out_folder, 'summary.json'), json.dumps(summary_dict, indent=4))
  if err:
    return None, f'Failed to write summary file err={err}'
  return summary_dict, None

def register(name_to_fn):
  name_to_fn.update({
    'write_json': {
      'fn': write_json
    }
  })
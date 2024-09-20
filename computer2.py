import os
import json
import numpy as np
from flask import Flask, request, make_response
from utils.call_llm import query_llm, query_llm_qw

########## flask func ##########
app = Flask(__name__)

class JsonEncoder(json.JSONEncoder):
    """Convert numpy classes to JSON serializable objects."""

    def default(self, obj):
        if isinstance(obj, (np.integer, np.floating, np.bool_)):
            return obj.item()
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(JsonEncoder, self).default(obj)


def json_dumps(data):
    return json.dumps(data, ensure_ascii=False, cls=JsonEncoder)

def wrap_resp(res, status=400, headers={'Content-Type': 'application/json'}):
    resp = make_response(json_dumps(res), status)
    resp.headers = headers
    return resp

######### llm api key #########
llm_type = "qwen-vl-max-0809"

######## mian func ###########
savefolder = 'xxxx' # write your savefolder, must be absolute path

def get_shot_answer():
    print('start request llm !')
    command = query_llm_qw("qwen-vl-max-0809")
    print(command)
    return command

@app.route('/get_code', methods = ['POST'])
def get_code():
    inf = request.files.get('input_file')
    out_folder = os.path.join(savefolder, 'output')
    os.makedirs(out_folder, exist_ok=True)
    os.makedirs(savefolder, exist_ok=True)
    input_file = os.path.join(savefolder, inf.filename)
    inf.save(input_file)
    try:
        out = get_shot_answer()
        res = {
            'msg': 'success',
            'code': 0,
            'data': out,
            }
        return wrap_resp(res, 200)
    except Exception as e:
        res = {
            'msg': 'fail',
            'code': -1,
            'data': str(e)
            }
        return wrap_resp(res)


if __name__ == '__main__':
    app.run('0.0.0.0', 9000, debug=False)



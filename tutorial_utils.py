import os
import tempfile

import magma as m

_OUTPUT_TO_EXT = {
    "verilog" : "v",
    "coreir" : "json",
    "coreir-verilog": "v",
}


def magma_to_verilog_string(defn, output="coreir-verilog", **kwargs):
    with tempfile.TemporaryDirectory() as tempdir:
        basename = os.path.join(tempdir, 'out')
        m.compile(basename, defn, output=output, **kwargs)
        out_name = ".".join((basename, _OUTPUT_TO_EXT[output]))
        with open(out_name, 'r') as f:
            return f.read()


def smt_to_smtlib_string(expr, daggify=False):
    return expr.value.to_smtlib(daggify=daggify)
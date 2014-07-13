#!/usr/bin/env python

print "[RENDER NML & NFO] render_nml_nfo.py"

import codecs # used for writing files - more unicode friendly than standard open() module
import json

import shutil
import sys
import os
currentdir = os.curdir
from multiprocessing import Pool
import subprocess

import iron_horse
import utils
import global_constants

# get args passed by makefile
repo_vars = utils.get_repo_vars(sys)

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates_path = os.path.join(currentdir, 'src', 'templates')
templates = PageTemplateLoader(templates_path)

generated_nml_path = os.path.join(iron_horse.generated_files_path, 'nml')
if not os.path.exists(generated_nml_path):
    os.mkdir(generated_nml_path)
generated_nfo_path = os.path.join(iron_horse.generated_files_path, 'nfo')
if not os.path.exists(generated_nfo_path):
    os.mkdir(generated_nfo_path)
grf_nfo = codecs.open(os.path.join(iron_horse.generated_files_path, 'iron-horse.nfo'),'w','utf8')

# we track file timestamps to see if we can render faster by only rendering when source file is changed
dep_timestamps_path = os.path.join('generated', 'dep_timestamps.json')
if not os.path.exists(dep_timestamps_path):
    codecs.open(dep_timestamps_path,'w','utf8').close()
    dep_timestamps = {}
else:
    dep_timestamps = json.loads(codecs.open(dep_timestamps_path,'r','utf8').read())
dep_timestamps_new = {}

consists = iron_horse.get_consists_in_buy_menu_order(show_warnings=True)


def check_item_dirty(path):
    if repo_vars.get('compile_faster', None) == 'True':
        if (float(dep_timestamps.get(path, 0)) == os.stat(path).st_mtime):
            return False
    else:
        return True


def render_nfo(filename):
    nmlc_call_args = ['nmlc',
                      #'--extra-constants=extra_constants.json',
                      '--lang-dir=generated/lang',
                      '--quiet',
                      '--nfo',
                      'generated/nfo/' + filename + '.nfo',
                      'generated/nml/' + filename + '.nml']
    subprocess.call(nmlc_call_args)


def render_header_item_nml_nfo(header_item):
    template = templates[header_item + '.pynml']

    if check_item_dirty(template.filename) == True:
        header_item_nml = codecs.open(os.path.join('generated', 'nml', header_item + '.nml'),'w','utf8')
        header_item_nml.write(utils.unescape_chameleon_output(template(consists=consists, global_constants=global_constants,
                                                        utils=utils, sys=sys, repo_vars=repo_vars)))
        header_item_nml.close()
        render_nfo(header_item)


def render_consist_nml_nfo(consist):
    if check_item_dirty(consist.vehicle_module_path) == True:
        consist_nml = codecs.open(os.path.join('generated', 'nml', consist.id + '.nml'),'w','utf8')
        consist_nml.write(utils.unescape_chameleon_output(consist.render()))
        consist_nml.close()
        render_nfo(consist.id)


def render_dispatcher(items, renderer):
    if repo_vars.get('no_mp', None) == 'True':
        for item in items:
            renderer(item)
    else:
        pool = Pool(processes=16) # 16 is an arbitrary amount that appears to be fast without blocking the system
        pool.map(renderer, items)
        pool.close()
        pool.join()


def link_nfo(item, dep_path, split=None):
    dep_timestamps_new[dep_path] = os.stat(dep_path).st_mtime
    item_nfo = codecs.open(os.path.join('generated', 'nfo', item + '.nfo'),'r','utf8').read()
    if split is not None:
        # fragile split on some specific nfo, may break; assumes a right-split only
        if split in item_nfo:
            item_nfo = item_nfo.split(split)[1]
    grf_nfo.write(item_nfo)


def main():
    header_items = ['header', 'cargo_table', 'railtype_table', 'disable_default_vehicles']

    if repo_vars.get('compile_faster', None) == 'True':
        utils.echo_message('Only rendering changed nml files: (COMPILE_FASTER=True)')

    if repo_vars.get('no_mp', None) == 'True':
        utils.echo_message('Multiprocessing disabled: (NO_MP=True)')

    print "Rendering header items"
    render_dispatcher(header_items, renderer=render_header_item_nml_nfo)

    print "Rendering consists"
    render_dispatcher(consists, renderer=render_consist_nml_nfo)

    print "Linking nfo"
    for header_item in header_items:
        link_nfo(header_item, templates[header_item+".pynml"].filename, split=None)
    for consist in consists:
        link_nfo(header_item, consist.vehicle_module_path, split='\wx00FE 	// DUMMY_CALLBACK;')
    grf_nfo.close()

    dep_timestamps_file = codecs.open(dep_timestamps_path, 'w', 'utf8')
    dep_timestamps_file.write(json.dumps(dep_timestamps_new))
    dep_timestamps_file.close()

    # some warnings suppressed when we call nforenum; assume nmlc has done the right thing and nforenum is wrong
    nforenum_call_args = ['nforenum',
                      '--silent',
                      '--warning-disable=100,109,111,147,170,204',
                      'generated/iron-horse.nfo']
    subprocess.call(nforenum_call_args)


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ALH5aHMZ8SuOo1wF1814CfBgbiFHaB2O
"""

import numpy as np
from io import StringIO
import matplotlib.pyplot as plt
import matplotlib.patches as pat
plt.rcParams['font.family'] = 'UD Digi Kyokasho N-B'

def flowchart(nodes=[{'name':'','shape':'terminal','description':'start'}],edges=[],dpi=40,fontsize=16,figsize=(20,5),named=False):
    news={}
    news['box'] = {'N':np.array([(0,1)]),'W':np.array([(-4,0)]),'S':np.array([(0,-1)]),'E':np.array([(4,0)])}
    news['diamond'] = {'N':np.array([(0,1.5)]),'W':np.array([(-4,0)]),'S':np.array([(0,-1.5)]),'E':np.array([(4,0)])}
    news['loop_start'] = {'N':np.array([(0,1.3)]),'W':np.array([(-4.5,0)]),'S':np.array([(0,-1.3)]),'E':np.array([(4.5,0)])}
    news['loop_end'] = {'N':np.array([(0,1.3)]),'W':np.array([(-4.5,0)]),'S':np.array([(0,-1.3)]),'E':np.array([(4.5,0)])}
    news['terminal'] = {'N':np.array([(0,1)]),'W':np.array([(-4,0)]),'S':np.array([(0,-1)]),'E':np.array([(4,0)])}
    news['connector'] = {'N':np.array([(0,1)]),'W':np.array([(-1,0)]),'S':np.array([(0,-1)]),'E':np.array([(1,0)])}
    news['joint'] = {'N':np.array([(0,0)]),'W':np.array([(0,0)]),'S':np.array([(0,0)]),'E':np.array([(0,0)])}
    news['io'] = {'N':np.array([(0,1)]),'W':np.array([(-4,0)]),'S':np.array([(0,-1)]),'E':np.array([(4,0)])}
    news['manual_input'] = {'N':np.array([(0,1.2)]),'W':np.array([(-4,0)]),'S':np.array([(0,-1.3)]),'E':np.array([(4,0)])}
    news['manual_operation'] = {'N':np.array([(0,1.3)]),'W':np.array([(-4,0)]),'S':np.array([(0,-1.3)]),'E':np.array([(4,0)])}
    news['document'] = {'N':np.array([(0,1.3)]),'W':np.array([(-4,0)]),'S':np.array([(0,-1.3)]),'E':np.array([(4,0)])}
    news['predefined'] = {'N':np.array([(0,1)]),'W':np.array([(-4.5,0)]),'S':np.array([(0,-1)]),'E':np.array([(4.5,0)])}
    news['database'] = {'N':np.array([(0,1.3)]),'W':np.array([(-4,0)]),'S':np.array([(0,-1.3)]),'E':np.array([(4,0)])}

    shapes={}
    shapes['box'] = np.array([(-4,1),(-4,-1),(4,-1),(4,1)])
    shapes['diamond'] = np.array([(0,1.5),(-4,0),(0,-1.5),(4,0)])
    shapes['loop_start'] = np.array([(-3.5,1.3),(-4.5,0.5),(-4.5,-1.3),(4.5,-1.3),(4.5,0.5),(3.5,1.3)])
    shapes['loop_end'] = np.array([(-4.5,1.3),(-4.5,-0.5),(-3.5,-1.3),(3.5,-1.3),(4.5,-0.5),(4.5,1.3)])
    shapes['io'] = np.array([(-3.5,1),(-4.5,-1),(3.5,-1),(4.5,1)])
    shapes['manual_input'] = np.array([(-4,0.7),(-4,-1.3),(4,-1.3),(4,1.8)])
    shapes['manual_operation'] = np.array([(-4.2,1.2),(-3.6,-1.3),(3.6,-1.3),(4.2,1.2)])

    fig = plt.figure(figsize=figsize,dpi=dpi,facecolor='white', linewidth=1)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    connectors={}
    for i,node in enumerate(nodes):
        x,y = 0,-4*i
        if 'offset' in node:
            x,y = np.array(node['offset'])+(x,y)
        if node['shape'] in shapes:
            ax.add_patch(plt.Polygon(shapes[node['shape']]+(x,y),fc='white',ec='black'))
        if node['shape'] == 'terminal':
            ax.add_patch(pat.FancyBboxPatch(xy=(x-3,y), width=6, height=0, boxstyle='round,pad=1', ec='black', fc='white'))
        if node['shape'] == 'connector':
            ax.add_patch(pat.Circle(xy=(x, y), radius=1, ec='black', fc='white'))
        if node['shape'] == 'joint':
            ax.add_patch(pat.Circle(xy=(x, y), radius=0, ec='black', fc='black'))
        if node['shape'] == 'document':
            ax.arrow(x-4,y+1.3,0,-2.6,head_width=0, head_length=0, length_includes_head=True, fc='black', ec='black')
            ax.arrow(x-4,y+1.3,8,0,head_width=0, head_length=0, length_includes_head=True, fc='black', ec='black')
            ax.arrow(x+4,y+1.3,0,-2.6,head_width=0, head_length=0, length_includes_head=True, fc='black', ec='black')
            ax.add_patch(pat.Arc(xy=(x-2,y-0.1), width=6.5, height=3, theta1=210, theta2=330, ec='black', fc='white'))
            ax.add_patch(pat.Arc(xy=(x+2,y-2.5), width=6.5, height=3, theta1=30, theta2=150, ec='black', fc='white'))
        if node['shape'] == 'predefined':
            ax.add_patch(plt.Polygon((np.array([(-4.5,1),(-4.5,-1),(4.5,-1),(4.5,1)])+(x,y)),ec='black',fc='white'))
            ax.arrow(x-4,y-1,0,2,head_width=0, head_length=0, length_includes_head=True, fc='black', ec='black')
            ax.arrow(x+4,y-1,0,2,head_width=0, head_length=0, length_includes_head=True, fc='black', ec='black')
        if node['shape'] == 'database':
            ax.arrow(x-4,y-1,0,2,head_width=0, head_length=0, length_includes_head=True, fc='black', ec='black')
            ax.arrow(x+4,y-1,0,2,head_width=0, head_length=0, length_includes_head=True, fc='black', ec='black')
            ax.add_patch(pat.Arc(xy=(x,y+0.3), width=11.5, height=2, theta1=10, theta2=170, ec='black', fc='white'))
            ax.add_patch(pat.Arc(xy=(x,y+1.7), width=11.5, height=2, theta1=190, theta2=350, ec='black', fc='white'))
            ax.add_patch(pat.Arc(xy=(x,y-0.3), width=11.5, height=2, theta1=190, theta2=350, ec='black', fc='white'))

        if 'description' in node:
            ax.text(x,y,node['description'],va='center',ha='center',fontsize=fontsize)
        if named:
            ax.text(x,news[node['shape']]['N'][0][1]+y-0.25,node['name'],va='center',ha='center',fontsize=fontsize*0.6,color='red')

        connectors[node['name']] = {'N':news[node['shape']]['N']+(x,y),'E':news[node['shape']]['E']+(x,y),
                                    'W':news[node['shape']]['W']+(x,y),'S':news[node['shape']]['S']+(x,y)}
    for edge in edges:
        node_start, edge_start = edge['start']
        node_end, edge_end = edge['end']
        x,y = tuple(*(connectors[node_start][edge_start]))
        if edge_start == 'N': x_,y_,ha,va = x-0.3,y+0.1,'right','bottom'
        if edge_start == 'E': x_,y_,ha,va = x+0.3,y+0.1,'left','bottom'
        if edge_start == 'W': x_,y_,ha,va = x-0.3,y+0.2,'right','bottom'
        if edge_start == 'S': x_,y_,ha,va = x+0.3,y-0.1,'left','top'
        if 'description' in edge:
            ax.text(x_,y_,edge['description'],ha=ha,va=va,fontsize=fontsize)
        if 'offset' in edge:
            for dx,dy in edge['offset']:
                ax.arrow(x,y,dx,dy,head_width=0, head_length=0, length_includes_head=True, fc='black', ec='black')
                x,y = x+dx,y+dy
        dx,dy = tuple(*(connectors[node_end][edge_end] - (x,y)))
        ax.arrow(x,y,dx,dy,head_width=0.5, head_length=0.5, length_includes_head=True, fc='black', ec='black')

    plt.axis('off'); plt.margins(0,0); plt.tight_layout()
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    buf = StringIO()
    plt.savefig(buf,format='svg')
    plt.clf();plt.close()
    return(buf.getvalue())
    
    if __name__ == '__main__':
        flowchart()
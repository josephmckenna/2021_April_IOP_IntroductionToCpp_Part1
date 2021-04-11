import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

df = pd.read_csv("File.txt", sep=" ")
#print(df)

moviewriter = animation.FFMpegWriter( fps=60)
fig = plt.figure(figsize=(12, 6))
with moviewriter.saving(fig, 'myfile.mp4',  dpi=100):
    integration_time = 100
    i = integration_time
    end = len(df.get("x"))
    while( i < end):
        ax = fig.add_subplot(121)
        ax2 = fig.add_subplot(122)

        ax.set_xlabel('X')
        ax.set_xlim([-0.02, 0.02])
        ax.set_ylim([-0.02, 0.02])
        ax.set_ylabel('Y')
        
        ax2.set_xlim([-0.02, 0.02])
        ax2.set_xlabel('Z')
        ax2.set_ylim([-0.02, 0.02])
        ax2.set_ylabel('Y')
        for j in range(i - integration_time, i):
            ax.plot(df.get("x")[j],df.get("y")[j], 'ko')
            ax2.plot(df.get("z")[j],df.get("y")[j], 'ko')
            print(j)
        moviewriter.grab_frame()
        i += 50
        fig.clear()
moviewriter.finish()


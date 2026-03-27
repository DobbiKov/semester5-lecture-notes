import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from scipy.special import comb
from scipy.stats import norm


def generate_ex3_plot1():
    """Chapter 4: Suite ne convergeant pas."""
    #save_to: ex3_plot1.png
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3), sharey=True)
    # Plot X_2n
    ax1.plot([0, 0], [0, 1], 'b-')
    ax1.plot([0, 0.5], [1, 1], 'b-')
    ax1.plot([0.5, 0.5], [1, 0], 'b--')
    ax1.plot([0.5, 1], [0, 0], 'b-')
    ax1.fill_between([0, 0.5], 0, 1, color='blue', alpha=0.2)
    ax1.set_title('$X_{2n}$')
    ax1.set_xticks([0, 0.5, 1])
    ax1.set_xticklabels(['0', '1/2', '1'])
    ax1.set_yticks([0, 1])
    ax1.set_ylim(-0.1, 1.1)
    ax1.grid(True, linestyle=':')
    # Plot X_{2n+1}
    ax2.plot([0, 0.5], [0, 0], 'r-')
    ax2.plot([0.5, 0.5], [0, 1], 'r-')
    ax2.plot([0.5, 1], [1, 1], 'r-')
    ax2.plot([1, 1], [1, 0], 'r-')
    ax2.fill_between([0.5, 1], 0, 1, color='red', alpha=0.2)
    ax2.set_title('$X_{2n+1}$')
    ax2.set_xticks([0, 0.5, 1])
    ax2.set_xticklabels(['0', '1/2', '1'])
    ax2.grid(True, linestyle=':')
    fig.suptitle('Exemple de suite ne convergeant pas')
    plt.savefig('ex3_plot1.png')
    plt.close()


def generate_ex3_plot2():
    """Chapter 4: Suite machine à écrire."""
    #save_to: ex3_plot2.png
    fig = plt.figure(figsize=(12, 4))
    grid = plt.GridSpec(2, 6, hspace=0.5, wspace=0.5)

    def plot_indicator(ax, interval, title):
        ax.plot([0, interval[0]], [0, 0], 'k-')
        ax.plot([interval[0], interval[0]], [0, 1], 'k-')
        ax.plot([interval[0], interval[1]], [1, 1], 'k-')
        ax.plot([interval[1], interval[1]], [1, 0], 'k-')
        ax.plot([interval[1], 1], [0, 0], 'k-')
        ax.fill_between(interval, 0, 1, alpha=0.2)
        ax.set_title(title)
        ax.set_xticks([0, 0.5, 1])
        ax.set_yticks([0, 1])
        ax.set_ylim(-0.1, 1.1)

    ax1 = fig.add_subplot(grid[0, 0:2])
    plot_indicator(ax1, [0, 1], '$X_1$')
    ax2 = fig.add_subplot(grid[0, 2:4])
    plot_indicator(ax2, [0, 1/2], '$X_2$')
    ax3 = fig.add_subplot(grid[0, 4:6])
    plot_indicator(ax3, [1/2, 1], '$X_3$')
    ax4 = fig.add_subplot(grid[1, 0:2])
    plot_indicator(ax4, [0, 1/3], '$X_4$')
    ax4.set_xticks([0, 1/3, 2/3, 1])
    ax5 = fig.add_subplot(grid[1, 2:4])
    plot_indicator(ax5, [1/3, 2/3], '$X_5$')
    ax5.set_xticks([0, 1/3, 2/3, 1])
    ax6 = fig.add_subplot(grid[1, 4:6])
    plot_indicator(ax6, [2/3, 1], '$X_6$')
    ax6.set_xticks([0, 1/3, 2/3, 1])
    plt.savefig('ex3_plot2.png')
    plt.close()


def generate_rademacher_plots():
    """Chapter 4: Fonctions de Rademacher."""
    #save_to: rademacher_plots.png
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4), sharey=True)
    # Plot X_1
    ax1.plot([0, 0.5], [-1, -1], 'b-')
    ax1.plot([0.5, 0.5], [-1, 1], 'b--')
    ax1.plot([0.5, 1], [1, 1], 'b-')
    ax1.set_title('$X_1(\omega)$')
    ax1.set_xlabel('$\omega$')
    ax1.set_xticks([0, 0.5, 1])
    ax1.set_xticklabels(['0', '1/2', '1'])
    ax1.set_yticks([-1, 1])
    ax1.grid(True, linestyle=':')
    # Plot X_2
    ax2.plot([0, 0.25], [-1, -1], 'r-')
    ax2.plot([0.25, 0.25], [-1, 1], 'r--')
    ax2.plot([0.25, 0.5], [1, 1], 'r-')
    ax2.plot([0.5, 0.5], [1, -1], 'r--')
    ax2.plot([0.5, 0.75], [-1, -1], 'r-')
    ax2.plot([0.75, 0.75], [-1, 1], 'r--')
    ax2.plot([0.75, 1], [1, 1], 'r-')
    ax2.set_title('$X_2(\omega)$')
    ax2.set_xlabel('$\omega$')
    ax2.set_xticks([0, 0.25, 0.5, 0.75, 1])
    ax2.set_xticklabels(['0', '1/4', '1/2', '3/4', '1'])
    ax2.grid(True, linestyle=':')
    plt.savefig('rademacher_plots.png')
    plt.close()


def generate_proba_return_zero():
    """Chapter 4: Probabilité de retour à l'origine."""
    #save_to: proba_return_zero.png
    k = np.arange(1, 51)
    p_s2k = comb(2 * k, k) / (2**(2 * k))
    stirling_approx = 1 / np.sqrt(np.pi * k)
    plt.figure(figsize=(10, 6))
    markerline, stemlines, baseline = plt.stem(2 * k, p_s2k, label='$P(S_{2k}=0)$', basefmt=" ")
    plt.setp(stemlines, 'color', plt.getp(markerline,'color'))
    plt.setp(stemlines, 'linestyle', 'dotted')
    plt.plot(2*k, stirling_approx, 'r--', label='Approximation de Stirling $\\frac{1}{\sqrt{\\pi k}}$')
    plt.title("Probabilité de retour à l'origine pour une marche aléatoire 1D")
    plt.xlabel("Nombre de pas (2k)")
    plt.ylabel("Probabilité")
    plt.legend()
    plt.grid(True, linestyle=':')
    plt.xlim(0, 102)
    plt.ylim(0)
    plt.savefig('proba_return_zero.png')
    plt.close()


def generate_convergence_en_loi_exemple():
    """Chapter 8: Convergence en loi exemple."""
    #save_to: convergence_en_loi_exemple.png
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    # Plot for X_2n
    ax1.plot([0, 0], [0, 1], 'b-', lw=2)
    ax1.plot([0, 0.5], [1, 1], 'b-', lw=2)
    ax1.plot([0.5, 0.5], [1, 0], 'b-', lw=2, label=r'$X_{2n}$')
    ax1.plot([0.5, 1], [0, 0], 'b-', lw=2)
    ax1.set_xlim(-0.1, 1.1)
    ax1.set_ylim(-0.1, 1.2)
    ax1.set_xticks([0, 0.5, 1])
    ax1.set_xticklabels(['0', r'$\frac{1}{2}$', '1'])
    ax1.set_yticks([0, 1])
    ax1.set_title(r'$X_{2n}$')
    ax1.spines['left'].set_position('zero')
    ax1.spines['bottom'].set_position('zero')
    ax1.spines['right'].set_color('none')
    ax1.spines['top'].set_color('none')
    ax1.xaxis.set_ticks_position('bottom')
    ax1.yaxis.set_ticks_position('left')
    ax1.plot(1, 0, ">k", transform=ax1.get_yaxis_transform(), clip_on=False)
    ax1.plot(0, 1, "^k", transform=ax1.get_xaxis_transform(), clip_on=False)
    # Plot for X_2n+1
    ax2.plot([0, 0.5], [0, 0], 'b-', lw=2)
    ax2.plot([0.5, 0.5], [0, 1], 'b-', lw=2, label=r'$X_{2n+1}$')
    ax2.plot([0.5, 1], [1, 1], 'b-', lw=2)
    ax2.plot([1, 1], [1, 0], 'b-', lw=2)
    ax2.set_xlim(-0.1, 1.1)
    ax2.set_ylim(-0.1, 1.2)
    ax2.set_xticks([0, 0.5, 1])
    ax2.set_xticklabels(['0', r'$\frac{1}{2}$', '1'])
    ax2.set_yticks([0, 1])
    ax2.set_title(r'$X_{2n+1}$')
    ax2.spines['left'].set_position('zero')
    ax2.spines['bottom'].set_position('zero')
    ax2.spines['right'].set_color('none')
    ax2.spines['top'].set_color('none')
    ax2.xaxis.set_ticks_position('bottom')
    ax2.yaxis.set_ticks_position('left')
    ax2.plot(1, 0, ">k", transform=ax2.get_yaxis_transform(), clip_on=False)
    ax2.plot(0, 1, "^k", transform=ax2.get_xaxis_transform(), clip_on=False)
    plt.tight_layout()
    plt.savefig('convergence_en_loi_exemple.png')
    plt.close()


def generate_cdf_examples():
    """Chapter 8: Exemples de fonctions de répartition."""
    #save_to: cdf_examples.png
    fig, axes = plt.subplots(2, 3, figsize=(15, 8))
    fig.suptitle('Exemples de fonctions de répartition', fontsize=16)
    # Bernoulli(p)
    p = 0.6
    ax = axes[0, 0]
    ax.plot([-2, 0], [0, 0], 'b-')
    ax.plot([0, 1], [1-p, 1-p], 'b-')
    ax.plot([1, 3], [1, 1], 'b-')
    ax.plot([0, 0], [0, 1-p], 'b--')
    ax.plot([1, 1], [1-p, 1], 'b--')
    ax.scatter([0, 1], [1-p, 1], facecolors='b', edgecolors='b', zorder=5)
    ax.scatter([0, 1], [0, 1-p], facecolors='white', edgecolors='b', zorder=5)
    ax.set_title('Bernoulli(p=0.6)')
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1-p, 1])
    ax.set_yticklabels(['0', '1-p', '1'])
    ax.set_ylim(-0.1, 1.1)
    ax.grid(True, linestyle=':')
    # Uniforme discrète sur {1,...,n}
    n = 5
    ax = axes[0, 1]
    x_vals = np.arange(0, n + 2, 1)
    y_vals = np.zeros_like(x_vals, dtype=float)
    for i, x in enumerate(x_vals):
        if x < 1:
            y_vals[i] = 0
        elif x >= n:
            y_vals[i] = 1
        else:
            y_vals[i] = np.floor(x) / n
    for i in range(len(x_vals) - 1):
        ax.plot([x_vals[i], x_vals[i+1]], [y_vals[i], y_vals[i]], 'b-')
    for i in range(1, n + 1):
        ax.scatter(i, i/n, facecolors='b', edgecolors='b', zorder=5)
        ax.scatter(i, (i-1)/n, facecolors='white', edgecolors='b', zorder=5)
    ax.set_title('Uniforme sur {1,...,5}')
    ax.set_xticks(range(n + 2))
    ax.set_yticks([k/n for k in range(n + 1)])
    ax.set_ylim(-0.1, 1.1)
    ax.grid(True, linestyle=':')
    # Uniforme continue sur [0,1]
    ax = axes[0, 2]
    x = np.linspace(-1, 2, 400)
    y = np.piecewise(x, [x < 0, (x >= 0) & (x <= 1), x > 1], [0, lambda x: x, 1])
    ax.plot(x, y, 'b-')
    ax.set_title('Uniforme sur [0,1]')
    ax.set_ylim(-0.1, 1.1)
    ax.set_xticks([0,1])
    ax.grid(True, linestyle=':')
    # Exponentielle(1)
    ax = axes[1, 0]
    x = np.linspace(-1, 4, 400)
    y = np.piecewise(x, [x < 0, x >= 0], [0, lambda x: 1 - np.exp(-x)])
    ax.plot(x, y, 'b-')
    ax.set_title('Exponentielle(1)')
    ax.set_ylim(-0.1, 1.1)
    ax.grid(True, linestyle=':')
    # Normale(0,1)
    ax = axes[1, 1]
    x = np.linspace(-3, 3, 400)
    y = norm.cdf(x, 0, 1)
    ax.plot(x, y, 'b-')
    ax.set_title('Normale(0,1)')
    ax.set_ylim(-0.1, 1.1)
    ax.grid(True, linestyle=':')
    ax.axhline(0.5, color='gray', linestyle='--')
    ax.axvline(0, color='gray', linestyle='--')
    # Placeholder for the 6th plot (or remove it)
    axes[1, 2].axis('off')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig('cdf_examples.png')
    plt.close()


def generate_cantor_construction():
    """Chapter 8: Construction de la fonction de Cantor."""
    #save_to: cantor_construction.png
    def cantor_function_recursive(ax, x_start, x_end, y_start, y_end, level):
        if level == 0:
            ax.plot([x_start, x_end], [y_start, y_end], 'b-')
            return
        x_third = x_start + (x_end - x_start) / 3
        x_two_thirds = x_start + 2 * (x_end - x_start) / 3
        y_mid = y_start + (y_end - y_start) / 2
        cantor_function_recursive(ax, x_start, x_third, y_start, y_mid, level - 1)
        ax.plot([x_third, x_two_thirds], [y_mid, y_mid], 'b-')
        cantor_function_recursive(ax, x_two_thirds, x_end, y_mid, y_end, level - 1)

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4))
    # F1
    ax1.plot([0, 1], [0, 1], 'b-')
    ax1.set_title('$F_1$')
    ax1.set_aspect('equal', 'box')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    # F2
    ax2.plot([0, 1/3.], [0, 0.5], 'b-')
    ax2.plot([1/3., 2/3.], [0.5, 0.5], 'b-')
    ax2.plot([2/3., 1], [0.5, 1], 'b-')
    ax2.set_title('$F_2$')
    ax2.set_aspect('equal', 'box')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.set_xticks([0, 1/3, 2/3, 1])
    ax2.set_xticklabels(['0', '1/3', '2/3', '1'])
    ax2.set_yticks([0, 0.5, 1])
    ax2.set_yticklabels(['0', '1/2', '1'])
    # F3
    cantor_function_recursive(ax3, 0, 1, 0, 1, 2)
    ax3.set_title('$F_3$')
    ax3.set_aspect('equal', 'box')
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig('cantor_construction.png')
    plt.close()


def generate_sandwich_functions():
    """Chapter 8: Fonctions sandwich pour la preuve."""
    #save_to: sandwich_functions.png
    x0 = 0
    epsilon = 0.5
    fig, ax = plt.subplots(figsize=(8, 5))
    # Plot the indicator function 1_{(-inf, x0]} (in blue)
    x_ind = np.linspace(-3, 3, 400)
    y_ind = (x_ind <= x0).astype(int)
    ax.plot(x_ind, y_ind, 'b', label=r'$\mathbf{1}_{(-\infty, x_0]}$')
    # Plot g_epsilon (in green)
    x_g = np.array([-3, x0, x0 + epsilon, 3])
    y_g = np.array([1, 1, 0, 0])
    ax.plot(x_g, y_g, 'g', label=r'$g_\epsilon$')
    # Plot f_epsilon (in red)
    x_f = np.array([-3, x0 - epsilon, x0, 3])
    y_f = np.array([1, 1, 0, 0])
    ax.plot(x_f, y_f, 'r', label=r'$f_\epsilon$')
    ax.set_title(r'Encadrement de $\mathbf{1}_{(-\infty, x_0]}$ par des fonctions continues')
    ax.set_xticks([x0 - epsilon, x0, x0 + epsilon])
    ax.set_xticklabels([r'$x_0-\epsilon$', r'$x_0$', r'$x_0+\epsilon$'])
    ax.set_yticks([0, 1])
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.legend()
    ax.set_ylim(-0.2, 1.4)
    plt.savefig('sandwich_functions.png')
    plt.close()


def generate_contour_integration():
    """Chapter 9: Contour d'intégration."""
    #save_to: contour_integration.png
    fig, ax = plt.subplots(figsize=(6, 4))
    # Contour rectangle
    R = 5
    u = 2
    rect = patches.Rectangle((-R, -u), 2*R, u, linewidth=0, facecolor='gray', alpha=0.1)
    ax.add_patch(rect)
    # Axes
    ax.axhline(0, color='black', lw=0.8)
    ax.axvline(0, color='black', lw=0.8)
    ax.set_xlabel('Re(z)')
    ax.set_ylabel('Im(z)')
    # Path
    ax.arrow(-R, 0, 2*R-0.2, 0, head_width=0.2, head_length=0.2, fc='blue', ec='blue', length_includes_head=True)
    ax.arrow(R, 0, 0, -u+0.2, head_width=0.2, head_length=0.2, fc='blue', ec='blue', length_includes_head=True)
    ax.arrow(R, -u, -2*R+0.2, 0, head_width=0.2, head_length=0.2, fc='blue', ec='blue', length_includes_head=True)
    ax.arrow(-R, -u, 0, u-0.2, head_width=0.2, head_length=0.2, fc='blue', ec='blue', length_includes_head=True)
    # Labels
    ax.text(0, 0.2, r'$\mathbb{R}$', ha='center')
    ax.text(0, -u - 0.4, r'$\mathbb{R} - iu$', ha='center')
    ax.text(R+0.2, -u/2, r'$\gamma_R$', va='center')
    ax.text(-R-0.6, -u/2, r'$\gamma_{-R}$', va='center')
    ax.set_xticks([-R, 0, R])
    ax.set_xticklabels(['-R', '0', 'R'])
    ax.set_yticks([-u, 0])
    ax.set_yticklabels(['-iu', '0'])
    ax.set_title("Contour d'intégration pour $I(u)$")
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_aspect('equal', adjustable='box')
    plt.tight_layout()
    plt.savefig('contour_integration.png')
    plt.close()


def generate_time_axis_impacts():
    """Chapter 11: Axe des temps avec impacts."""
    #save_to: time_axis_impacts.png
    fig, ax = plt.subplots(figsize=(8, 1))
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.yaxis.set_major_formatter(plt.NullFormatter())
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.set_xlim(-0.5, 6.5)
    ax.set_ylim(-0.5, 0.5)
    # Draw arrow
    ax.plot((6.4, 6.5), (0.05, 0), lw=1, color='k', clip_on=False)
    ax.plot((6.4, 6.5), (-0.05, 0), lw=1, color='k', clip_on=False)
    ax.text(6.7, -0.1, 'Temps', ha='center', va='center')
    # Plot impacts
    impacts = [1, 2.5, 3, 4.2, 5.5]
    ax.plot(impacts, [0]*len(impacts), 'x', color='black', markersize=8)
    plt.tight_layout()
    plt.savefig('time_axis_impacts.png', bbox_inches='tight', transparent=True)
    plt.close()


def generate_discrete_time_axis():
    """Chapter 11: Axe des temps discret."""
    #save_to: discrete_time_axis.png
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.yaxis.set_major_formatter(plt.NullFormatter())
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.set_xlim(-0.5, 5.5)
    ax.set_ylim(-0.5, 1)
    ax.axhline(0, color='black', lw=1)
    # Ticks and labels
    ticks = np.arange(0, 5)
    labels = [r'$0$', r'$\frac{1}{n}$', r'$\frac{2}{n}$', r'$\frac{3}{n}$', r'$\frac{4}{n}$']
    ax.set_xticks(ticks)
    ax.set_xticklabels(labels)
    ax.tick_params(axis='x', length=10)
    # Impacts
    impacts = [0.7, 1.2, 3.5, 3.6, 3.8]
    ax.plot(impacts, [0]*len(impacts), 'x', color='black', markersize=8)
    plt.tight_layout()
    plt.savefig('discrete_time_axis.png', bbox_inches='tight', transparent=True)
    plt.close()


def generate_Nn_t_plot():
    """Chapter 11: Trajectoire de N_n(t)."""
    #save_to: Nn_t_plot.png
    fig, ax = plt.subplots(figsize=(8, 4))
    t = np.array([0, 1.2, 1.2, 2.5, 2.5, 4.8, 4.8, 6])
    N_t = np.array([0, 0, 1, 1, 2, 2, 3, 3])
    ax.step(t, N_t, where='post', color='red')
    ax.plot([1.2, 2.5, 4.8], [1, 2, 3], 'ro')
    ax.plot([1.2, 2.5, 4.8], [0, 1, 2], 'ro', markerfacecolor='white')
    ax.set_xlabel('t')
    ax.set_ylabel(r'$N_n(t)$')
    ax.set_yticks([0, 1, 2, 3])
    ax.set_xticks([1.2, 2.5, 4.8])
    ax.set_xticklabels([r'$T_1$', r'$T_2$', r'$T_3$'])
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xlim(0, 6)
    ax.set_ylim(-0.2, 3.5)
    ax.grid(True, linestyle='--', alpha=0.6)
    plt.title("Trajectoire de $N_n(t)$")
    plt.savefig('Nn_t_plot.png')
    plt.close()


def generate_exp_survival():
    """Chapter 11: Fonction de survie exponentielle."""
    #save_to: exp_survival.png
    fig, ax = plt.subplots(figsize=(8, 3))
    x = np.linspace(0, 5, 400)
    y = np.exp(-0.8 * x)  # lambda = 0.8
    ax.plot(x, y, 'r-')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.set_xlabel('t', loc='right')
    ax.set_ylabel(r'$P(T>t)$', loc='top', rotation=0)
    # Example points
    t1 = 1.5
    t2 = 3
    ax.plot([t1, t2], [0, 0], 'k*')
    ax.text(t1, -0.2, r'$T_1$', ha='center')
    ax.text(t2, -0.2, r'$T_2$', ha='center')
    ax.hlines(y=np.exp(-0.8 * t1), xmin=0, xmax=t1, color='red', linestyle=':')
    ax.vlines(x=t1, ymin=0, ymax=np.exp(-0.8 * t1), color='red', linestyle=':')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1.1)
    plt.savefig('exp_survival.png')
    plt.close()


def generate_london_grid():
    """Chapter 11: Quadrillage de Londres."""
    #save_to: london_grid.png
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_xticks(np.arange(0, 6, 1))
    ax.set_yticks(np.arange(0, 5, 1))
    ax.grid(True, which='both', color='black', linestyle='-', linewidth=1)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(length=0)
    plt.savefig('london_grid.png')
    plt.close()


def generate_bus_arrival_timeline():
    """Chapter 11: Timeline des arrivées de bus."""
    #save_to: bus_arrival_timeline.png
    fig, ax = plt.subplots(figsize=(10, 2))
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.yaxis.set_major_formatter(plt.NullFormatter())
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.5, 1)
    # Draw axis
    ax.axhline(0, color='k', lw=1)
    ax.plot((10.4, 10.5), (0.05, 0), lw=1, color='k', clip_on=False)
    ax.plot((10.4, 10.5), (-0.05, 0), lw=1, color='k', clip_on=False)
    # Bus arrivals
    arrivals = [1, 3, 4, 7, 9]
    ax.plot(arrivals, [0]*len(arrivals), 'x', color='black', markersize=8, label='Arrivée de bus')
    # My arrival
    my_arrival_t = 5.5
    ax.plot([my_arrival_t], [0], 'ro', markersize=8, label='Mon arrivée')
    ax.text(my_arrival_t, -0.2, 't', ha='center')
    # Waiting time interval
    S_k, S_k1 = 4, 7
    ax.annotate('', xy=(S_k, 0.2), xytext=(S_k1, 0.2),
                arrowprops=dict(arrowstyle='<->', color='blue'))
    plt.savefig('bus_arrival_timeline.png', bbox_inches='tight', transparent=True)
    plt.close()


def generate_poisson_process_construction():
    """Chapter 11: Construction du processus de Poisson."""
    #save_to: poisson_process_construction.png
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    # Horizontal axis for S_n
    ax.axhline(0, color='black', lw=1)
    ax.set_xlim(-0.5, 10)
    ax.set_ylim(-0.5, 3)
    # Y_i values
    Y = np.array([2.0, 3.5, 1.5, 2.5])
    S = np.cumsum(Y)
    S = np.insert(S, 0, 0)
    # Plot S_n points
    ax.plot(S, [0]*len(S), 'r.')
    for i, s_val in enumerate(S):
        if i == 0: continue
        ax.text(s_val, -0.3, f'$S_{i}$')
    # Plot Y_i intervals
    for i in range(len(Y)):
        ax.annotate('', xy=(S[i], 0.2), xytext=(S[i+1], 0.2),
                    arrowprops=dict(arrowstyle='<->', color='black'))
        ax.text((S[i]+S[i+1])/2, 0.3, f'$Y_{i+1}$')
    # Plot N(t)
    t_vals = np.concatenate([S, [10]])
    n_vals = np.arange(len(t_vals))
    ax.step(t_vals, n_vals, where='post', color='red', label='N(t)')
    ax.set_yticks(range(5))
    ax.set_xlabel('t')
    ax.set_ylabel('N(t)')
    ax.legend()
    plt.title("Construction du Processus de Poisson N(t)")
    plt.savefig('poisson_process_construction.png')
    plt.close()


def main():
    """Generate all images for the textbook."""
    print("Generating images for MDD303 Probabilités...")
    
    # Chapter 4 images
    print("  - ex3_plot1.png")
    generate_ex3_plot1()
    print("  - ex3_plot2.png")
    generate_ex3_plot2()
    print("  - rademacher_plots.png")
    generate_rademacher_plots()
    print("  - proba_return_zero.png")
    generate_proba_return_zero()
    
    # Chapter 8 images
    print("  - convergence_en_loi_exemple.png")
    generate_convergence_en_loi_exemple()
    print("  - cdf_examples.png")
    generate_cdf_examples()
    print("  - cantor_construction.png")
    generate_cantor_construction()
    print("  - sandwich_functions.png")
    generate_sandwich_functions()
    
    # Chapter 9 images
    print("  - contour_integration.png")
    generate_contour_integration()
    
    # Chapter 11 images
    print("  - time_axis_impacts.png")
    generate_time_axis_impacts()
    print("  - discrete_time_axis.png")
    generate_discrete_time_axis()
    print("  - Nn_t_plot.png")
    generate_Nn_t_plot()
    print("  - exp_survival.png")
    generate_exp_survival()
    print("  - london_grid.png")
    generate_london_grid()
    print("  - bus_arrival_timeline.png")
    generate_bus_arrival_timeline()
    print("  - poisson_process_construction.png")
    generate_poisson_process_construction()
    
    print("Done! All images generated successfully.")


if __name__ == "__main__":
    main()

#region imports
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
#endregion

def main():
    """
    Main function to demonstrate plotting of normal distribution PDF and CDF.
    """
    # Parameters for the first normal distribution
    mu_a = 0.0
    sig_a = 1.0
    c_a = 1.0

    # Calculate the probability for x < c_a
    p_a = stats.norm(mu_a, sig_a).cdf(c_a)

    # Generate x values and compute PDF and CDF
    x_a = np.linspace(mu_a - 5 * sig_a, mu_a + 5 * sig_a, 500)
    cdf_a = np.array([stats.norm(mu_a, sig_a).cdf(x) for x in x_a])
    gnpdf_a = np.array([stats.norm(mu_a, sig_a).pdf(x) for x in x_a])

    # Plot PDF
    plt.subplots(2, 1, sharex=True)
    plt.subplot(2, 1, 1)
    plt.plot(x_a, gnpdf_a)
    plt.xlim(x_a.min(), x_a.max())
    plt.ylim(0, gnpdf_a.max() * 1.1)

    # Fill area under the curve up to c_a
    x_fill = np.linspace(mu_a - 5 * sig_a, c_a, 100)
    gnpdf_fill = np.array([stats.norm(mu_a, sig_a).pdf(x) for x in x_fill])
    ax = plt.gca()
    ax.fill_between(x_fill, gnpdf_fill, color='grey', alpha=0.3)

    # Annotations and formatting
    text_x = mu_a - 4 * sig_a
    text_y = 0.65 * gnpdf_a.max()
    plt.text(text_x, text_y, r'$f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$')
    arrow_x = (c_a - mu_a + 5 * sig_a) * 2 / 3 + mu_a - 5 * sig_a
    arrow_y = (stats.norm(mu_a, sig_a).pdf(arrow_x) / 2.0)
    plt.annotate('P(x<{:0.2f}|N({:0.2f},{:0.2f}))={:0.2f}'.format(c_a, mu_a, sig_a, p_a), size=8, xy=(c_a, p_a), xytext=(arrow_x, arrow_y), arrowprops=dict(facecolor='black', shrink=0.05))
    ax.tick_params(axis='both', which='both', direction='in', top=True, right=True, labelsize=10)
    ax.yaxis.set_label_text('f(x)')

    # Plot CDF
    plt.subplot(2, 1, 2)
    plt.plot(x_a, cdf_a)
    plt.ylim(0, 1)
    plt.ylabel('$\Phi(x)=\int_{-\infty}^{x}f(x)\mathrm{d}x$', size=12)
    plt.xlabel('x')
    plt.plot(c_a, p_a, 'o', markerfacecolor='white', markeredgecolor='red')
    ax = plt.gca()
    ax.tick_params(axis='both', direction='in', top=True, right=True, labelsize=10)
    ax.set_xlim(ax.get_xlim())

    ax.hlines(p_a, ax.get_xlim()[0], c_a, color='black', linewidth=1)
    ax.vlines(c_a, 0, p_a, color='black', linewidth=1)
    plt.show()

    # Parameters for the second normal distribution
    mu_b = 175.0
    sig_b = 3.0
    c_b = mu_b + 2 * sig_b

    # Calculate the probability for x < c_b
    p_b = 1.0 - stats.norm(mu_b, sig_b).cdf(c_b)

    # Generate x values and compute PDF and CDF
    x_b = np.linspace(mu_b - 5 * sig_b, mu_b + 5 * sig_b, 500)
    cdf_b = np.array([1.0 - stats.norm(mu_b, sig_b).cdf(x) for x in x_b])
    gnpdf_b = np.array([stats.norm(mu_b, sig_b).pdf(x) for x in x_b])

    # Plot PDF
    plt.subplots(2, 1, sharex=True)
    plt.subplot(2, 1, 1)
    plt.plot(x_b, gnpdf_b)
    plt.xlim(x_b.min(), x_b.max())
    plt.ylim(0, gnpdf_b.max() * 1.1)

    # Fill area under the curve from c_b to infinity
    x_fill = np.linspace(c_b, mu_b + 5 * sig_b, 100)
    gnpdf_fill = np.array([stats.norm(mu_b, sig_b).pdf(x) for x in x_fill])
    ax = plt.gca()
    ax.fill_between(x_fill, gnpdf_fill, color='grey', alpha=0.3)

    # Annotations and formatting
    text_x = c_b + sig_b
    text_y = 0.65 * gnpdf_b.max()
    plt.text(text_x, text_y, r'$f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$')
    arrow_x = (c_b + sig_b * 1 / 2)
    arrow_y = (stats.norm(mu_b, sig_b).pdf(arrow_x) / 2.0)
    plt.annotate('P(x<{:0.2f}|N({:0.2f},{:0.2f}))={:0.2f}'.format(c_b, mu_b, sig_b, p_b), size=8, xy=(c_b, p_b), xytext=(arrow_x, arrow_y), arrowprops=dict(facecolor='black', shrink=0.05))
    plt.ylabel('f(x)', size=12)
    ax.tick_params(axis='both', which='both', direction='in', top=True, right=True, labelsize=10)
    ax.yaxis.set_label_text('f(x)')

    # Plot CDF
    plt.subplot(2, 1, 2)
    plt.plot(x_b, cdf_b)
    plt.ylim(0, 1)
    plt.ylabel('$1-\Phi(x)=1-\int_{-\infty}^{x}f(x)\mathrm{d}x$', size=12)
    plt.xlabel('x')
    plt.plot(c_b, p_b, 'o', markerfacecolor='white', markeredgecolor='red')
    ax = plt.gca()
    ax.tick_params(axis='both', which='both', direction='in', top=True, right=True, labelsize=10)
    ax.set_xlim(ax.get_xlim())

    ax.hlines(p_b, ax.get_xlim()[0], c_b, color='black', linewidth=1)
    ax.vlines(c_b, 0, p_b, color='black', linewidth=1)
    plt.show()

if __name__ == "__main__":
    main()


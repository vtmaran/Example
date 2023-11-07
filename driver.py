from calculate_head_loss import calculate_head_loss


def main():

    # System Properties.
    e = 0.0002
    D = 0.25 # m
    rho = 1000 # kg/m^3
    mu = 6e-4 # Pa/s
    L = 110 # m
    V = 10 # m/s

    # Bisection Properties
    a = 0.0001
    b = 1
    tol = 0.0001
    maxiter = 50
    plot_output = True

    verbose = True
    head_loss = calculate_head_loss(e, D, rho, mu, L, V, a, b,
                                    tol=tol, maxiter=maxiter,
                                    plot_output=plot_output, verbose=verbose)

    print('The head loss due to frictional effects is '
          '{0:5.2f} (m/s)^2.'.format(head_loss))


if __name__ == '__main__':
    main()

/** Contains the equation solver class for eqn. (4). */

function logit(x, x_0, k, L) {
    /** Computes the logit of x.
     *
     * @param x: Input value at which to evaluate logit.
     * @param x_0: Midpoint of sigmoid function.
     * @param k: Steepness of sigmoid function.
     * @param L: Maximum value of sigmoid function.
     * @returns The logit of x.
     */
    return L / (1 + Math.exp(-k*(x - x_0)));
}


class Solver {
    /** Class for solving the robustness-adaptivity coupled ODE and computing its vector field. */

    /** Constructor.
     *
     * @param params: A dictionary whose elements are the parameters. The keys
     *     are: "alpha_r", "alpha_a", "q", "gamma_r0", "gamma_r2", "gamma_a",
     *          "beta_a", and "beta_r".
     * @param initial_values: A dict containing the values of the ODE's solution
     *     at time t=0. The keys are "robustness", "adaptivity", "time".
     */
    constructor(params, initial_values) {
        // All attributes are intended for the user to change externally
        this.params = params;
        this.initial_values = initial_values;
    }

    get solution() {
        /** Returns the solution to the ODE computed with a forward Euler method using the stored parameters.
         *
         * @returns Array with the three columns (i) robustness, (ii)
         *     adaptivity, and (iii) time. The rows correspond to the evaluation
         *     points.
         */

        // Initialize solution at time t=0
        let {robustness: curr_rob, adaptivity: curr_ada, time: curr_time} = this.initial_values;

        // Solve over time
        let solution = {robustness: [], adaptivity: [], time: []};
        while (curr_time <= this.params.t_max) {
            // Store current values (logit transformed)
            const {k_r, k_a, r_0, a_0} = this.params;
            solution.robustness.push(logit(curr_rob, r_0, k_r, 1));
            solution.adaptivity.push(logit(curr_ada, a_0, k_a, 1));
            solution.time.push(curr_time);

            // Compute next values (simultaneous update!)
            const delta_rob = this.computeDrDt(curr_rob, curr_ada) * this.params.step_size;
            const delta_ada = this.computeDaDt(curr_rob, curr_ada) * this.params.step_size;
            curr_rob += delta_rob;
            curr_ada += delta_ada;
            curr_time += this.params.step_size;
        }

        return solution;
    }

    // get vector_field() {
    //     /** Returns the vector field of the ODE.
    //      *
    //      * @returns ...
    //      */
    //
    //     ...
    // }

    computeDrDt(rob, ada) {
        /** Computes dr/dt according to eqn (4).
         *
         * @param rob Current robustness value.
         * @param ada Current adaptivity value.
         * @returns The computed value for dr/dt.
         */
        const {alpha_r, q, gamma_r0, gamma_r2, beta_a} = this.params;
        return alpha_r*(1 - q) + gamma_r0*rob - gamma_r2*Math.pow(rob, 3) - beta_a * ada;
    }


    computeDaDt(rob, ada) {
        /** Computes da/dt according to eqn (4).
         *
         * @param rob Current robustness value.
         * @param ada Current adaptivity value.
         * @returns The computed value for da/dt.
         */
        const {alpha_a, q, gamma_a, beta_r} = this.params;
        return alpha_a*q - gamma_a*ada + beta_r*rob;
    }
}

def kelly_criterion(win_probability, win_loss_ratio):
    """
    Calculate the Kelly Criterion.

    :param win_probability: The probability of a win.
    :param win_loss_ratio: The ratio of win amount to loss amount.
    :return: The optimal fraction of the portfolio to bet.
    """
    try:
        kelly_fraction = win_probability - (1 - win_probability) / win_loss_ratio
        return max(0, kelly_fraction)  # Ensure the fraction is not negative
    except ZeroDivisionError:
        # Handle case where win_loss_ratio is 0 to avoid division by zero error
        return 0

def exit_strategy(portfolio, risk_multiplier, reward_multiplier, win_probability, win_loss_ratio):
    """
    Generate a detailed exit strategy based on risk and reward preferences using Kelly Criterion.

    :param portfolio: Dictionary of coins and their quantities.
    :param risk_multiplier: User's risk multiplier.
    :param reward_multiplier: User's reward multiplier.
    :param win_probability: The probability of a win.
    :param win_loss_ratio: The ratio of win amount to loss amount.
    :return: Detailed exit strategy.
    """
    try:
        # Calculate the Kelly fraction
        kelly_fraction = kelly_criterion(win_probability, win_loss_ratio)
        print(f"Kelly Fraction: {kelly_fraction}")

        # Adjust Kelly fraction based on risk and reward multipliers
        adjusted_fraction = kelly_fraction * risk_multiplier * reward_multiplier
        print(f"Adjusted Fraction: {adjusted_fraction}")

        # Generate exit strategy
        strategy = {}
        for coin, quantity in portfolio.items():
            exit_amount = quantity * adjusted_fraction
            strategy[coin] = exit_amount
            print(f"{coin} Exit Amount: {exit_amount}")

        return strategy
    except Exception as e:
        # Print error message and return an empty strategy
        print(f"Error in exit_strategy calculation: {e}")
        return {}
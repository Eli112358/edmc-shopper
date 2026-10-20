# Roadmap

## Table of contents

- [Configuration](#configuration)
- [Fleet Carrier](#fleet-carrier)
- [Main loop](#main-loop)
- [Modes](#modes)
  - [Colonization](#colonization)
  - [Community Goals](#community-goals)
  - [General Trade](#general-trade)
  - [Missions](#missions)
- [Traveling Salesman Problem](#traveling-salesman-problem)

## Main loop

Overview of the main loop:

- Gather list of commodities
  - Depends on modes selected
- Search [Inara](https://inara.cz/elite)
- Plot route
  - Use [StarMap](https://edsm.net) for system coordinates
  - Solve [TSP](#traveling-salesman-problem)
- Show next step (buy/sell/jump/etc.)
- Copy next system to clipboard

## Traveling Salesman Problem

Develop custom algorithm to solve my situation

Criteria:

- Starting and ending points are often the same
- If using a fleet carrier, minimize its jumps
  - Jump the ship around small pockets where possible

## Configuration

Configurable items:

- Use [fleet carrier](#fleet-carrier)
- [Modes](#modes)

## Modes

Enable each independently to allow profit from [general trade](#general-trade) alongside [colonization](#colonization), for example

List of operating modes:

- [General Trade](#general-trade)
- [Colonization](#colonization)
- [Community Goals](#community-goals)
- [Missions](#missions)

### General Trade

Buy low, sell high... for a profit

I am aware of the [feature on Inara](https://inara.cz/elite/market-traderoutes/). This plugin plans to automate this (as much as possible) by using that Inara feature, displaying the next step (buy/sell/jump/etc.), and copying the next system to the clipboard

### Colonization

Fulfill most needed commodity first. Also minimize trips by filling cargo with other commodities that fit

### Community Goals

Sometimes a community goal involves commodities

### Missions

For those missions that involve commodities

## Fleet carrier

If available and configured to use, then use it

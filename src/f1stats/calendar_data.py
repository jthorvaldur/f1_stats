"""2026 F1 calendar and regulations reference data."""

CALENDAR_2026 = [
    {"round": 1, "name": "Australian Grand Prix", "dates": "06-08 Mar", "circuit": "Albert Park Grand Prix Circuit", "circuit_id": "albert_park", "city": "Melbourne", "country": "Australia", "sprint": False},
    {"round": 2, "name": "Chinese Grand Prix", "dates": "13-15 Mar", "circuit": "Shanghai International Circuit", "circuit_id": "shanghai", "city": "Shanghai", "country": "China", "sprint": True},
    {"round": 3, "name": "Japanese Grand Prix", "dates": "27-29 Mar", "circuit": "Suzuka Circuit", "circuit_id": "suzuka", "city": "Suzuka", "country": "Japan", "sprint": False},
    {"round": 4, "name": "Miami Grand Prix", "dates": "01-03 May", "circuit": "Miami International Autodrome", "circuit_id": "miami", "city": "Miami", "country": "USA", "sprint": True},
    {"round": 5, "name": "Canadian Grand Prix", "dates": "22-24 May", "circuit": "Circuit Gilles Villeneuve", "circuit_id": "villeneuve", "city": "Montreal", "country": "Canada", "sprint": True},
    {"round": 6, "name": "Monaco Grand Prix", "dates": "05-07 Jun", "circuit": "Circuit de Monaco", "circuit_id": "monaco", "city": "Monte Carlo", "country": "Monaco", "sprint": False},
    {"round": 7, "name": "Spanish Grand Prix (Catalunya)", "dates": "12-14 Jun", "circuit": "Circuit de Barcelona-Catalunya", "circuit_id": "barcelona", "city": "Barcelona", "country": "Spain", "sprint": False},
    {"round": 8, "name": "Austrian Grand Prix", "dates": "26-28 Jun", "circuit": "Red Bull Ring", "circuit_id": "red_bull_ring", "city": "Spielberg", "country": "Austria", "sprint": False},
    {"round": 9, "name": "British Grand Prix", "dates": "03-05 Jul", "circuit": "Silverstone Circuit", "circuit_id": "silverstone", "city": "Silverstone", "country": "Great Britain", "sprint": True},
    {"round": 10, "name": "Belgian Grand Prix", "dates": "17-19 Jul", "circuit": "Circuit de Spa-Francorchamps", "circuit_id": "spa", "city": "Spa", "country": "Belgium", "sprint": False},
    {"round": 11, "name": "Hungarian Grand Prix", "dates": "24-26 Jul", "circuit": "Hungaroring", "circuit_id": "hungaroring", "city": "Budapest", "country": "Hungary", "sprint": False},
    {"round": 12, "name": "Dutch Grand Prix", "dates": "21-23 Aug", "circuit": "Circuit Zandvoort", "circuit_id": "zandvoort", "city": "Zandvoort", "country": "Netherlands", "sprint": True},
    {"round": 13, "name": "Italian Grand Prix", "dates": "04-06 Sep", "circuit": "Autodromo Nazionale Monza", "circuit_id": "monza", "city": "Monza", "country": "Italy", "sprint": False},
    {"round": 14, "name": "Spanish Grand Prix (Madrid)", "dates": "11-13 Sep", "circuit": "Madrid Street Circuit", "circuit_id": "madrid", "city": "Madrid", "country": "Spain", "sprint": False},
    {"round": 15, "name": "Azerbaijan Grand Prix", "dates": "24-26 Sep", "circuit": "Baku City Circuit", "circuit_id": "baku", "city": "Baku", "country": "Azerbaijan", "sprint": False},
    {"round": 16, "name": "Singapore Grand Prix", "dates": "09-11 Oct", "circuit": "Marina Bay Street Circuit", "circuit_id": "singapore", "city": "Singapore", "country": "Singapore", "sprint": True},
    {"round": 17, "name": "United States Grand Prix", "dates": "23-25 Oct", "circuit": "Circuit of The Americas", "circuit_id": "americas", "city": "Austin", "country": "USA", "sprint": False},
    {"round": 18, "name": "Mexican Grand Prix", "dates": "30 Oct-01 Nov", "circuit": "Autodromo Hermanos Rodriguez", "circuit_id": "rodriguez", "city": "Mexico City", "country": "Mexico", "sprint": False},
    {"round": 19, "name": "Sao Paulo Grand Prix", "dates": "06-08 Nov", "circuit": "Autodromo Jose Carlos Pace", "circuit_id": "interlagos", "city": "Sao Paulo", "country": "Brazil", "sprint": False},
    {"round": 20, "name": "Las Vegas Grand Prix", "dates": "19-21 Nov", "circuit": "Las Vegas Strip Circuit", "circuit_id": "las_vegas", "city": "Las Vegas", "country": "USA", "sprint": False},
    {"round": 21, "name": "Qatar Grand Prix", "dates": "27-29 Nov", "circuit": "Lusail International Circuit", "circuit_id": "losail", "city": "Lusail", "country": "Qatar", "sprint": False},
    {"round": 22, "name": "Abu Dhabi Grand Prix", "dates": "04-06 Dec", "circuit": "Yas Marina Circuit", "circuit_id": "yas_marina", "city": "Abu Dhabi", "country": "UAE", "sprint": False},
]

REGULATION_CHANGES = {
    "power_unit": {
        "title": "Power Unit Revolution",
        "changes": [
            {"what": "MGU-H deleted", "from": "Motor Generator Unit - Heat (recovered exhaust energy)", "to": "Removed entirely", "implication": "Simpler, cheaper PU. Turbo lag returns. New manufacturers (Audi, Ford) can enter without mastering the most complex component."},
            {"what": "MGU-K tripled", "from": "120 kW (161 hp)", "to": "350 kW (469 hp)", "implication": "Nearly half the car's power is now electric. Massive energy recovery under braking. Changes braking character fundamentally."},
            {"what": "Battery capacity doubled", "from": "4 MJ usable per lap", "to": "9 MJ usable per lap", "implication": "Longer electric-only running possible. Energy management becomes a key strategy differentiator."},
            {"what": "ICE power reduced", "from": "~550 kW", "to": "~400 kW", "implication": "Combined power stays similar (~750 kW total) but the split shifts to electric. ICE is less dominant."},
            {"what": "Sustainable fuel mandate", "from": "E10 (10% ethanol blend)", "to": "100% sustainable fuel", "implication": "Zero net carbon from fuel. All teams run identical fuel spec. New combustion characteristics affect engine tuning."},
        ],
    },
    "aero": {
        "title": "Active Aerodynamics",
        "changes": [
            {"what": "Active front and rear wings", "from": "Fixed aero (only DRS on rear wing)", "to": "Full-time active aero — wings adjust angle continuously", "implication": "Cars switch between high-downforce (corners) and low-drag (straights) automatically. Fundamentally changes car behavior."},
            {"what": "DRS removed", "from": "Drag Reduction System (rear wing only, within 1s)", "to": "Replaced by 'Overtake Mode' + active aero", "implication": "No more DRS zones. Instead, following cars get energy bonus. Active aero provides drag reduction everywhere."},
            {"what": "Z-Mode / X-Mode", "from": "Single aero configuration", "to": "Z-Mode (high downforce, corners) / X-Mode (low drag, straights)", "implication": "Car automatically transitions between modes. The transition speed and smoothness becomes a design differentiator."},
            {"what": "Downforce cut 30%", "from": "~2000 kg at 250 km/h", "to": "~1400 kg at 250 km/h", "implication": "Cars are less planted in corners. More driver skill required. Closer racing because less aero wake disruption."},
            {"what": "Drag cut 55%", "from": "High drag coefficient", "to": "55% lower drag", "implication": "Higher top speeds on straights. Better fuel efficiency. Cars are faster in a straight line but slower in corners."},
        ],
    },
    "chassis": {
        "title": "Smaller, Lighter Cars",
        "changes": [
            {"what": "Minimum weight", "from": "800 kg (2025)", "to": "768 kg (2026)", "implication": "32 kg lighter. Teams struggle to meet target — most start overweight. Weight reduction is an ongoing development battle."},
            {"what": "Wheelbase shortened", "from": "3.6 m maximum", "to": "3.4 m maximum (-200 mm)", "implication": "More agile cars. Better direction changes. Cars look noticeably shorter."},
            {"what": "Car width reduced", "from": "2.0 m", "to": "1.9 m (-100 mm)", "implication": "Narrower cars. More room for overtaking. Changed aerodynamic characteristics."},
            {"what": "Tyre width reduced", "from": "305 mm front / 405 mm rear", "to": "280 mm front / 375 mm rear", "implication": "Less mechanical grip. Combined with lower downforce, makes cars more challenging to drive."},
            {"what": "Floor width reduced", "from": "1.6 m", "to": "1.45 m (-150 mm)", "implication": "Less ground effect. Reduced dependency on underbody aero. Cars less sensitive to ride height."},
        ],
    },
    "sporting": {
        "title": "Sporting Regulations",
        "changes": [
            {"what": "Overtake Mode", "from": "DRS within 1 second", "to": "Energy bonus when within 1s at detection point, lasts full next lap", "implication": "Attacking car gets +0.5 MJ extra energy. More strategic than DRS — driver chooses when to deploy."},
            {"what": "Boost Button", "from": "No equivalent", "to": "Manual energy deployment override", "implication": "Drivers can override automatic energy management for attack/defense. Adds tactical dimension to wheel-to-wheel racing."},
            {"what": "Sprint format unchanged", "from": "6 Sprint weekends (2025)", "to": "6 Sprint weekends (China, Miami, Canada, GB, Netherlands, Singapore)", "implication": "Sprint format stable. Extra points available at 6 venues. 36 points for top 8 finishers."},
            {"what": "Cost cap", "from": "$135M (2025)", "to": "$135M (2026, unchanged)", "implication": "Same budget ceiling despite massive new regulations. Teams must develop entirely new cars within existing budgets."},
            {"what": "New teams", "from": "10 teams / 20 cars", "to": "11 teams / 22 cars", "implication": "Cadillac F1 (GM/Andretti) enters as 11th team. First new constructor since Haas (2016). 22 cars on grid."},
        ],
    },
}

RACE_WEEKEND_FORMAT = {
    "standard": {
        "friday": [
            {"session": "Free Practice 1", "duration": "60 min", "purpose": "Car setup, tire evaluation, data collection. Teams test different configurations."},
            {"session": "Free Practice 2", "duration": "60 min", "purpose": "Race simulation runs, long-run pace evaluation, fine-tuning setup."},
        ],
        "saturday": [
            {"session": "Free Practice 3", "duration": "60 min", "purpose": "Final setup adjustments before qualifying. Often disrupted by weather or red flags."},
            {"session": "Qualifying", "duration": "~60 min", "purpose": "Sets the grid for Sunday's race. Three knockout rounds: Q1 (18 min), Q2 (15 min), Q3 (12 min)."},
        ],
        "sunday": [
            {"session": "Grand Prix", "duration": "~90 min / 305 km", "purpose": "The race. Maximum 2 hours. Points: 25-18-15-12-10-8-6-4-2-1."},
        ],
    },
    "sprint": {
        "friday": [
            {"session": "Free Practice 1", "duration": "60 min", "purpose": "Only practice session. Must cover setup, long runs, and qualifying prep in one hour."},
            {"session": "Sprint Qualifying", "duration": "~36 min", "purpose": "Sets Sprint grid. SQ1 (12 min) → SQ2 (10 min) → SQ3 (8 min). Medium tyres in SQ1/SQ2, softs in SQ3."},
        ],
        "saturday": [
            {"session": "Sprint Race", "duration": "~30 min / 100 km", "purpose": "One-third distance race. No mandatory pit stop. Points: 8-7-6-5-4-3-2-1 for top 8."},
            {"session": "Qualifying", "duration": "~60 min", "purpose": "Sets Grand Prix grid. Q1 (18 min) → Q2 (15 min) → Q3 (12 min). Independent of Sprint result."},
        ],
        "sunday": [
            {"session": "Grand Prix", "duration": "~90 min / 305 km", "purpose": "Full race. Grid from Saturday qualifying, not Sprint finishing order."},
        ],
    },
    "qualifying_format": {
        "Q1": {"duration": "18 min", "eliminated": 5, "remaining": 15, "tyre": "Free choice", "desc": "All 22 drivers. Slowest 7 are eliminated (positions 16-22)."},
        "Q2": {"duration": "15 min", "eliminated": 5, "remaining": 10, "tyre": "Free choice", "desc": "15 remaining drivers. Slowest 5 eliminated (positions 11-15)."},
        "Q3": {"duration": "12 min", "eliminated": 0, "remaining": 10, "tyre": "Free choice", "desc": "Top 10 shootout. Fastest driver takes pole position."},
    },
    "points": {
        "race": {"1": 25, "2": 18, "3": 15, "4": 12, "5": 10, "6": 8, "7": 6, "8": 4, "9": 2, "10": 1},
        "sprint": {"1": 8, "2": 7, "3": 6, "4": 5, "5": 4, "6": 3, "7": 2, "8": 1},
    },
}

CIRCUIT_DETAILS = {
    "albert_park": {"name": "Albert Park", "city": "Melbourne", "country": "Australia", "length_km": 5.278, "laps": 58, "turns": 14, "type": "street-park", "drs_zones": 0, "first_gp": 1996, "lap_record": "1:20.235 (Leclerc, 2024)", "description": "Fast, flowing layout around a lake in a public park. Mix of high-speed sweeps and tight chicanes. Resurfaced and reconfigured in 2022 to promote overtaking. The season opener traditionally produces drama."},
    "shanghai": {"name": "Shanghai International Circuit", "city": "Shanghai", "country": "China", "length_km": 5.451, "laps": 56, "turns": 16, "type": "permanent", "drs_zones": 0, "first_gp": 2004, "lap_record": "1:32.238 (M. Schumacher, 2004)", "description": "Hermann Tilke design with the famous snail-shell Turn 1-2-3 complex. Long back straight rewards power. Heavy braking zones create overtaking opportunities. Weather can be unpredictable."},
    "suzuka": {"name": "Suzuka Circuit", "city": "Suzuka", "country": "Japan", "length_km": 5.807, "laps": 53, "turns": 18, "type": "permanent", "drs_zones": 0, "first_gp": 1987, "lap_record": "1:30.983 (de Vries, 2023 FP)", "description": "The drivers' favorite. Figure-eight layout with Esses, Degner curves, 130R, and the Casio Triangle. Extremely high downforce demands. Rewards car balance and driver commitment. One of the few circuits where the track crosses over itself."},
    "miami": {"name": "Miami International Autodrome", "city": "Miami", "country": "USA", "length_km": 5.412, "laps": 57, "turns": 19, "type": "street-park", "drs_zones": 0, "first_gp": 2022, "lap_record": "1:29.708 (Verstappen, 2023)", "description": "Built around Hard Rock Stadium. Mix of high-speed straights and technical sections. Turn 17 hairpin is the primary overtaking spot. Bumpy surface challenges car setup. Florida heat affects tire degradation."},
    "villeneuve": {"name": "Circuit Gilles Villeneuve", "city": "Montreal", "country": "Canada", "length_km": 4.361, "laps": 70, "turns": 14, "type": "semi-permanent", "drs_zones": 0, "first_gp": 1978, "lap_record": "1:13.078 (Bottas, 2019)", "description": "On Ile Notre-Dame island. Stop-start layout with heavy braking zones and long straights. The Wall of Champions at the final chicane has claimed many victims. Low downforce, high on brakes. Safety car frequency is highest on the calendar."},
    "monaco": {"name": "Circuit de Monaco", "city": "Monte Carlo", "country": "Monaco", "length_km": 3.337, "laps": 78, "turns": 19, "type": "street", "drs_zones": 0, "first_gp": 1950, "lap_record": "1:12.909 (Hamilton, 2021)", "description": "The crown jewel. Narrow streets, elevation changes, the tunnel, the swimming pool chicane. Qualifying is everything — overtaking is nearly impossible. The slowest circuit on the calendar but the most prestigious. Maximum downforce, minimum margin for error."},
    "barcelona": {"name": "Circuit de Barcelona-Catalunya", "city": "Barcelona", "country": "Spain", "length_km": 4.657, "laps": 66, "turns": 16, "type": "permanent", "drs_zones": 0, "first_gp": 1991, "lap_record": "1:18.149 (Verstappen, 2023)", "description": "The benchmark circuit. Used extensively for testing, so teams know it intimately. High-speed final sector, demanding Turn 3, and the challenging Turn 9-10 complex. A good indicator of true car performance because every team has extensive data."},
    "red_bull_ring": {"name": "Red Bull Ring", "city": "Spielberg", "country": "Austria", "length_km": 4.318, "laps": 71, "turns": 10, "type": "permanent", "drs_zones": 0, "first_gp": 1970, "lap_record": "1:05.619 (Sainz, 2020)", "description": "Short, fast, dramatic. Only 10 turns but significant elevation changes. Three heavy braking zones into uphill corners create overtaking opportunities. Altitude (700m) affects engine performance. Track limits are a constant talking point."},
    "silverstone": {"name": "Silverstone Circuit", "city": "Silverstone", "country": "Great Britain", "length_km": 5.891, "laps": 52, "turns": 18, "type": "permanent", "drs_zones": 0, "first_gp": 1950, "lap_record": "1:27.097 (Verstappen, 2024)", "description": "Home of British motorsport. Maggotts-Becketts-Chapel is the most demanding high-speed complex in F1. Copse and Stowe test courage. High-speed circuit that rewards aerodynamic efficiency. British weather adds unpredictability."},
    "spa": {"name": "Circuit de Spa-Francorchamps", "city": "Spa", "country": "Belgium", "length_km": 7.004, "laps": 44, "turns": 19, "type": "permanent", "drs_zones": 0, "first_gp": 1950, "lap_record": "1:46.286 (Bottas, 2018)", "description": "The longest circuit on the calendar. Eau Rouge/Raidillon is iconic — a compression into a blind, high-speed left-right-left over a crest. Long Kemmel Straight, the Bus Stop chicane, and Blanchimont. Micro-climates mean rain can hit one sector while another is dry."},
    "hungaroring": {"name": "Hungaroring", "city": "Budapest", "country": "Hungary", "length_km": 4.381, "laps": 70, "turns": 14, "type": "permanent", "drs_zones": 0, "first_gp": 1986, "lap_record": "1:16.627 (Hamilton, 2020)", "description": "Monaco without walls. Tight, twisty, low-speed. Extremely difficult to overtake. High downforce setup. Track position is king — qualifying pace matters enormously. Summer heat creates extreme tire degradation."},
    "zandvoort": {"name": "Circuit Zandvoort", "city": "Zandvoort", "country": "Netherlands", "length_km": 4.259, "laps": 72, "turns": 14, "type": "permanent", "drs_zones": 0, "first_gp": 1952, "lap_record": "1:11.097 (Hamilton, 2023)", "description": "Old-school circuit in the dunes. Banked final turn (18° banking) is unique in modern F1. Narrow, technical, rewards driver confidence. The Dutch fans create an electric atmosphere. Limited overtaking makes strategy critical."},
    "monza": {"name": "Autodromo Nazionale Monza", "city": "Monza", "country": "Italy", "length_km": 5.793, "laps": 53, "turns": 11, "type": "permanent", "drs_zones": 0, "first_gp": 1950, "lap_record": "1:21.046 (Barrichello, 2004)", "description": "The Temple of Speed. Lowest downforce configuration of the year. Long straights connected by chicanes. Slipstreaming battles are legendary. Parabolica (now Curva Alboreto) rewards bravery. The tifosi make it the most atmospheric race on the calendar."},
    "madrid": {"name": "Madrid Street Circuit", "city": "Madrid", "country": "Spain", "length_km": 5.473, "laps": 56, "turns": 18, "type": "street", "drs_zones": 0, "first_gp": 2026, "lap_record": "N/A (new circuit)", "description": "Brand new for 2026. Street circuit through the Spanish capital. Expected to feature a mix of high-speed sections along wide boulevards and tighter technical zones. First F1 race in Madrid. The newest addition to the calendar."},
    "baku": {"name": "Baku City Circuit", "city": "Baku", "country": "Azerbaijan", "length_km": 6.003, "laps": 51, "turns": 20, "type": "street", "drs_zones": 0, "first_gp": 2016, "lap_record": "1:43.009 (Leclerc, 2019)", "description": "The most dramatic street circuit. 2.2 km main straight produces extreme top speeds. Turn 8 castle section is impossibly narrow. Always produces chaotic races, safety cars, and surprise results. Walls on both sides leave zero margin."},
    "singapore": {"name": "Marina Bay Street Circuit", "city": "Singapore", "country": "Singapore", "length_km": 4.940, "laps": 62, "turns": 19, "type": "street", "drs_zones": 0, "first_gp": 2008, "lap_record": "1:35.867 (Hamilton, 2023)", "description": "The original night race. Humid, hot, physically brutal — drivers lose 3-4 kg per race. Bumpy surface, tight corners, no room for error. High downforce, low speed. Safety car probability is extremely high. One of the most demanding races on the calendar."},
    "americas": {"name": "Circuit of The Americas", "city": "Austin", "country": "USA", "length_km": 5.513, "laps": 56, "turns": 20, "type": "permanent", "drs_zones": 0, "first_gp": 2012, "lap_record": "1:36.169 (Leclerc, 2019)", "description": "Purpose-built for F1. Turn 1 uphill braking zone is iconic. The Esses (turns 3-6) demand commitment. Mix of high and low-speed corners tests all aspects of car performance. Bumpy surface has been a persistent issue."},
    "rodriguez": {"name": "Autodromo Hermanos Rodriguez", "city": "Mexico City", "country": "Mexico", "length_km": 4.304, "laps": 71, "turns": 17, "type": "permanent", "drs_zones": 0, "first_gp": 1963, "lap_record": "1:17.774 (Bottas, 2021)", "description": "At 2,240m altitude — the highest circuit on the calendar. Thin air reduces engine power by ~20% and downforce significantly. Unique challenge for power units and cooling. The stadium section through the baseball stadium is atmospheric. Peraltada corner is a classic."},
    "interlagos": {"name": "Autodromo Jose Carlos Pace", "city": "Sao Paulo", "country": "Brazil", "length_km": 4.309, "laps": 71, "turns": 15, "type": "permanent", "drs_zones": 0, "first_gp": 1973, "lap_record": "1:10.540 (Bottas, 2018)", "description": "Anti-clockwise, short, and dramatic. Senna S is a natural amphitheater. The long run down to Turn 4 is one of the best overtaking spots in F1. Elevation changes, unpredictable weather, and passionate fans. Counter-clockwise running uniquely stresses the left side of the car."},
    "las_vegas": {"name": "Las Vegas Strip Circuit", "city": "Las Vegas", "country": "USA", "length_km": 6.201, "laps": 50, "turns": 17, "type": "street", "drs_zones": 0, "first_gp": 2023, "lap_record": "1:35.490 (Piastri, 2024)", "description": "Night race on the Strip. 1.9 km main straight past the casinos produces extreme top speeds. Low-grip surface due to road paint and residual materials. Cold desert night temperatures challenge tire warm-up. The spectacle matches the racing."},
    "losail": {"name": "Lusail International Circuit", "city": "Lusail", "country": "Qatar", "length_km": 5.419, "laps": 57, "turns": 16, "type": "permanent", "drs_zones": 0, "first_gp": 2021, "lap_record": "1:24.319 (Verstappen, 2023)", "description": "Fast, flowing desert circuit. High-speed corners dominate — Turn 12-13-14 complex is taken nearly flat out. Extreme heat and abrasive surface destroy tires. Kerb severity caused tire failures in 2023, leading to modifications. Night race under floodlights."},
    "yas_marina": {"name": "Yas Marina Circuit", "city": "Abu Dhabi", "country": "UAE", "length_km": 5.281, "laps": 58, "turns": 16, "type": "permanent", "drs_zones": 0, "first_gp": 2009, "lap_record": "1:26.103 (Verstappen, 2021)", "description": "The season finale. Redesigned in 2021 to improve racing — chicane replaced by high-speed sweeper, new hairpin. Twilight race transitioning from daylight to floodlights. The Yas Hotel straddling the track is iconic. Often decides championships."},
}

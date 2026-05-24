"""HFT historical data — timeline, firms, technology evolution, market structure, microwave routes."""

TIMELINE = [
    {"year": 1969, "event": "Instinet founded", "category": "infrastructure", "detail": "First electronic communication network (ECN). Institutional block trading without exchange floor."},
    {"year": 1971, "event": "NASDAQ launches", "category": "infrastructure", "detail": "First electronic stock exchange. Quotes displayed on screens instead of ticker tape. Market makers connected via phone lines."},
    {"year": 1987, "event": "Black Monday — program trading blamed", "category": "regulation", "detail": "Portfolio insurance algorithms amplified the 22.6% single-day crash. First major scrutiny of automated trading. Circuit breakers introduced."},
    {"year": 1996, "event": "Island ECN launches", "category": "infrastructure", "detail": "Josh Levine's electronic limit order book. Sub-second execution. The template for modern electronic exchanges. Later acquired by NASDAQ."},
    {"year": 1998, "event": "SEC authorizes ECNs (Reg ATS)", "category": "regulation", "detail": "Alternative Trading Systems legitimized. Fragmentation begins — orders can execute on multiple venues, creating arbitrage opportunities."},
    {"year": 2000, "event": "Decimalization begins", "category": "regulation", "detail": "SEC mandates penny increments (from 1/16ths). Spreads collapse from $0.0625 to $0.01. Floor market makers lose edge. Speed becomes the new advantage."},
    {"year": 2001, "event": "Island ECN goes fully electronic", "category": "infrastructure", "detail": "Sub-millisecond matching engine. The first exchange where speed was a competitive advantage. HFT firms begin to form."},
    {"year": 2002, "event": "Automated Trading Desk (ATD) peaks", "category": "firms", "detail": "One of the first pure HFT firms. Trading ~6% of US equity volume by this point. Bought by Citadel in 2007."},
    {"year": 2004, "event": "Reg NMS proposed", "category": "regulation", "detail": "SEC proposes the National Market System regulation. Would create the 'order protection rule' requiring best price execution across all venues."},
    {"year": 2005, "event": "Reg NMS finalized", "category": "regulation", "detail": "Order Protection Rule (Rule 611): brokers must route to the venue with the best price. Creates massive incentive for speed — fastest firm captures the order. HFT era begins in earnest."},
    {"year": 2005, "event": "Getco founded (later KCG, now Virtu)", "category": "firms", "detail": "Daniel Tierney and Stephen Schuler. Electronic market-making across equities and futures. Would merge with Knight Capital in 2014 to form KCG, then Virtu."},
    {"year": 2006, "event": "NYSE goes electronic (Hybrid Market)", "category": "infrastructure", "detail": "NYSE transitions from floor-only to electronic matching. The last major holdout falls. Floor traders become largely ceremonial."},
    {"year": 2007, "event": "Spread Networks dark fiber (Chicago–NJ)", "category": "technology", "detail": "827-mile fiber optic cable, Chicago to New Jersey in 13.1ms (later 12.98ms). Cost $300M. The canonical latency arbitrage infrastructure investment."},
    {"year": 2007, "event": "CME Globex co-location launches", "category": "technology", "detail": "CME opens Aurora, IL data center with co-location racks. Firms can place servers feet from the matching engine. Latency drops from milliseconds to microseconds."},
    {"year": 2008, "event": "Financial crisis — HFT provides liquidity", "category": "regulation", "detail": "While banks pulled back, HFT market makers continued quoting. Spreads widened but markets stayed open. This earned HFT credibility with regulators — temporarily."},
    {"year": 2009, "event": "Flash Orders controversy", "category": "regulation", "detail": "Senator Schumer and SEC scrutinize 'flash orders' — sub-second peeks at order flow before public dissemination. BATS and NASDAQ suspend flash order programs."},
    {"year": 2009, "event": "Citadel Securities established", "category": "firms", "detail": "Ken Griffin spins out the market-making division. Would become the dominant US equity market maker — handling ~25% of all US equity volume by 2024."},
    {"year": 2010, "event": "Flash Crash — May 6", "category": "regulation", "detail": "DJIA drops 1000 points in minutes, recovers within 20 minutes. Waddell & Reed's E-mini S&P sell algorithm triggered a liquidity vacuum. HFT firms withdrew quotes en masse. Single-stock circuit breakers introduced."},
    {"year": 2010, "event": "HFT reaches ~60% of US equity volume", "category": "infrastructure", "detail": "Peak HFT market share in US equities. Every major exchange now co-located. Arms race in full swing."},
    {"year": 2011, "event": "Microwave networks begin", "category": "technology", "detail": "McKay Brothers and others build line-of-sight microwave relay towers between data centers. Chicago to NJ in ~8.5ms (vs 13ms fiber). Speed of light in air > speed in glass."},
    {"year": 2012, "event": "Knight Capital $440M loss", "category": "firms", "detail": "Software deployment error causes Knight's algo to buy high and sell low for 45 minutes. Loses $440M. Company rescued by Getco merger → KCG Group."},
    {"year": 2012, "event": "IEX founded", "category": "infrastructure", "detail": "Brad Katsuyama founds the 'anti-HFT' exchange with a 350-microsecond speed bump (38 miles of coiled fiber). Profiled in Michael Lewis's 'Flash Boys' (2014)."},
    {"year": 2013, "event": "Direct Edge merges with BATS", "category": "infrastructure", "detail": "Exchange consolidation. BATS Global Markets becomes the second-largest US equities exchange operator. Later acquired by CBOE."},
    {"year": 2014, "event": "Flash Boys published", "category": "regulation", "detail": "Michael Lewis's book puts HFT in the public consciousness. IEX popularity surges. FBI and DOJ launch investigations. Political pressure mounts."},
    {"year": 2014, "event": "Virtu Financial IPO filing", "category": "firms", "detail": "Virtu reveals it had only 1 losing day in 1,238 trading days. The perfect track record becomes both a marketing tool and regulatory red flag."},
    {"year": 2015, "event": "SEC approves IEX as national exchange", "category": "regulation", "detail": "IEX becomes the 13th US national securities exchange. The speed bump is approved. Debate about whether 'slowing down' markets is good policy."},
    {"year": 2015, "event": "FPGA-based trading systems become standard", "category": "technology", "detail": "Field-Programmable Gate Arrays process market data and generate orders in nanoseconds. Hardware, not software, becomes the bottleneck. Firms like Jump Trading invest heavily."},
    {"year": 2016, "event": "Jump Trading's microwave/millimeter wave network", "category": "technology", "detail": "Jump buys a radio tower in Hounslow, UK (near Heathrow) for London-Frankfurt microwave relay. Millimeter wave technology pushes latency below 4ms."},
    {"year": 2016, "event": "MiFID II proposed (EU)", "category": "regulation", "detail": "European regulation requiring algo trading firms to register, test algorithms, and maintain records. Market-making obligations. Takes effect January 2018."},
    {"year": 2017, "event": "Cryptocurrency HFT begins in earnest", "category": "technology", "detail": "Arbitrage between crypto exchanges becomes profitable. Latency advantages are huge — crypto exchange matching engines are orders of magnitude slower than traditional venues."},
    {"year": 2018, "event": "MiFID II takes effect", "category": "regulation", "detail": "European algo trading regulation. Tick size regime, market-making obligations, algo testing requirements. Increases compliance costs, benefits larger firms."},
    {"year": 2018, "event": "Laser communication networks", "category": "technology", "detail": "Anova Technologies and others experiment with free-space optical (laser) links between data centers. Lower latency than microwave in some conditions but weather-dependent."},
    {"year": 2019, "event": "Citadel Securities handles 25% of US equity volume", "category": "firms", "detail": "Single firm dominance unprecedented. Also becomes largest options market maker. Payment for order flow (PFOF) from retail brokers (Robinhood) becomes major revenue source."},
    {"year": 2020, "event": "COVID volatility — HFT profits surge", "category": "firms", "detail": "March 2020 volatility spike. Virtu reports $1.37B revenue in Q1 2020 alone (3x normal). HFT thrives in volatility — wider spreads and more price dislocations."},
    {"year": 2020, "event": "GameStop / meme stock phenomenon", "category": "regulation", "detail": "Retail trading surge via Robinhood. PFOF scrutiny intensifies. Citadel Securities' role as wholesale market maker debated in Congress."},
    {"year": 2021, "event": "SEC proposes equity market structure reform", "category": "regulation", "detail": "Chair Gensler proposes tick size changes, best execution rules, PFOF restrictions, and auction mechanisms for retail orders. Biggest structural reform since Reg NMS."},
    {"year": 2022, "event": "FTX collapse", "category": "infrastructure", "detail": "Crypto exchange FTX collapses in November. $8B customer funds missing. Jump Trading and other HFT firms suffer losses. Crypto market structure credibility damaged."},
    {"year": 2022, "event": "Jane Street revenue: $21.9B", "category": "firms", "detail": "Jane Street reports $21.9B in net trading revenue. Bond and ETF market making dominance. The firm's scale rivals major banks."},
    {"year": 2023, "event": "AI/ML integration accelerates", "category": "technology", "detail": "LLMs and transformer models begin supplementing traditional signal generation. Not replacing core HFT execution but enhancing alpha research, news parsing, and risk management."},
    {"year": 2024, "event": "SEC equity market reform finalized", "category": "regulation", "detail": "Tick size reduction (to $0.005 for liquid stocks), minimum quoting increments, enhanced best-execution requirements. Effective 2025-2026."},
    {"year": 2025, "event": "DeFi HFT on Hyperliquid, dYdX", "category": "technology", "detail": "On-chain order books with sub-second finality. MEV (Maximal Extractable Value) strategies. Searcher-builder-proposer architecture. HFT meets blockchain consensus."},
    {"year": 2026, "event": "Consolidated audit trail (CAT) fully operational", "category": "regulation", "detail": "SEC's Consolidated Audit Trail tracks every order, cancellation, and execution across all US equities and options venues. Complete market surveillance."},
]

FIRMS = [
    {"name": "Citadel Securities", "hq": "Miami/Chicago", "founded": 2002, "type": "Market Maker", "markets": "Equities, Options, FX, Crypto", "est_daily_volume": "$30B+", "notable": "Handles ~25% of US equity volume, ~40% of retail equity orders. Largest options market maker. Ken Griffin."},
    {"name": "Virtu Financial", "hq": "New York", "founded": 2008, "type": "Market Maker", "markets": "Equities, FX, Futures, Crypto", "est_daily_volume": "$15B+", "notable": "Only 1 losing day in 1,238 consecutive trading days (pre-IPO). Acquired KCG (Knight/Getco) in 2017."},
    {"name": "Jane Street", "hq": "New York", "founded": 2000, "type": "Prop Trading / Market Maker", "markets": "ETFs, Bonds, Equities, Crypto", "est_daily_volume": "$20B+", "notable": "$21.9B net trading revenue (2022). ETF arbitrage specialist. Dominant in bond markets. OCaml programming language."},
    {"name": "Jump Trading", "hq": "Chicago", "founded": 1999, "type": "Prop Trading", "markets": "Futures, Equities, Crypto, FX", "est_daily_volume": "$10B+", "notable": "Heavy infrastructure investor — microwave towers, FPGA farms, co-location. Jump Crypto division (post-FTX losses). DRW founder's son."},
    {"name": "Tower Research Capital", "hq": "New York", "founded": 1998, "type": "Prop Trading", "markets": "Equities, Futures, Options", "est_daily_volume": "$5B+", "notable": "Mark Gorton. One of the original HFT firms. Statistical arbitrage and market making."},
    {"name": "Two Sigma", "hq": "New York", "founded": 2001, "type": "Quant Hedge Fund", "markets": "Equities, Futures, Options", "est_daily_volume": "N/A", "notable": "$60B+ AUM. David Siegel and John Overdeck. Machine learning-heavy. Longer holding periods than pure HFT."},
    {"name": "DE Shaw", "hq": "New York", "founded": 1988, "type": "Quant Hedge Fund", "markets": "Multi-asset", "est_daily_volume": "N/A", "notable": "$60B+ AUM. David Shaw (computational biochemistry PhD). Jeff Bezos's first job out of Princeton. Pioneer of quantitative trading."},
    {"name": "Renaissance Technologies", "hq": "East Setauket, NY", "founded": 1982, "type": "Quant Hedge Fund", "markets": "Multi-asset", "est_daily_volume": "N/A", "notable": "Jim Simons (mathematician, Chern-Simons form). Medallion Fund: ~66% annual returns since 1988. Most successful fund in history. Closed to outside investors since 1993."},
    {"name": "Optiver", "hq": "Amsterdam", "founded": 1986, "type": "Market Maker", "markets": "Options, ETFs, Futures, Equities", "est_daily_volume": "$10B+", "notable": "Dutch options market-making tradition. Major in European and Asian markets. $8.3B profit in 2022."},
    {"name": "IMC Trading", "hq": "Amsterdam", "founded": 1989, "type": "Market Maker", "markets": "Options, ETFs, Bonds", "est_daily_volume": "$5B+", "notable": "Amsterdam options pit origins. Global market maker. Major in US options."},
    {"name": "Flow Traders", "hq": "Amsterdam", "founded": 2004, "type": "Market Maker", "markets": "ETFs, Bonds, Crypto", "est_daily_volume": "$5B+", "notable": "Publicly traded. ETF market making specialist. One of the first major firms to enter crypto market making."},
    {"name": "Hudson River Trading", "hq": "New York", "founded": 2002, "type": "Prop Trading / Market Maker", "markets": "Equities, Futures, Options", "est_daily_volume": "$8B+", "notable": "Heavy quantitative research focus. Historically low profile. Major US equity market maker."},
    {"name": "Susquehanna (SIG)", "hq": "Bala Cynwyd, PA", "founded": 1987, "type": "Prop Trading / Market Maker", "markets": "Options, ETFs, Equities", "est_daily_volume": "$10B+", "notable": "Jeff Yass. Options market-making roots. Game theory and poker culture. Major TikTok/ByteDance investor."},
    {"name": "XTX Markets", "hq": "London", "founded": 2015, "type": "Market Maker", "markets": "FX, Equities, Futures", "est_daily_volume": "$10B+", "notable": "Founded by Alex Gerko (ex-GSA Capital). Largest non-bank FX market maker. ML-heavy. Top-3 global FX liquidity provider."},
    {"name": "Wolverine Trading", "hq": "Chicago", "founded": 1994, "type": "Prop Trading / Market Maker", "markets": "Options, Futures, Equities", "est_daily_volume": "$3B+", "notable": "Chicago options pit origins. Quantitative options pricing. Major in volatility markets."},
    {"name": "DRW Trading", "hq": "Chicago", "founded": 1992, "type": "Prop Trading", "markets": "Futures, Crypto, Fixed Income", "est_daily_volume": "$5B+", "notable": "Don Wilson. Chicago futures heritage. Cumberland (crypto division). Real estate ventures. Major in interest rate futures."},
    {"name": "Wintermute", "hq": "London", "founded": 2017, "type": "Market Maker", "markets": "Crypto (CEX + DEX)", "est_daily_volume": "$5B+", "notable": "Dominant crypto market maker. Both centralized and decentralized venue liquidity. DeFi native."},
    {"name": "Quantitative Brokers", "hq": "New York", "founded": 2008, "type": "Algo Execution", "markets": "Futures, Fixed Income", "est_daily_volume": "N/A", "notable": "Execution algorithm provider for futures. TWAP, VWAP, and adaptive algo development. Institutional client-facing."},
]

LATENCY_EVOLUTION = [
    {"year": 1995, "latency_ms": 1000, "medium": "Dial-up modem", "context": "Seconds to execute. Phone-based trading."},
    {"year": 2000, "latency_ms": 100, "medium": "T1 lines to exchanges", "context": "Electronic exchanges. Sub-second execution becomes possible."},
    {"year": 2005, "latency_ms": 10, "medium": "Co-located fiber", "context": "Servers in exchange data centers. Reg NMS drives speed competition."},
    {"year": 2007, "latency_ms": 1, "medium": "Optimized fiber + co-lo", "context": "Spread Networks. Sub-millisecond matching engines."},
    {"year": 2010, "latency_ms": 0.1, "medium": "FPGA + co-location", "context": "Hardware acceleration. FPGA processes market data in microseconds."},
    {"year": 2012, "latency_ms": 0.01, "medium": "Microwave + FPGA", "context": "McKay Brothers microwave. Chicago-NJ in 4.1ms one-way (vs 6.5ms fiber)."},
    {"year": 2015, "latency_ms": 0.005, "medium": "Millimeter wave + custom NIC", "context": "Kernel bypass networking. Custom network cards process packets in nanoseconds."},
    {"year": 2018, "latency_ms": 0.001, "medium": "Laser + FPGA + custom silicon", "context": "Sub-microsecond tick-to-trade. ASIC-based feed handlers."},
    {"year": 2023, "latency_ms": 0.0005, "medium": "Custom ASIC + integrated optics", "context": "Nanosecond-scale decisions. Physics limit (speed of light) becomes binding constraint."},
]

TECHNOLOGY_STACK = {
    "network": {
        "title": "Network Infrastructure",
        "layers": [
            {"name": "Fiber Optic", "latency": "~5μs/km", "cost": "$$", "weather": "Immune", "bandwidth": "Terabits/s", "desc": "Glass fiber. Speed of light in glass ≈ 200,000 km/s (0.67c). Reliable, high bandwidth, but slower than air."},
            {"name": "Microwave", "latency": "~3.3μs/km", "cost": "$$$", "weather": "Rain sensitive", "bandwidth": "~1 Gbps", "desc": "Line-of-sight radio. Speed of light in air ≈ 300,000 km/s. ~35% faster than fiber. Tower network requires clear path."},
            {"name": "Millimeter Wave", "latency": "~3.3μs/km", "cost": "$$$$", "weather": "Very sensitive", "bandwidth": "~10 Gbps", "desc": "60-90 GHz band. Higher bandwidth than microwave. Shorter range per hop. Used for critical last-mile links."},
            {"name": "Free-Space Optical (Laser)", "latency": "~3.3μs/km", "cost": "$$$$$", "weather": "Fog sensitive", "bandwidth": "~100 Gbps", "desc": "Laser links between rooftops/towers. Speed of light in air. Highest bandwidth of wireless options. Weather dependent."},
        ],
    },
    "hardware": {
        "title": "Compute Hardware",
        "layers": [
            {"name": "CPU (x86)", "latency": "~1-10μs", "flexibility": "Highest", "power": "150-300W", "desc": "General-purpose. Good for strategy logic, risk management. Too slow for critical path in modern HFT. Intel Xeon / AMD EPYC."},
            {"name": "GPU", "latency": "~10-100μs", "flexibility": "Medium", "power": "300-700W", "desc": "Parallel processing. Used for backtesting, ML training, Monte Carlo simulations. Not used in live trading critical path due to latency."},
            {"name": "FPGA", "latency": "~100ns-1μs", "flexibility": "Medium", "power": "10-75W", "desc": "Reprogrammable logic gates. Market data parsing, order generation in nanoseconds. Xilinx/AMD Alveo, Intel Stratix. The workhorse of modern HFT."},
            {"name": "ASIC", "latency": "<100ns", "flexibility": "None", "power": "5-50W", "desc": "Application-Specific IC. Fastest possible but cannot be reprogrammed. Used for feed handlers and checksum computation. Extremely expensive to develop."},
        ],
    },
    "software": {
        "title": "Software Stack",
        "layers": [
            {"name": "Kernel Bypass (DPDK/ef_vi)", "desc": "Network packets go directly to userspace, bypassing the OS kernel. Saves ~10μs per packet. Solarflare/Xilinx OpenOnload. Essential for sub-microsecond systems."},
            {"name": "Lock-Free Data Structures", "desc": "No mutexes or locks. Atomic operations only. Disruptor pattern (LMAX). Pre-allocated memory pools. No garbage collection pauses."},
            {"name": "Custom Memory Allocators", "desc": "Arena/bump allocators. No malloc/free in hot path. Memory mapped I/O for shared state. Huge pages (2MB/1GB) to reduce TLB misses."},
            {"name": "C++ / Rust (Critical Path)", "desc": "Zero-cost abstractions. No garbage collection. Compile-time optimization. Template metaprogramming for static dispatch. Rust entering for safety-critical components."},
            {"name": "FPGA HDL (Verilog/VHDL)", "desc": "Hardware description language. Market data parser, order encoder, risk checks — all in hardware. Tick-to-trade in nanoseconds."},
            {"name": "Python (Research/Backtesting)", "desc": "Numpy, Pandas, scikit-learn. Alpha research, signal generation, backtesting. Never in the critical trading path."},
        ],
    },
}

MARKET_VENUES = {
    "equities": [
        {"name": "NYSE", "location": "Mahwah, NJ", "type": "Exchange", "share": "~22%", "note": "New York Stock Exchange. World's largest by market cap. Co-location in Mahwah data center."},
        {"name": "NASDAQ", "location": "Carteret, NJ", "type": "Exchange", "share": "~18%", "note": "Electronic-native. Tech-heavy listings. INET matching engine."},
        {"name": "CBOE (BATS/EDGX/EDGA/BZX)", "location": "Secaucus, NJ", "type": "Exchange", "share": "~20%", "note": "Four equity exchanges under CBOE. Former BATS Global Markets."},
        {"name": "IEX", "location": "Secaucus, NJ", "type": "Exchange", "share": "~3%", "note": "350μs speed bump. 'Flash Boys' exchange. Designed to level playing field."},
        {"name": "MEMX", "location": "Secaucus, NJ", "type": "Exchange", "share": "~5%", "note": "Members Exchange. Founded by major banks and market makers to reduce exchange fees."},
    ],
    "futures": [
        {"name": "CME Group", "location": "Aurora, IL", "type": "Exchange", "share": "~85%", "note": "World's largest futures exchange. E-mini S&P 500, Eurodollars, crude oil, metals. Globex electronic platform."},
        {"name": "ICE (Intercontinental Exchange)", "location": "Various", "type": "Exchange", "share": "~10%", "note": "Energy futures (Brent crude, natural gas), agricultural commodities, fixed income."},
        {"name": "Eurex", "location": "Frankfurt", "type": "Exchange", "share": "~3%", "note": "European derivatives. Euro Stoxx 50, Bund futures. Deutsche Börse subsidiary."},
        {"name": "CBOE Futures", "location": "Various", "type": "Exchange", "share": "~2%", "note": "VIX futures, Bitcoin futures. Volatility product specialist."},
    ],
    "fx": [
        {"name": "EBS (CME)", "location": "Global", "type": "ECN", "share": "~25%", "note": "Primary interbank FX venue for G10 currencies. Now owned by CME Group."},
        {"name": "Refinitiv (LSEG) / Matching", "location": "Global", "type": "ECN", "share": "~20%", "note": "Former Reuters. Major FX venue. Complementary to EBS."},
        {"name": "Hotspot (CBOE)", "location": "Global", "type": "ECN", "share": "~5%", "note": "Institutional FX. Clean order flow preferred by non-bank market makers."},
        {"name": "XTX Markets (internalizer)", "location": "London", "type": "Market Maker", "share": "~10%", "note": "Largest non-bank FX liquidity provider. Internalizes flow, provides streaming prices."},
    ],
    "crypto": [
        {"name": "Binance", "location": "Various", "type": "CEX", "share": "~40%", "note": "Largest crypto exchange by volume. BTC, ETH, and 300+ pairs. Co-location available."},
        {"name": "Coinbase", "location": "USA", "type": "CEX", "share": "~10%", "note": "Largest regulated US crypto exchange. Publicly traded (COIN). Institutional focus."},
        {"name": "Hyperliquid", "location": "Decentralized", "type": "DEX", "share": "~5%", "note": "On-chain perpetual futures. L1 blockchain with order book. Sub-second finality. HyperBFT consensus."},
        {"name": "dYdX", "location": "Decentralized", "type": "DEX", "share": "~3%", "note": "Decentralized perpetual exchange. Cosmos-based L1. Off-chain order book with on-chain settlement."},
    ],
}

STRATEGIES = [
    {"name": "Market Making", "holding": "Microseconds–seconds", "edge": "Spread capture + rebates", "risk": "Inventory risk, adverse selection", "desc": "Quote both bid and ask. Earn the spread. The canonical HFT strategy. Requires speed to avoid being picked off by informed flow."},
    {"name": "Statistical Arbitrage", "holding": "Minutes–hours", "edge": "Mean reversion of correlated assets", "risk": "Model risk, regime change", "desc": "Identify mispricings between related securities. Pairs trading, ETF arbitrage, index arbitrage. More quant than pure HFT."},
    {"name": "Latency Arbitrage", "holding": "Microseconds", "edge": "Speed advantage across venues", "risk": "Infrastructure cost, regulatory", "desc": "Exploit price differences between exchanges before they converge. The 'arms race' strategy. Diminishing returns as latency converges."},
    {"name": "ETF Arbitrage", "holding": "Seconds–minutes", "edge": "NAV vs market price divergence", "risk": "Creation/redemption costs", "desc": "When ETF trades above/below NAV, arbitrage the basket. Jane Street's core competency. Keeps ETF prices efficient."},
    {"name": "Event-Driven (News)", "holding": "Milliseconds–seconds", "edge": "Fastest news parsing", "risk": "Misinterpretation", "desc": "Parse news feeds, economic releases, earnings. NLP/ML to extract signal. Trade before humans can read the headline."},
    {"name": "Momentum Ignition", "holding": "Seconds", "edge": "Triggering other algos", "risk": "Regulatory (market manipulation)", "desc": "Place aggressive orders to trigger momentum-following algos, then trade against them. Grey area — potentially illegal. Hard to prove."},
    {"name": "Cross-Asset Arbitrage", "holding": "Microseconds–seconds", "edge": "Lead-lag between markets", "risk": "Execution risk", "desc": "E-mini S&P futures lead SPY ETF by ~200ms. Trade the follower when the leader moves. Requires presence on multiple venues."},
    {"name": "MEV (Crypto)", "holding": "Milliseconds (block time)", "edge": "Transaction ordering within blocks", "risk": "Protocol risk, competition", "desc": "Maximal Extractable Value. Reorder, insert, or censor transactions within a blockchain block. Sandwich attacks, liquidation frontrunning, arbitrage."},
]

MICROWAVE_ROUTES = [
    {
        "name": "Chicago–New Jersey (The Golden Route)",
        "endpoints": {"from": "CME Aurora, IL", "to": "NYSE Mahwah / NASDAQ Carteret / Equinix Secaucus, NJ"},
        "distance_km": 1130,
        "fiber_latency_ms": 6.55,
        "microwave_latency_ms": 3.97,
        "advantage_ms": 2.58,
        "advantage_pct": 39,
        "num_towers": 20,
        "operators": [
            {"name": "McKay Brothers", "type": "Independent", "status": "Active", "note": "Pioneer. Operational since 2012. Aviat Networks hardware. ~4.09ms one-way. Sells access to multiple firms."},
            {"name": "New Line Networks (NLN)", "type": "Jump/Virtu JV", "status": "Active", "note": "Joint venture of Jump Trading + Virtu Financial. Shortest path. Antenna directly across from CME datacenter. ~3.97ms one-way."},
            {"name": "Spread Networks", "type": "Fiber", "status": "Active (fiber)", "note": "The original $300M dark fiber (2010). 827 miles, 13.1ms → optimized to ~6.55ms. Still used for bandwidth-heavy data."},
            {"name": "Anova Technologies", "type": "Independent", "status": "Active", "note": "Microwave + millimeter wave + laser hybrid. Multiple redundant paths. Sells to buy-side and sell-side."},
            {"name": "Custom Connect", "type": "Independent", "status": "Active", "note": "European-based provider expanding to US routes."},
        ],
        "tower_locations": [
            "Aurora, IL (CME datacenter)", "West Chicago, IL", "Elburn, IL", "Rochelle, IL",
            "Shabbona, IL", "Waterman, IL", "Paw Paw, IL", "Earlville, IL",
            "Wanatah, IN", "Plymouth, IN", "Warsaw, IN", "Fort Wayne, IN",
            "Van Wert, OH", "Upper Sandusky, OH", "Mansfield, OH",
            "Youngstown, OH", "Mercer, PA", "Stroudsburg, PA",
            "Blairstown, NJ", "Mahwah, NJ / Carteret, NJ / Secaucus, NJ"
        ],
        "arb_math": "E-mini S&P 500 (CME Aurora) vs SPY ETF (NYSE Mahwah). Price change at CME takes 3.97ms to reach NJ via microwave vs 6.55ms via fiber. The 2.58ms advantage window allows capturing the price dislocation before fiber-connected firms react. At peak, this was worth ~$1-5M/day across the industry.",
    },
    {
        "name": "London–Frankfurt",
        "endpoints": {"from": "LD4/Slough (London)", "to": "FR2/Frankfurt"},
        "distance_km": 637,
        "fiber_latency_ms": 4.67,
        "microwave_latency_ms": 2.13,
        "advantage_ms": 2.54,
        "advantage_pct": 54,
        "num_towers": 12,
        "operators": [
            {"name": "McKay Brothers (Quincy Data)", "type": "Independent", "status": "Active", "note": "European arm. ~2.15ms one-way."},
            {"name": "Jump Trading", "type": "Proprietary", "status": "Active", "note": "Bought radio tower in Hounslow (near Heathrow) for last-mile advantage. Millimeter wave links."},
            {"name": "Custom Connect", "type": "Independent", "status": "Active", "note": "Dutch provider. Microwave and millimeter wave."},
            {"name": "Anova Technologies", "type": "Independent", "status": "Active", "note": "Laser + microwave hybrid. Belgian route."},
        ],
        "tower_locations": [
            "Slough, UK (Equinix LD4)", "Swingate, UK (Dover cliffs)",
            "Dunkerque, France", "Oostende, Belgium", "Bruges, Belgium",
            "Antwerp, Belgium", "Eindhoven, Netherlands", "Venlo, Netherlands",
            "Duisburg, Germany", "Dusseldorf, Germany", "Cologne, Germany",
            "Frankfurt, Germany (Equinix FR2)"
        ],
        "arb_math": "Eurex (Frankfurt) vs LSE/ICE (London). Bund futures vs UK gilts, Euro Stoxx vs FTSE. 2.54ms advantage enables cross-listing and index arbitrage between the two largest European financial centers.",
    },
    {
        "name": "Tokyo–Osaka",
        "endpoints": {"from": "Equinix TY3 (Tokyo)", "to": "Equinix OS1 (Osaka)"},
        "distance_km": 400,
        "fiber_latency_ms": 3.0,
        "microwave_latency_ms": 1.5,
        "advantage_ms": 1.5,
        "advantage_pct": 50,
        "num_towers": 8,
        "operators": [
            {"name": "McKay Brothers", "type": "Independent", "status": "Active", "note": "Japan network operational. Mountain terrain makes routing challenging."},
        ],
        "tower_locations": [
            "Tokyo (Equinix TY3)", "Yokohama", "Shizuoka", "Hamamatsu",
            "Nagoya", "Suzuka", "Kyoto", "Osaka (Equinix OS1)"
        ],
        "arb_math": "JPX (Tokyo) vs Osaka Exchange (derivatives). Nikkei 225 futures (Osaka) vs constituent stocks (Tokyo). Japan's equity-futures lead-lag arbitrage.",
    },
    {
        "name": "Chicago–Toronto",
        "endpoints": {"from": "CME Aurora, IL", "to": "TMX/MX (Toronto/Montreal)"},
        "distance_km": 700,
        "fiber_latency_ms": 5.0,
        "microwave_latency_ms": 2.5,
        "advantage_ms": 2.5,
        "advantage_pct": 50,
        "num_towers": 10,
        "operators": [
            {"name": "McKay Brothers", "type": "Independent", "status": "Active", "note": "Cross-border microwave. Crosses Lake Michigan routing challenges."},
        ],
        "tower_locations": [
            "Aurora, IL", "Gary, IN", "South Bend, IN", "Kalamazoo, MI",
            "Lansing, MI", "Flint, MI", "Port Huron, MI (border)",
            "London, ON", "Hamilton, ON", "Toronto, ON (TMX)"
        ],
        "arb_math": "S&P/TSX futures vs US index products. CAD/USD FX correlation trades. Cross-border ETF arbitrage (XIU vs SPY).",
    },
    {
        "name": "NJ Triangle (Last Mile)",
        "endpoints": {"from": "NYSE Mahwah", "to": "NASDAQ Carteret / CBOE Secaucus"},
        "distance_km": 56,
        "fiber_latency_ms": 0.35,
        "microwave_latency_ms": 0.19,
        "advantage_ms": 0.16,
        "advantage_pct": 46,
        "num_towers": 3,
        "operators": [
            {"name": "Multiple firms", "type": "Various", "status": "Active", "note": "Short-range millimeter wave and laser links. Every microsecond matters for cross-exchange arb."},
        ],
        "tower_locations": [
            "Mahwah, NJ (NYSE)", "Secaucus, NJ (CBOE/IEX/MEMX)", "Carteret, NJ (NASDAQ)"
        ],
        "arb_math": "Cross-exchange equity arbitrage. Same stock listed on NYSE, NASDAQ, BATS. Price update at one venue creates 160μs window to trade at the others. This is pure latency arbitrage — the strategy that Flash Boys made famous.",
    },
    {
        "name": "London–Paris",
        "endpoints": {"from": "Equinix LD4 (Slough)", "to": "Equinix PA3 (Paris)"},
        "distance_km": 340,
        "fiber_latency_ms": 2.8,
        "microwave_latency_ms": 1.15,
        "advantage_ms": 1.65,
        "advantage_pct": 59,
        "num_towers": 6,
        "operators": [
            {"name": "McKay Brothers", "type": "Independent", "status": "Active", "note": "Channel crossing via microwave. Short route, high advantage percentage."},
        ],
        "tower_locations": [
            "Slough, UK", "Swingate/Dover, UK", "Calais, France",
            "Arras, France", "Compiègne, France", "Paris (Equinix PA3)"
        ],
        "arb_math": "Euronext Paris vs LSE. CAC 40 vs FTSE cross-index arbitrage. FX correlation with EUR/GBP.",
    },
]

LINE_SPEED_COMPARISON = [
    {"medium": "Standard fiber (dark)", "speed_c": 0.67, "speed_kms": 200000, "latency_us_km": 5.0, "bandwidth": "100+ Gbps", "reliability": "99.999%", "cost_tier": 2},
    {"medium": "Hollow-core fiber", "speed_c": 0.997, "speed_kms": 299000, "latency_us_km": 3.34, "bandwidth": "10+ Gbps", "reliability": "99.99%", "cost_tier": 5},
    {"medium": "Microwave (6-11 GHz)", "speed_c": 0.9997, "speed_kms": 299900, "latency_us_km": 3.34, "bandwidth": "0.1-1 Gbps", "reliability": "99.9%", "cost_tier": 3},
    {"medium": "Millimeter wave (60-90 GHz)", "speed_c": 0.9997, "speed_kms": 299900, "latency_us_km": 3.34, "bandwidth": "1-10 Gbps", "reliability": "99.5%", "cost_tier": 4},
    {"medium": "Free-space optical (laser)", "speed_c": 0.9997, "speed_kms": 299900, "latency_us_km": 3.34, "bandwidth": "10-100 Gbps", "reliability": "99.0%", "cost_tier": 5},
    {"medium": "LEO satellite (Starlink)", "speed_c": 0.9997, "speed_kms": 299900, "latency_us_km": 3.34, "bandwidth": "0.1-1 Gbps", "reliability": "99.0%", "cost_tier": 3},
]

MICROWAVE_GAMES = {
    "tower_wars": {
        "title": "The Tower Wars",
        "events": [
            {"year": 2011, "event": "McKay Brothers builds first CHI-NJ microwave", "detail": "~20 towers, 4.1ms one-way. First commercial HFT microwave network. Sold access to multiple firms."},
            {"year": 2013, "event": "Jump Trading builds proprietary network", "detail": "Jump invests ~$100M in its own tower infrastructure. Won't share with competitors. Shortest possible path."},
            {"year": 2015, "event": "New Line Networks (Jump + Virtu JV)", "detail": "Jump and Virtu pool resources. Antenna placed directly across the street from CME datacenter in Aurora, IL. Shaves ~1μs off last-mile."},
            {"year": 2016, "event": "Jump buys Hounslow tower (London)", "detail": "Jump Trading acquires radio tower near Heathrow for London-Frankfurt last-mile advantage. Millimeter wave link to LD4 datacenter in Slough."},
            {"year": 2017, "event": "West Chicago mystery antenna", "detail": "Mysterious shortwave antenna appears in empty field near CME. Linked to 10Band LLC. Purpose: shortwave radio to Europe (~10ms advantage over any other medium for transatlantic). Physics: shortwave bounces off ionosphere."},
            {"year": 2018, "event": "Laser links deployed", "detail": "Anova Technologies deploys free-space optical (laser) links. Higher bandwidth than microwave, same speed, but fog/rain dependent. Hybrid networks emerge."},
            {"year": 2019, "event": "Gazillion-dollar standoff (Bloomberg)", "detail": "Bloomberg profiles the escalating tower arms race. Two firms build competing towers on adjacent properties. Each tower costs $5-14M. The advantage sought: <1 microsecond."},
            {"year": 2021, "event": "LEO satellite experiments", "detail": "SpaceX Starlink investigated for inter-continental low-latency links. Advantage: great-circle routing vs. cable routing. For transatlantic, satellite could beat undersea fiber."},
        ],
    },
    "last_mile": {
        "title": "The Last Mile Problem",
        "detail": "The most expensive microseconds are the first and last. Getting signal from the antenna to the exchange matching engine involves: antenna → cable → building entry → patch panel → switch → server NIC. Each component adds nanoseconds. Firms pay millions to be in the closest rack to the exchange switch. CME and NYSE offer 'equalized cable lengths' — all co-located servers have the same cable distance to the matching engine — but the last-mile from the antenna to the building is not equalized.",
    },
    "weather": {
        "title": "Weather Risk",
        "detail": "Microwave networks fail in heavy rain (signal attenuation). Firms maintain fiber backup circuits that activate automatically. The latency penalty for falling back to fiber (~2.5ms on CHI-NJ) means losing the race during rain events. Some firms have built redundant microwave paths through different weather zones to mitigate correlated rain fade. The reliability vs. speed tradeoff is a core engineering decision.",
    },
    "economics": {
        "title": "The Economics of Microseconds",
        "detail": "A single microsecond of advantage on the CHI-NJ route is estimated to be worth $1-10M per year to a top HFT firm. Building a microwave tower costs $5-14M. Annual spectrum licensing, maintenance, and power: ~$1-2M per tower. A 20-tower network: $100-280M build + $20-40M/year operating. The ROI depends on exclusive vs. shared access — proprietary networks (Jump) capture full value; shared networks (McKay) amortize across clients but allow competing firms to access the same speed.",
    },
}

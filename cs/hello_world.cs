using System;
using System.Collections.Generic;
using System.Linq;

namespace CodeReview
{
    public interface IMarketDataFeed
    {
        string Stock { get; }
        event Action<MarketTick> Tick;
    }

    public interface IIndicator
    {
        event Action<double> IndicatorUpdated;
    }

    public class AverageHalfSpreadIndicator
    {
        private List<MarketTick> _lastTicks;

        public AverageHalfSpreadIndicator(IMarketDataFeed marketDataFeed)
        {
            marketDataFeed.Tick += OnTick;
        }

        private void OnTick(MarketTick ticks)
        {
            _lastTicks.Add(ticks);
            if (_lastTicks.Count == 20)
            {
                _lastTicks.RemoveAt(0);
            }

            var start = DateTime.Now;
            var spreads = _lastTicks.Select(x => 100 * (x.Mid - x.Bid) / x.Bid);
            Console.WriteLine("Time (computing spreads): " + (DateTime.Now -start).TotalMilliseconds + " ms");
            var averageSpread = spreads.Average();
            Console.WriteLine("Time (total): " + (DateTime.Now -start).TotalMilliseconds + " ms");
            IndicatorUpdated(averageSpread);
        }
        public event Action<double> IndicatorUpdated;
    }

    public class MarketTick
    {
        public double Bid { get; set; }
        public double Ask { get; set; }
        public double Last { get; set; }

        public double Mid
        {
            get { return (Bid + Ask) / 2; }
        }
    }

    public class SimpleFeed : IMarketDataFeed
    {
        public string Stock
        {
            get
            {
                return "Apple";
            }
        }

        public event Action<MarketTick> Tick
        {
            add
            {
            }
            remove
            {
            }
        }
    }

    public class HelloWorld
    {
        static public void Main ()
        {
            SimpleFeed foo = new SimpleFeed();
            Console.WriteLine (foo.Stock);
        }
    }

}

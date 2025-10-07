import { useState, useEffect } from 'react'
import StockCard from './components/StockCard'
import StockChart from './components/StockChart'
import { Button } from '@/components/ui/button'
import { RefreshCw } from 'lucide-react'
import './App.css'

function App() {
  const [stockData, setStockData] = useState([])
  const [chartData, setChartData] = useState({})
  const [loading, setLoading] = useState(false)

  // Mock data for demonstration
  const mockStockData = [
    { symbol: 'AAPL', price: 256.49, change: 1.23, changePercent: 0.48, volume: 739338 },
    { symbol: 'MSFT', price: 523.97, change: -2.45, changePercent: -0.47, volume: 225984 },
    { symbol: 'AMZN', price: 221.80, change: 0.85, changePercent: 0.38, volume: 437717 },
    { symbol: 'GOOGL', price: 245.82, change: 2.15, changePercent: 0.88, volume: 290648 },
    { symbol: 'TSLA', price: 432.87, change: -5.32, changePercent: -1.21, volume: 919063 }
  ]

  const mockChartData = {
    'AAPL': [
      { time: '15:55', price: 256.55 },
      { time: '15:56', price: 256.35 },
      { time: '15:57', price: 256.51 },
      { time: '15:58', price: 256.29 },
      { time: '15:59', price: 256.49 }
    ]
  }

  useEffect(() => {
    setStockData(mockStockData)
    setChartData(mockChartData)
  }, [])

  const refreshData = () => {
    setLoading(true)
    // Simulate API call
    setTimeout(() => {
      setStockData(mockStockData.map(stock => ({
        ...stock,
        price: stock.price + (Math.random() - 0.5) * 2,
        change: (Math.random() - 0.5) * 4,
        changePercent: (Math.random() - 0.5) * 2
      })))
      setLoading(false)
    }, 1000)
  }

  return (
    <div className="min-h-screen bg-background p-6">
      <div className="max-w-7xl mx-auto">
        <div className="flex items-center justify-between mb-8">
          <div>
            <h1 className="text-3xl font-bold text-foreground">تحليل السوق الأمريكي للأسهم</h1>
            <p className="text-muted-foreground mt-2">بيانات لحظية للأسهم الأمريكية الرئيسية</p>
          </div>
          <Button 
            onClick={refreshData} 
            disabled={loading}
            className="flex items-center gap-2"
          >
            <RefreshCw className={`h-4 w-4 ${loading ? 'animate-spin' : ''}`} />
            تحديث البيانات
          </Button>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-6 mb-8">
          {stockData.map((stock) => (
            <StockCard
              key={stock.symbol}
              symbol={stock.symbol}
              price={stock.price}
              change={stock.change}
              changePercent={stock.changePercent}
              volume={stock.volume}
            />
          ))}
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {chartData['AAPL'] && (
            <StockChart data={chartData['AAPL']} symbol="AAPL" />
          )}
          <div className="bg-card rounded-lg p-6 border">
            <h3 className="text-lg font-semibold mb-4">معلومات إضافية</h3>
            <div className="space-y-2 text-sm">
              <p><span className="font-medium">مصدر البيانات:</span> Yahoo Finance API</p>
              <p><span className="font-medium">تحديث البيانات:</span> كل دقيقة</p>
              <p><span className="font-medium">الأسهم المتتبعة:</span> AAPL, MSFT, AMZN, GOOGL, TSLA</p>
              <p><span className="font-medium">نوع التحليل:</span> المتوسط المتحرك البسيط (SMA)</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default App

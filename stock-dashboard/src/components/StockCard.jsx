import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { TrendingUp, TrendingDown } from 'lucide-react'

const StockCard = ({ symbol, price, change, changePercent, volume }) => {
  const isPositive = change >= 0
  
  return (
    <Card className="w-full">
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
        <CardTitle className="text-sm font-medium">{symbol}</CardTitle>
        {isPositive ? (
          <TrendingUp className="h-4 w-4 text-green-600" />
        ) : (
          <TrendingDown className="h-4 w-4 text-red-600" />
        )}
      </CardHeader>
      <CardContent>
        <div className="text-2xl font-bold">${price?.toFixed(2)}</div>
        <p className={`text-xs ${isPositive ? 'text-green-600' : 'text-red-600'}`}>
          {isPositive ? '+' : ''}{change?.toFixed(2)} ({changePercent?.toFixed(2)}%)
        </p>
        <p className="text-xs text-muted-foreground mt-1">
          الحجم: {volume?.toLocaleString()}
        </p>
      </CardContent>
    </Card>
  )
}

export default StockCard

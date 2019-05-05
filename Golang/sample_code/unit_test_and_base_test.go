// 名为testing的包被专门用来进行自动化测试, 日志和错误报告, 并且包含一些基准测试函数功能
//测试程序必须属于被测试的包, 并且文件名满足 *_test.go

//测试函数头部必须为这种形式:
fun TestAbcd(t *testing.T)
//T是传给测试函数的结构类型, 用来管理测试状态, 支持格式化测试日志
//如t.Log, t.Error, t.ErrorF

func (t *T) Fail() 		// 标记测试函数为失败, 然后继续执行
func (t *T) FailNow() 	// 标记测试函数为失败并终止执行;文件中其他测试被忽略, 继续执行下一个文件
func (t *T) Log(args ...interface{}) // args 被用默认格式打印到错误日志中
func (t *T) Fatal(args ...interface{}) // 标记为失败并终止, 然后写入错误日志

// 使用--chatty 或-v 选项, 每个测试函数及测试状态会被打印
go test fmt_test.go --chatty 

//简单的基准测试函数 
func BenchmarkReverse(b *testing.B) {
	...
}

go test -test.bech=.*  //运行所有基准测试函数


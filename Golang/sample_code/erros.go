/* original url: https://github.com/Unknwon/the-way-to-go_ZH_CN/blob/master/eBook/13.1.md
 * <the way to go>
 * 13 错误处理与测试
 */

// Go 检查和报告错误条件的惯有方式：
//产生错误的函数会返回两个变量，一个值和一个错误码；如果后者是 nil 就是成功，非 nil 就是发生了错误。
//为了防止发生错误时正在执行的函数（如果有必要的话甚至会是整个程序）被中止，在调用函数后必须检查错误。
if value, err := pack1.Func1(param1); err != nil {
	fmt.Printf("Error %s in pack1.Func1 with parameter %v", err.Error(), param1)
	return err
} else {
	//Process(value)
}
 
// Go 的预定义接口类型
type error interface {
	Error() string
}

//定义错误
err := errors.New("math - squre root of negative number")

// eorrors.go
package main

import (
	"errors"
	"fmt"
)

var errNotFound error = error = errors.New("Not found error")

func main() {
	fmt.Printf("error: %v", errNotFound)
}

// 当发生如数组下标越界或类型断言失败这样的运行时错误时,
// Go运行时会触发运行时panic,
// 伴随程序的崩溃抛出一个runtime.Error 接口类型的值
// 这个值有个RuntimeError()方法用于区分普通错误

package main
import "fmt"
func main() {
	fmt.Println("Starting the program")
	panic("Aserver error occured: stopping the program!")
	fmt.Println("Ending the program")
}

//一个检查程序是否被已知用户启动的具体例子
var user = os.Getenv("USER")
func check() {
	if user == "" {
		panic("Unknown user: no value for $USER")
	}
}

// panic可用于错误处理模式
if error != nil {
	panic("ERROR occured:" + err.Error())
}

// recover内建函数被用于从panic或错误场景中恢复: 让程序
// 可以从panicking重新获得控制权, 停止终止过程而恢复正常执行


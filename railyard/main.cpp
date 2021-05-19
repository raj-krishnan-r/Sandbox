#include <stdio.h>
class Stack
{
    int top = 0;
    char operators[500];

public:
    void push(char c)
    {
        operators[top++] = c;
    }
    char pop()
    {
        if (top < 0)
        {
            return '!';
        }
        return operators[--top];
    }
    char stackTop()
    {
        return operators[top - 1];
    }
    bool stackEmpty()
    {
        if (top < 0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};
bool isOperator(char);
int precedenceOf(char);
int main()
{
    Stack stack;
    char exp[100];
    printf("Expression : ");
    scanf("%s", exp);

    int start = 0;
    while (exp[start] != '\0')
    {
        if (!isOperator(exp[start]))
        {
            printf("%c", exp[start]);
        }
        else if (isOperator(exp[start]))
        {
            while ((!stack.stackEmpty()) && (precedenceOf(stack.stackTop()) >= precedenceOf(exp[start])) && (stack.stackTop() != '('))
            {
                printf("%c", stack.pop());
            }
            stack.push(exp[start]);
        }
        else if (exp[start] == '(')
        {
            stack.push('(');
        }
        else if (exp[start] == ')')
        {
            while (stack.stackTop() != '(')
            {
                printf("%c", stack.pop());
            }
            if (stack.stackTop() == '(')
            {
                stack.pop();
            }
        }
    }
    while (!stack.stackEmpty())
    {
        printf("%c", stack.pop());
    }
}

bool isOperator(char c)
{
    if (c == '+')
    {
        return true;
    }
    else if (c == '*')
    {
        return true;
    }
    else if (c == '/')
    {
        return true;
    }
    else if (c == '-')
    {
        return true;
    }
    else
    {
        return false;
    }
}
int precedenceOf(char c)
{
    if (c == '+')
    {
        return 2;
    }
    else if (c == '*')
    {
        return 3;
    }
    else if (c == '/')
    {
        return 3;
    }
    else if (c == '-')
    {
        return 2;
    }
    else
    {
        return 4;
    }
}
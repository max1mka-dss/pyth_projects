{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "7lPyzNzeLIOj"
   },
   "source": [
    "# Базовые структуры данных\n",
    "\n",
    "\n",
    "\n",
    "## Домашнее задание \n",
    "\n",
    "### Описание домашнего задания и формат сдачи\n",
    "\n",
    "Решите предложенные задачи по программированию — впишите свой код в ячейки после условий задач вместо комментария `### YOUR CODE HERE ###` в файле *jun_anl_data_structures.ipynb* и сохраните изменения, используя опцию *Save and Checkpoint* из вкладки меню *File* или кнопку *Save and Checkpoint* на панели инструментов. Итоговый файл в формате `.ipynb` (файл Jupyter Notebook) загрузите в личный кабинет обучающей онлайн-платформы Skillbox (https://go.skillbox.ru/) и отправьте на проверку."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "awb1K2hlLIOl"
   },
   "source": [
    "**NB!** Во всех заданиях обязательно наличие выдачи."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "3ndIOSVeLIOm"
   },
   "source": [
    "## Индексация списка"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "YBj2DZxnmQzq"
   },
   "source": [
    "**Цель блока заданий:** в данном блоке задач вы потренируетесь вызывать элементы или группы элементов из списка. \n",
    "\n",
    "**Рекомендации к выполнению блока заданий:** попробуйте разделить задание на части, поэтапно вызывайте по индексу составные части (которые могут также являться списками) из списка, пока не дойдёте до нужного элемента.\n",
    "\n",
    "**Критерии оценки:** задания считаются выполненными, если выдача строго соответствует примеру из каждого задания. Допустим, в пятом задании результатом должен быть список с единственным элементом, равным 74."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "XSWqZnZ2LIOo"
   },
   "outputs": [],
   "source": [
    "L = [[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], \n",
    "    [[21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]], \n",
    "    [[41, 42, 43, 44, 45], [46, [47, 48], 49, 50], [51, 52, 53, 54, 55], [56, 57, 58, 59, 60]], \n",
    "    [61, 62, 63, [64, 65, 66, 67, 68, 69, 70, 71], 72, 73, 74, [75, [76, 77, 78], 79], 80], \n",
    "    [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "jwigC9WlLIOt"
   },
   "source": [
    "### 1.\n",
    "Из приведённого выше списка списков выведите с помощью индексов число `7`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "PDaSjPzRLIOu"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L[0][0][6]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "TF6eb9fYLIOw"
   },
   "source": [
    "### 2.\n",
    "Из приведённого выше списка списков выведите с помощью индексов число `49`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "l_oW37-qLIOx"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "49"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L[2][1][2]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "FBDB0JeBLIO1"
   },
   "source": [
    "### 3.\n",
    "Из приведённого выше списка списков выведите с помощью индексов число `78`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "tpM-jm4bLIO2"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "78"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L[3][7][1][2]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "gnaTfR3BLIO5"
   },
   "source": [
    "### 4.\n",
    "Из приведённого выше списка списков выведите с помощью индексов (используя **отрицательные значения**) число `99`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "sA0ImW8oLIO6"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "99"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L[4][18]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "07mV6-oeLIO-"
   },
   "source": [
    "### 5.\n",
    "Из приведённого выше списка списков сделайте **срез** с числом `74`. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "OM-zgJ15LIO-"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[74]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L[3][6:7]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "TE82rH0CLIPB"
   },
   "source": [
    "### 6.\n",
    "Из приведённого выше списка списков сделайте **срез** с числами `47, 48`. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "MKpqyOINLIPD"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[47, 48]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L[2][1][1][:]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "t6Fgb0AkLIPK"
   },
   "source": [
    "### 7.\n",
    "Из приведённого выше списка списков сделайте **срез** с числами `77, 78`. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "l1pGFe7uLIPM"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[77, 78]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L[3][7][1][1:]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "RwOlYKGhLIPR"
   },
   "source": [
    "## Функция range()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "xsF_OmeImQ1t"
   },
   "source": [
    "**Цель блока заданий:** в данном блоке задач вы закрепите навык генерации числовых последовательностей через функцию range(). В дальнейшем функция range() будет часто использоваться в счётных циклах, а также для решения других задач.\n",
    "\n",
    "**Рекомендации к выполнению блока заданий:** обратите внимание, что шаг последовательности может быть как «вперед», так и «назад». Для вывода результата в формате списка можно использовать функцию list().\n",
    "\n",
    "**Критерии оценки:** задания считаются выполненными, если выдача строго соответствует примеру из задания. Использование функций сортировки не допускается."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "s2K0_TThLIPR"
   },
   "source": [
    "### 8.\n",
    "С помощью функции `range` сгенерируйте следующую последовательность: <br>\n",
    "`[0, 1, 2, 3, 4]`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "vpuvqwqdLIPS"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 2, 3, 4]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_list_1 = list(range(0, 5))\n",
    "my_list_1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "WyhA3ipeLIPU"
   },
   "source": [
    "### 9.\n",
    "С помощью функции `range` сгенерируйте следующую последовательность: <br>\n",
    "`[3, 4]`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "WHoyVxCeLIPV"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 4]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_list_2 = list(range(3, 5))\n",
    "my_list_2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "Clfo7jhOLIPY"
   },
   "source": [
    "### 10.\n",
    "С помощью функции `range` сгенерируйте следующую последовательность: <br>\n",
    "`[4, 8, 12, 16]`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "WepJj6ZfLIPY"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[4, 8, 12, 16]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_list_3 = list(range(4, 17, 4))\n",
    "my_list_3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "U9glCsGCLIPb"
   },
   "source": [
    "### 11.\n",
    "С помощью функции `range` сгенерируйте следующую последовательность: <br>\n",
    "`[16, 12, 8, 4]`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "NDm-DmpTLIPc"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[16, 12, 8, 4]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_list_4 = list(range(16, 3, -4))\n",
    "my_list_4"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "CHz6UIKyLIPi"
   },
   "source": [
    "### 12.\n",
    "С помощью функции `range` сгенерируйте следующую последовательность: <br>\n",
    "`[0, 5, 10]`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "9C06f5sTLIPj"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 5, 10]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_list_5 = list(range(0, 11, 5))\n",
    "my_list_5"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "ZZehpNQuLIPm"
   },
   "source": [
    "### 13.\n",
    "С помощью функции `range` сгенерируйте следующую последовательность: <br>\n",
    "`[10, 5, 0]`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "H4QmyUfZLIPm"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[10, 5, 0]"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_list_6 = list(range(10, -1, -5))\n",
    "my_list_6"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "kwWQ1al2LIPr"
   },
   "source": [
    "### 14.\n",
    "С помощью функции `range` сгенерируйте следующую последовательность: <br>\n",
    "`[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "85HO3S_cLIPu"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_list_7 = list(range(-10, 0, 1))\n",
    "my_list_7"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "sbCO0FbLLIP3"
   },
   "source": [
    "### 15.\n",
    "С помощью функции `range` сгенерируйте следующую последовательность: <br>\n",
    "`[-10, -16, -22, -28, -34]`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "Frychu-HLIP4"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[-10, -16, -22, -28, -34]"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_list_8 = list(range(-10, -35, -6))\n",
    "my_list_8"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "1Gfu4kFqLIP-"
   },
   "source": [
    "## Операторы и типы данных\n",
    "\n",
    "Этот блок должен быть решён **БЕЗ** использования готовых функций и сторонних библиотек. Используйте операторы."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "0csxPvg4mQ3H"
   },
   "source": [
    "**Цель блока заданий:** в данном блоке задач вы потренируетесь в использовании базовых операторов в Python.\n",
    "\n",
    "**Рекомендации к выполнению блока заданий:** выполнить данные задания можно опираясь на знания, полученные в этом и предшествующих модулях. Подумайте, как можно решить задачу простыми инструментами, если вам кажется, что для её выполнения необходим метод, с которым вы не знакомились в этом и предшествующих модулях.\n",
    "\n",
    "**Критерии оценки:** задания считаются выполенными, если программа выводит корректный ответ в нужном формате. Формат выдачи приведён к каждому заданию. В решении не должны быть задействованы циклы, условия, функции, исключения, которые являются темами следующих модулей. Проверка корректности входных значений не требуется."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "qnWdcLseLIP_"
   },
   "source": [
    "### 16.\n",
    "Часы показывают время в формате h:mm:ss (количество часов (от 0 до 23), двузначное количество минут, двузначное количество секунд). Количество минут и секунд при необходимости дополняются до двузначного числа нулями.\n",
    "\n",
    "Программа должна запрашивать количество секунд S, которое прошло с начала суток, и выводить в формате h:mm:ss, какое время будут показывать часы. <br><br>\n",
    "\n",
    "*Формат ввода:* <br>\n",
    "3600<br><br>\n",
    "\n",
    "*Формат вывода:* <br>\n",
    "1:00:00"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "UaM4-TFYLIP_"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введите количество секунд 3600\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'1:00:00'"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "S = int(input('Введите количество секунд '))\n",
    "h = int(S/3600)\n",
    "mm = int((S % 3600) / 60)\n",
    "m1 = mm//10\n",
    "m2 = mm%10\n",
    "ss = (S % 3600) % 60\n",
    "s1 = ss//10\n",
    "s2 = ss%10\n",
    "res = str(h) + ':' + str(m1)+ str(m2) + ':' + str(s1) + str(s2)\n",
    "res"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "BnxMhHlDLIQB"
   },
   "source": [
    "### 17.\n",
    "Машина выезжает на нулевой километр МКАД и едет по часовой стрелке с постоянной скоростью V километров в час. На каком километре МКАД машина окажется через T часов? \n",
    "<br> Длина МКАД: 109 км. <br><br> \n",
    "\n",
    "*Формат ввода:* <br>\n",
    "60 <br>\n",
    "1\n",
    "<br><br>\n",
    "*Формат вывода:* <br>\n",
    "60"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "66aeGuRbLIQC"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введите скорость, км/ч: 60\n",
      "Введите время, ч: 1\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "60"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "V = int(input('Введите скорость, км/ч: '))\n",
    "T = int(input('Введите время, ч: '))\n",
    "D = V*T\n",
    "km = D % 109\n",
    "km"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "ZxMi6_58LIQG"
   },
   "source": [
    "### 18.\n",
    "Напишите программу, которая запрашивает целое пятизначное число и выводит сумму его цифр.\n",
    "\n",
    "*Формат ввода:* <br>\n",
    "11111\n",
    "<br><br>\n",
    "*Формат вывода:* <br>\n",
    "5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "wasIkbwELIQH"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введите пятизначное число 11111\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "num = input('Введите пятизначное число ')\n",
    "sum = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3]) + int(num[4])\n",
    "print(sum)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "6q6JEgziLIQK"
   },
   "source": [
    "### 19.\n",
    "Напишите программу, которая запрашивает целое четырёхзначное число и меняет местами его две первые и две последние цифры.\n",
    "\n",
    "*Формат ввода:* <br>\n",
    "5236 \n",
    "<br><br>\n",
    "*Формат вывода:* <br>\n",
    "3652"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "tupFycemLIQK"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введите четырёхзначное число 5236\n",
      "3652\n"
     ]
    }
   ],
   "source": [
    "num = int(input('Введите четырёхзначное число '))\n",
    "a = num // 100\n",
    "b = num % 100\n",
    "a, b = b, a\n",
    "print(a*100 + b)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "3NglY6CQLIQN"
   },
   "source": [
    "#### 20.\n",
    "Напишите программу, которая на основании параметра D (сколько километров в день преодолевает машина) рассчитывает, сколько дней она затратит на путь длиной P километров.  <br><br>\n",
    "*Формат ввода:* <br>\n",
    "105 <br>\n",
    "120\n",
    "<br><br>\n",
    "*Формат вывода:* <br>\n",
    "2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "7sCggR--LIQN"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введите количество км за день: 200\n",
      "Введите общий путь, км: 50\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "D = int(input('Введите количество км за день: '))\n",
    "P = int(input('Введите общий путь, км: '))\n",
    "days = (P + D - 1)//D\n",
    "days\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "oWERt2BRLIQR"
   },
   "source": [
    "### 21.\n",
    "Напишите программу, которая считает, сколько рублей и копеек нужно заплатить за N авокадо, если одно авокадо стоит R рублей и K копеек. <br><br>\n",
    "*Формат ввода:* <br>\n",
    "40 20 <br>\n",
    "5\n",
    "<br><br>\n",
    "*Формат вывода:* <br>\n",
    "201 руб. 00 коп."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "Zvx5ybP7LIQU"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введите цену авокадо (_ рублей _ копеек)40 20\n",
      "Введите количество авокадо: 5\n",
      "201 руб. 00 коп.\n"
     ]
    }
   ],
   "source": [
    "R, K = map(int, input('Введите цену авокадо (_ рублей _ копеек)').split())\n",
    "N = int(input('Введите количество авокадо: '))\n",
    "sum = R*N + (K*N)/100\n",
    "r = int(sum)\n",
    "k = int((sum - r) * 100)\n",
    "k1 = k//10\n",
    "k2 = k%10\n",
    "print(r, 'руб.', str(k1) + str(k2), 'коп.')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "Q0u91-MILIQX"
   },
   "source": [
    "### 22.\n",
    "Пусть организаторы мероприятия неправильно составили гугл-форму и просили людей указывать ФИО в неправильном порядке. Сначала спрашивали имя, потом отчество, затем фамилию. Напишите программу, которая будет переставлять ФИО в нужный порядок. <br> <br> \n",
    "\n",
    "*Формат ввода:* <br>\n",
    "Иван Иванович Иванов<br><br>\n",
    "*Формат вывода:* <br>\n",
    "Иванов Иван Иванович"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "hrXguBL7LIQX"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введите Имя Отчество Фамилию: Иван Иванович Иванов\n",
      "Иванов Иван Иванович\n"
     ]
    }
   ],
   "source": [
    "name, patroymic, surname = map(str, input('Введите Имя Отчество Фамилию: ').split())\n",
    "print(surname, name, patroymic)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "vwexBPelLIQb"
   },
   "source": [
    "## Cловари и списки"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "K51IjN6QmQ30"
   },
   "source": [
    "**Цель блока заданий:** в данном блоке задач вы зарепите навык работы со словарями и списками. В текущем блоке также пригодятся навыки, отработанные в первом блоке настоящего домашнего задания.\n",
    "\n",
    "**Рекомендации к выполнению блока заданий:** попробуйте работать с большим словарём по тому же принципу, по которому вы вызывали составные элементы из большого списка в первом блоке заданий настоящей работы. Поэтапно вызывайте сначала один многосоставный объект, затем из него извлеките другой, но уже меньший, пока не доберётесь до целевого элемента.\n",
    "\n",
    "**Критерии оценки:** задания считаются выполненными, если произошли нужные изменения (или их отстутсвие, если того требует условие задания), но при этом не произошло никаких других изменений, которые не описаны в задании. Обратите, пожалуйста, внимание, что программа в 23-й задаче должна быть универсальной, то есть работать не только для нулевого элемента."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "nIgc10tKLIQc"
   },
   "source": [
    "### 23.\n",
    "У вас есть список с заказом в ресторане. Напишите программу, которая меняет указанное по названию блюдо на другое. При этом новое блюдо в списке будет расположено на месте того, что было заменено.\n",
    "\n",
    "*Формат ввода:* <br>\n",
    "белое вино<br>\n",
    "красное вино <br><br>\n",
    "*Формат вывода:* <br>\n",
    "`['красное вино', 'салат Цезарь', 'паста Карбонара', 'чизкейк', 'шоколадный сорбет']`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "O0k3dslvLIQd"
   },
   "outputs": [],
   "source": [
    "order = ['белое вино', 'салат Цезарь', 'паста Карбонара', 'чизкейк', 'шоколадный сорбет']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "D9s6foo_LIQh"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введите блюдо, которое хотите заменить: белое вино\n",
      "Введите блюдо на, которое хотите заменить: красное вино\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "['красное вино',\n",
       " 'салат Цезарь',\n",
       " 'паста Карбонара',\n",
       " 'чизкейк',\n",
       " 'шоколадный сорбет']"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pos1 = input('Введите блюдо, которое хотите заменить: ')\n",
    "pos2 = input('Введите блюдо на, которое хотите заменить: ')\n",
    "ind = order.index(pos1)\n",
    "order[ind] = pos2\n",
    "order"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "GLx0EKUiLIQj"
   },
   "source": [
    "__________________\n",
    "Вам дан словарь c расписанием на неделю. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "fbPqWtv_LIQl"
   },
   "outputs": [],
   "source": [
    "diary = {'понедельник': {\n",
    "                          'утро': ['погулять с собакой'],\n",
    "                          'день': [],\n",
    "                          'вечер': ['погулять с собакой']\n",
    "                                      },\n",
    "        'вторник': {\n",
    "                          'утро': ['погулять с собакой'],\n",
    "                          'день': [],\n",
    "                          'вечер': ['погулять с собакой']\n",
    "                                      },\n",
    "        'среда': {\n",
    "                          'утро': ['погулять с собакой'],\n",
    "                          'день': [],\n",
    "                          'вечер': ['погулять с собакой']\n",
    "                                      },\n",
    "        'четверг': {\n",
    "                          'утро': ['погулять с собакой'],\n",
    "                          'день': [],\n",
    "                          'вечер': ['погулять с собакой']\n",
    "                                      },\n",
    "        'пятница': {\n",
    "                          'утро': ['заехать в шиномонтаж', 'помыть машину'],\n",
    "                          'день': [],\n",
    "                          'вечер': ['поход в театр',  'ужин в кафе']\n",
    "                                      },\n",
    "        'суббота': {\n",
    "                          'утро': [],\n",
    "                          'день': [],\n",
    "                          'вечер': []\n",
    "                                      },\n",
    "        'воскресенье': {\n",
    "                          'утро': [],\n",
    "                          'день': [],\n",
    "                          'вечер': []\n",
    "                                      }}"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "3FocVZkgLIQn"
   },
   "source": [
    "### 24.\n",
    "Удалите ключи `суббота` и `воскресенье`. Вместо них добавьте пару, где ключ — это кортеж `суббота, воскресенье`, а значение — список с делом `посадить цветы на даче`. Можно ли сделать ключ `суббота, воскресенье` списком?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "lcw8GWcnLIQo"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'понедельник': {'утро': ['погулять с собакой'], 'день': [], 'вечер': ['погулять с собакой']}, 'вторник': {'утро': ['погулять с собакой'], 'день': [], 'вечер': ['погулять с собакой']}, 'среда': {'утро': ['погулять с собакой'], 'день': [], 'вечер': ['погулять с собакой']}, 'четверг': {'утро': ['погулять с собакой'], 'день': [], 'вечер': ['погулять с собакой']}, 'пятница': {'утро': ['заехать в шиномонтаж', 'помыть машину'], 'день': [], 'вечер': ['поход в театр', 'ужин в кафе']}, ('суббота', 'воскресенье'): ['посадить цветы на даче']}\n"
     ]
    }
   ],
   "source": [
    "del diary['суббота']\n",
    "del diary['воскресенье']\n",
    "diary[('суббота','воскресенье')] = ['посадить цветы на даче']\n",
    "print(diary)\n",
    "# ключ не может быть списком, так как кюч должен быть неизменяемым объектом\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "vVhNCrtLLIQs"
   },
   "source": [
    "### 25.\n",
    "Добавьте в список дел во вторник утром `поход к зубному`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "R4BiwaWlLIQu"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['погулять с собакой', 'Поход к зубному']\n"
     ]
    }
   ],
   "source": [
    "diary['вторник']['утро'].append('Поход к зубному')\n",
    "print(diary['вторник']['утро'])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "BPQ5R-PkLIQ2"
   },
   "source": [
    "### 26.\n",
    "Замените `поход в театр` на `поход в кино` в списке дел в пятницу вечером."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "nhqzOrZILIQ5"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['поход в кино', 'ужин в кафе']\n"
     ]
    }
   ],
   "source": [
    "ind = diary['пятница']['вечер'].index('поход в театр')\n",
    "diary['пятница']['вечер'][ind] = 'поход в кино'\n",
    "print(diary['пятница']['вечер'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "HCE0aq_BLIQ7"
   },
   "source": [
    "### 27.\n",
    "Ваш друг вернётся из отпуска на один день раньше, поэтому он заберёт свою собаку в среду, а не в четверг. Удалите дело `погулять с собакой` из соответствующих списков."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "WPnIXdTVLIQ7"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'понедельник': {'утро': ['погулять с собакой'], 'день': [], 'вечер': ['погулять с собакой']}, 'вторник': {'утро': ['погулять с собакой'], 'день': [], 'вечер': ['погулять с собакой']}, 'среда': {'утро': ['погулять с собакой'], 'день': [], 'вечер': []}, 'четверг': {'утро': [], 'день': [], 'вечер': []}, 'пятница': {'утро': ['заехать в шиномонтаж', 'помыть машину'], 'день': [], 'вечер': ['поход в театр', 'ужин в кафе']}, 'суббота': {'утро': [], 'день': [], 'вечер': []}, 'воскресенье': {'утро': [], 'день': [], 'вечер': []}}\n"
     ]
    }
   ],
   "source": [
    "diary['среда']['вечер'].remove('погулять с собакой')\n",
    "diary['четверг']['утро'].remove('погулять с собакой')\n",
    "diary['четверг']['вечер'].remove('погулять с собакой')\n",
    "print(diary)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "A80KVUrZLIQ9"
   },
   "source": [
    "### 28.\n",
    "Выведите второе дело из списка дел, которые вам нужно сделать в пятницу утром."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "ofqEBNuZLIQ-"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "помыть машину\n"
     ]
    }
   ],
   "source": [
    "print(diary['пятница']['утро'][1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "colab": {
   "collapsed_sections": [
    "t6Fgb0AkLIPK",
    "s2K0_TThLIPR",
    "WyhA3ipeLIPU",
    "Clfo7jhOLIPY",
    "U9glCsGCLIPb",
    "CHz6UIKyLIPi",
    "ZZehpNQuLIPm",
    "kwWQ1al2LIPr",
    "qnWdcLseLIP_",
    "BnxMhHlDLIQB",
    "ZxMi6_58LIQG",
    "6q6JEgziLIQK",
    "3NglY6CQLIQN",
    "oWERt2BRLIQR",
    "Q0u91-MILIQX",
    "nIgc10tKLIQc",
    "3FocVZkgLIQn",
    "vVhNCrtLLIQs",
    "BPQ5R-PkLIQ2",
    "HCE0aq_BLIQ7"
   ],
   "name": "jun_anl_data_structures_.ipynb",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}

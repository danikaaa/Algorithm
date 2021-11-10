import time # 시간 측정 위해 time 모듈 추가
import random # 리스트를 무작위로 섞기위해 random 모듈 추가

m = int(input("데이터의 개수 : ")) # 데이터의 개수를 입력받음 
print("\n")

# 병합 정렬
def merge_sort(a):

    def sort(left, right):
        if right - left < 2:
            return
        mid = (left + right) // 2       # left와 right의 중간 지점 계산
        sort(left, mid)                 # 왼쪽 부분 배열 정렬
        sort(mid, right)                # 오른쪽 부분 배열 정렬
        merge(left, mid, right)         # 병합

    def merge(left, mid, right):
        tmp = []
        l, r = left, mid

        while l < mid and r < right:
            if a[l] < a[r]:             # a[l]보다 a[r]이 크면
                tmp.append(a[l])        # tmp에 l이 1씩 증가
                l += 1
            else:
                tmp.append(a[r])        # 아니면 r이 1씩 증가
                r += 1

        while l < mid:              # 왼쪽 부분 배열만 남아있을 때
            tmp.append(a[l])        # tmp에 l이 1씩 증가
            l += 1
        while r < right:            # 오른쪽 부분 배열만 남아있을 때
            tmp.append(a[r])        # tmpdp r이 1씩 증가
            r += 1

        for i in range(left, right):    # 결과를 a[i]에 저장
            a[i] = tmp[i - left]

    return sort(0, len(a))


# 퀵 정렬
def quick_sort(a,start,end):
    if start>= end:         # 원소가 1개 이하인 경우 종료
        return
    piv = start           # 첫번째 값 piv
    left = start + 1      # a[piv]보다 큰 값 저장
    right = end           # a[piv]보다 작은 값 저장
    
    while left<=right:
                                                    
        while left<=end and a[left]<=a[piv]:              # 피벗보다 큰 데이터를 찾을 때까지 반복
            left +=1
        while right>start and a[right]>= a[piv]:
            right-=1
        if left>right:                                      # left가 right가 엇갈린 경우
            a[right],a[piv]= a[piv],a[right]            # a[right]와  a[piv]의 자리 교환
        else:                                               # 엇갈리지 않은 경우
            a[left],a[right]=a[right],a[left]               # a[left]와 a[right]이 자리 교환
    
    quick_sort(a, start,right-1)           #분할 후 왼쪽 부분에서 다시 정렬 수행
    quick_sort(a,right+1,end)              #분할 후 오른쪽 부분에서 다시 정렬 수행




   
ls = [x for x in range(m)] #  m개의 원소를 갖는 리스트
random.shuffle(ls) # 정렬하기 전 랜덤으로 섞기
ls2 = ls[:] # 퀵 정렬에 사용하는 리스트


start = time.time()
merge_sort(ls) # 병합 정렬 실행 시간
merge_time = time.time() - start

start = time.time()
quick_sort(ls2,0,len(ls2)-1)    # 합쳐서 정렬 
quick_time = time.time() - start # 퀵 정렬 실행 시간


# 출력문 ㅎㅎ
print("<<<병합 정렬>>>")
print("실행시간 : ", merge_time,"\n")

print("<<<퀵 정렬>>>")
print("실행시간 : ", quick_time)

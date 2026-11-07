#
# Copyright (C) 2026 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

MIUICAMERA_PATH := device/xiaomi/miuicamera-everpal

-include vendor/xiaomi/miuicamera-everpal/BoardConfigVendor.mk

TARGET_SYSTEM_PROP += $(MIUICAMERA_PATH)/system.prop
TARGET_VENDOR_PROP += $(MIUICAMERA_PATH)/vendor.prop

BOARD_VENDOR_SEPOLICY_DIRS += $(MIUICAMERA_PATH)/sepolicy/vendor
